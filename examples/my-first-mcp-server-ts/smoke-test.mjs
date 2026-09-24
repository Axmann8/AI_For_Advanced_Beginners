/**
 * Smoke test: launch server.mjs, list its tools, call a couple.   npm test
 */
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const client = new Client({ name: "smoke-test", version: "1.0.0" });
await client.connect(new StdioClientTransport({ command: process.execPath, args: ["server.mjs"] }));

const { tools } = await client.listTools();
console.log("Tools:", tools.map((t) => t.name).join(", "));

for (const [name, args] of [["roll_dice", { notation: "3d6+2" }], ["random_fortune", {}]]) {
  const result = await client.callTool({ name, arguments: args });
  console.log(`${name} ->`, result.content[0].text);
}

const prompt = await client.getPrompt({ name: "daily_standup", arguments: { focus: "MCP" } });
console.log("prompt ->", prompt.messages[0].content.text.slice(0, 50) + "…");

await client.close();
