#!/usr/bin/env node
/**
 * Pocket Toolkit (JavaScript edition): the twin of the Python example.
 *
 * Tools:     roll_dice, random_fortune, save_note, list_notes
 * Resource:  notes://all
 * Prompt:    daily_standup
 *
 * Uses the official MCP TypeScript SDK. Plain .mjs, so no build step needed.
 * (Want real TypeScript? Rename to .ts, add type annotations, and run with `npx tsx server.ts`.)
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { z } from "zod";

const NOTES_FILE = join(dirname(fileURLToPath(import.meta.url)), "notes.json");

const FORTUNES = [
  "The bug you're hunting is in the file you haven't opened yet.",
  "A small automation today saves a hundred clicks tomorrow.",
  "You are one config file away from something awesome.",
  "Curiosity is your best debugger.",
  "Ship the weird little project. The weird ones teach the most.",
];

const loadNotes = () => (existsSync(NOTES_FILE) ? JSON.parse(readFileSync(NOTES_FILE, "utf8")) : []);
const text = (t) => ({ content: [{ type: "text", text: t }] });

const server = new McpServer({ name: "pocket-toolkit-ts", version: "1.0.0" });

server.registerTool(
  "roll_dice",
  {
    title: "Roll dice",
    description: "Roll dice using tabletop notation, e.g. '1d20', '4d6', '2d8+3'.",
    inputSchema: { notation: z.string().default("1d20").describe("Dice notation like 2d6+1") },
  },
  async ({ notation }) => {
    const m = /^\s*(\d*)d(\d+)\s*([+-]\s*\d+)?\s*$/i.exec(notation);
    if (!m) return text(`Couldn't parse '${notation}'. Try something like '2d6+1'.`);
    const count = Number(m[1] || 1);
    const sides = Number(m[2]);
    const mod = Number((m[3] || "0").replace(/\s/g, ""));
    if (count < 1 || count > 100 || sides < 2 || sides > 1000) {
      return text("Keep it between 1-100 dice with 2-1000 sides, adventurer.");
    }
    const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
    const total = rolls.reduce((a, b) => a + b, 0) + mod;
    const modText = mod ? ` ${mod > 0 ? "+" : "-"} ${Math.abs(mod)}` : "";
    return text(`🎲 ${notation}: [${rolls.join(", ")}]${modText} = **${total}**`);
  },
);

server.registerTool(
  "random_fortune",
  { title: "Random fortune", description: "Return a random fortune-cookie message. Great for morale." },
  async () => text(`🥠 ${FORTUNES[Math.floor(Math.random() * FORTUNES.length)]}`),
);

server.registerTool(
  "save_note",
  {
    title: "Save note",
    description: "Save a short note to the local notes file, with an optional tag.",
    inputSchema: { text: z.string(), tag: z.string().default("general") },
  },
  async ({ text: noteText, tag }) => {
    const notes = loadNotes();
    notes.push({ text: noteText, tag, created: new Date().toISOString().slice(0, 19) });
    writeFileSync(NOTES_FILE, JSON.stringify(notes, null, 2));
    return text(`📝 Saved note #${notes.length} with tag '${tag}'.`);
  },
);

server.registerTool(
  "list_notes",
  {
    title: "List notes",
    description: "List saved notes. Pass a tag to filter, or leave empty for all notes.",
    inputSchema: { tag: z.string().optional() },
  },
  async ({ tag }) => {
    const notes = loadNotes().filter((n) => !tag || n.tag === tag);
    if (!notes.length) return text("No notes yet. Ask me to save one!");
    return text(notes.map((n) => `- [${n.tag}] ${n.text} (${n.created})`).join("\n"));
  },
);

server.registerResource(
  "all-notes",
  "notes://all",
  { title: "All notes", description: "All saved notes as raw JSON.", mimeType: "application/json" },
  async (uri) => ({ contents: [{ uri: uri.href, text: JSON.stringify(loadNotes(), null, 2) }] }),
);

server.registerPrompt(
  "daily_standup",
  {
    title: "Daily standup",
    description: "Turn your notes into an upbeat standup update.",
    argsSchema: { focus: z.string().optional() },
  },
  ({ focus }) => ({
    messages: [
      {
        role: "user",
        content: {
          type: "text",
          text: `Read my notes with list_notes, then write a short, upbeat standup update about ${
            focus || "my projects"
          }: what I did, what I'm doing next, and any blockers.`,
        },
      },
    ],
  }),
);

await server.connect(new StdioServerTransport());
