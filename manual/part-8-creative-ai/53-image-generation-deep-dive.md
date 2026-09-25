# 53 · Image Generation Deep Dive: Direct Images Like an Art Director 🎨🖼️

> ⏱️ 8 min read · 🎯 Everyone (beginner → pro techniques) · 🧰 Needs: one image tool (ChatGPT, Gemini, Midjourney, Ideogram, or ComfyUI locally)

**AI image tools went from "weird hands" to professional-grade in a few short years.** This chapter goes way past "type a
prompt, get a picture": how to pick the right tool for the job, write prompts like an art director, edit precisely, keep
characters consistent across dozens of images, run open models locally, and automate image pipelines. Plus a pile of fun
projects and the ethics you need to know. 🖌️✨

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Image AI is a magic painter. You describe a picture ("a sleepy fox in a scarf on a pile of books, painted in watercolors")
and it paints it in seconds. The more clearly you describe what you see in your head (the thing, the place, the colors, the
lighting, the style) the closer it gets. And you can keep saying "now make it nighttime" or "give the fox a yellow scarf"
until it's perfect.

</details>

<!-- in-this-chapter -->

## 🧭 Choosing your tool (by job)

<details class="eli5">
<summary>🧸 ELI5</summary>

Different magic painters are best at different things: some paint beautiful art, some are great at words on pictures, some are
best at fixing photos.

</details>

| Job | Great picks |
|---|---|
| 🗣️ Following complex instructions, conversational edits | **ChatGPT (GPT Image)**, **Gemini (Nano Banana)** |
| 🎭 Artistic, gorgeous aesthetics, concept art | **Midjourney** |
| 📷 Photoreal product and marketing shots | **FLUX**, GPT Image, Gemini |
| 🔤 Text and typography (posters, logos, signs) | **Ideogram**, GPT Image, Gemini |
| 📐 Vector/SVG, icons, brand sets | **Recraft** |
| 🔓 Open and local, full control | **FLUX** open models, the **Stable Diffusion** family, **Qwen-Image** and friends via **ComfyUI** |
| 🖌️ Pro editing inside design tools | **Adobe Firefly** (Photoshop), **Canva AI** |
| 🧑 Consistent characters and products | Gemini or GPT Image with reference images, Midjourney references, LoRAs |

> [!TIP]
> **💡 Check the leaderboards**
> Rankings shift every few months. Arena-style leaderboards (where people vote blind between images) are a great way to see
> who's leading for photorealism, editing or text *right now*.

## 🧬 The anatomy of a great image prompt

<details class="eli5">
<summary>🧸 ELI5</summary>

A great picture description has layers: what's in it, what it's doing, where it is, what style, what lighting, and what
feeling. Fill in the ones you care about.

</details>

Think like a photographer or art director. Cover these layers (skip any you don't care about):

| Layer | Examples |
|---|---|
| **Subject** | "a red fox wearing a tiny knitted scarf" |
| **Action / pose** | "curled up asleep on a stack of old books" |
| **Setting** | "in a cozy attic library, rain on the skylight" |
| **Style / medium** | "watercolor illustration," "35mm film photo," "3D animated-film render," "risograph print" |
| **Lighting** | "warm lamp light, soft shadows, golden hour" |
| **Camera / composition** | "close-up, shallow depth of field, eye-level, centered" |
| **Color palette** | "muted autumn tones, pops of teal" |
| **Mood** | "peaceful, nostalgic" |
| **Text (if any)** | `the words "Reading Nook" in hand-lettered serif at the top` |
| **Format** | "square," "16:9," "vertical 9:16 phone wallpaper" |

**Example:**

> *A red fox wearing a tiny knitted scarf, curled up asleep on a stack of old books in a cozy attic library, rain on the
> skylight. Watercolor illustration, warm lamp light, muted autumn palette with teal accents. Peaceful, nostalgic. Square.*

> [!TIP]
> **🪄 Let AI write your prompts**
> *"Turn my idea into 3 detailed image prompts in different styles: [idea]."* Claude is an excellent prompt writer for image
> models, especially for keeping a series consistent.

## 🎨 Style vocabulary cheat sheet

<details class="eli5">
<summary>🧸 ELI5</summary>

Here are magic words that change the look of your picture: art styles, camera words and lighting words.

</details>

| Styles | Camera & lens | Lighting | Texture & finish |
|---|---|---|---|
| Watercolor | Macro close-up | Golden hour | Film grain |
| Oil painting | Wide-angle | Soft window light | Paper texture |
| Studio Ghibli-inspired | Aerial / drone shot | Neon glow | Glossy 3D render |
| Pixel art | Fisheye | Candlelight | Matte clay (claymation) |
| Risograph print | Tilt-shift miniature | Studio softbox | Cross-stitch |
| Isometric illustration | Portrait 85mm, f/1.8 | Rim light / backlight | Paper cut-out |
| Art nouveau poster | Low angle, heroic | Moody chiaroscuro | Stained glass |
| Vintage travel poster | Polaroid snapshot | Bioluminescent | Knitted wool 🧶 |

**Tip:** name an *era or medium* ("1970s sci-fi paperback cover") rather than a living artist. You get the vibe without
copying a real person's work.

## ✂️ Editing: the real superpower

<details class="eli5">
<summary>🧸 ELI5</summary>

You can change pictures just by asking: "make it nighttime," "remove the lamp," "put my dog in this scene." No drawing skills
needed.

</details>

Modern models edit images **conversationally**:

| Edit | Example |
|---|---|
| **Change details** | *"Make it nighttime."* *"Change the scarf to yellow."* *"Remove the lamp."* |
| **Inpainting** | Select an area and describe what goes there |
| **Outpainting / expand** | Extend the canvas: *"Show more of the room."* |
| **Style transfer** | *"Redo this photo as a watercolor storybook illustration."* |
| **Combine images** | *"Put the product from image 1 into the scene from image 2."* |
| **Relight** | *"Same scene, but lit by sunset through the window."* |
| **Restore** | *"Repair and colorize this old family photo, keeping faces natural."* 👵📷 |
| **Change angle** | *"Show this room from the doorway instead."* |

## 🧑‍🎨 Consistency: same character, many images

<details class="eli5">
<summary>🧸 ELI5</summary>

To draw the same character in lots of pictures, first make a "character sheet" picture, then show it to the AI every time
you ask for a new scene.

</details>

1. **Create a reference sheet first:** *"Character sheet: front, side and back views of [character], plain background."*
2. **Reuse the reference image** in every generation: *"Using this character, show her at the beach."*
3. **Lock the description:** keep a fixed "character bible" paragraph you paste each time.
4. **Keep a style reference** too: one image that defines the look of the whole series.
5. **Advanced:** train a small **LoRA** on 10–20 images of a character, product or your own style ([Fine-Tuning](../part-7-local-ai/51-fine-tuning-for-normal-people.md#-fine-tuning-beyond-text)).

## 🖥️ Running image models locally

<details class="eli5">
<summary>🧸 ELI5</summary>

You can run picture-making AI on your own computer if it has a good graphics card. Then you can make as many pictures as you
like, for free and privately.

</details>

| Tool | Style | Best for |
|---|---|---|
| **ComfyUI** | Node graph: connect boxes into a pipeline | Maximum control, shareable workflows |
| **Forge / Automatic1111-style UIs** | Classic web UI with tabs and sliders | Getting started quickly |
| **InvokeAI** | Polished canvas-based app | Artists who want layers and inpainting |
| **Draw Things, DiffusionBee** | Mac apps | Easy local generation on Apple Silicon |

**Hardware:** an NVIDIA GPU with 8 GB+ VRAM runs many models, and 16–24 GB runs the big ones comfortably
([Hardware for Local AI](../part-7-local-ai/48-hardware-for-local-ai.md)). Macs work, but slower.

**Why bother?** Unlimited generations, full privacy, custom LoRAs, ControlNet-style guidance (pose, depth, edges), and batch
pipelines.

## 💼 Practical uses that pay off

<details class="eli5">
<summary>🧸 ELI5</summary>

Picture AI isn't just for fun. It helps with social posts, presentations, product photos, logos and more.

</details>

| Use | Tips |
|---|---|
| Social posts & thumbnails | Generate the background, then add text in Canva for control |
| Product mockups | Your product photo + "on a marble counter, soft morning light" |
| Presentations | One consistent illustration style across all slides |
| Logos & brand exploration | Generate 20 directions fast, then refine the winner in a vector tool |
| Storyboards | Consistent characters across frames for video ([Video & Audio](54-video-and-audio-production.md)) |
| Real estate & interiors | *"Show this empty room furnished in Scandinavian style"* (label it as a render!) |
| Personal fun | Pet portraits in Renaissance style, D&D character art, custom wallpapers 🐶👑 |

## ⚙️ Automating image generation

<details class="eli5">
<summary>🧸 ELI5</summary>

Robots can make pictures for you automatically, like a new picture for every blog post you write.

</details>

- **APIs:** OpenAI, Google (Gemini/Imagen), Black Forest Labs, Ideogram, Recraft, Stability, plus aggregators like **Replicate**
  and **fal**.
- **n8n / Make / Zapier:** a blog post is published → Claude writes an image prompt → the image API → upload to your CMS.
- **MCP:** image-generation MCP servers let Claude or Cursor create images mid-conversation.
- **ComfyUI workflows:** run locally or via API for batch jobs ("make 50 product shots in the same style").

## ⚖️ Ethics & rights (the practical version)

<details class="eli5">
<summary>🧸 ELI5</summary>

Be fair: don't make fake pictures of real people, don't pretend AI pictures are real photos, and check the rules before selling
AI art.

</details>

| Guideline | Why |
|---|---|
| **Don't** make misleading, sexual or harmful images of real people | It hurts real people, and many places make it illegal |
| **Don't** impersonate brands or fake news photos | Misinformation spreads fast |
| **Check commercial-use terms** before selling or advertising | Rules differ by tool and plan |
| **Label AI images** when it matters | Journalism, reviews, anything people might take as real |
| **Prefer tools with content credentials** (C2PA) | Transparency about how an image was made |
| **Respect artists** | Avoid imitating living artists' signature styles for commercial work |

## 🎮 15 image projects

<details class="eli5">
<summary>🧸 ELI5</summary>

Fifteen fun picture projects to try this month.

</details>

| # | Project | # | Project |
|---|---|---|---|
| 1 | 🌿 Brand kit for an imaginary shop | 9 | 🃏 Custom playing cards for game night |
| 2 | 📚 A picture book starring your kid or pet | 10 | 🗺️ A fantasy map of your neighborhood |
| 3 | 🖼️ Restore and colorize old family photos | 11 | 🏠 "What if" room makeovers |
| 4 | 🎴 Tarot deck for your friend group | 12 | 🍰 A recipe book with dreamy food photos |
| 5 | 🐶 Pet portraits in 5 art styles | 13 | 🎟️ Posters for an imaginary film festival |
| 6 | 🧙 D&D character portraits | 14 | 📱 A month of phone wallpapers |
| 7 | 💌 Personalized greeting cards | 15 | 🎨 A style LoRA of your own sketches |
| 8 | 🏷️ Stickers and emoji for your group chat | | |

## 🎯 Key takeaways

- **Pick tools by job:** instruction-following and editing (GPT Image, Nano Banana), art (Midjourney), photoreal (FLUX),
  text (Ideogram), vectors (Recraft).
- Prompt in **layers**: subject, action, setting, style, lighting, camera, palette, mood, text, format.
- **Conversational editing** is the real superpower.
- **Reference sheets + reused references + character bibles** keep characters consistent. LoRAs go further.
- Create **ethically**: consent, labels, commercial terms, respect for artists.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. You need a poster with the exact words "Summer Fête 2026" spelled correctly. Which tools are strongest?</summary>

Tools known for **typography**: **Ideogram**, GPT Image or Gemini.

</details>

<details class="quiz">
<summary>❓ 2. How do you keep the same character looking the same across 12 illustrations?</summary>

Make a **reference sheet**, **reuse it as a reference image** each time, keep a fixed **character bible** description, and
optionally train a **LoRA**.

</details>

<details class="quiz">
<summary>❓ 3. Why name an era or medium instead of a living artist in prompts?</summary>

You get the **style you want** without copying a real person's signature work, which is kinder to artists and safer for
commercial use.

</details>

> [!TIP]
> **🎮 Try this: the brand-kit challenge**
> Invent a tiny business (e.g. "Pixel's Plant Shop 🌿"). Generate a logo concept, a color palette, an Instagram post and a
> product mockup, all visually consistent, using at least two different tools. Share your favorite! 🎨

---

**Next:** [54 · Video & Audio Production with AI →](54-video-and-audio-production.md)
