# 29 · Image Generation Deep Dive 🎨🖼️

AI image tools went from "weird hands" to **professional-grade** in a few short years. This chapter
goes past "type a prompt, get a picture": how to direct images like an art director, keep characters
consistent, edit precisely, and build image pipelines.

---

## Choosing your tool (by job)

| Job | Great picks |
|---|---|
| 🎭 Artistic, gorgeous aesthetics | **Midjourney** |
| 🗣️ Following complex instructions, conversational edits | **ChatGPT images**, **Gemini image models ("Nano Banana")** |
| 🔤 Text and typography in images (posters, logos) | **Ideogram**, ChatGPT, Gemini |
| 📐 Vector/SVG, brand sets, icons | **Recraft** |
| 🔓 Open and local, full control | **Flux** (Black Forest Labs), **Stable Diffusion** family via **ComfyUI** |
| 🖌️ Pro editing inside design tools | **Adobe Firefly** (Photoshop), **Canva AI** |
| 🧑 Consistent characters and products | Gemini/ChatGPT with reference images, Midjourney character/style references, Flux LoRAs |

## The anatomy of a great image prompt 🧬

Think like a photographer or art director. Cover these layers (skip any you don't care about):

| Layer | Examples |
|---|---|
| **Subject** | "a red fox wearing a tiny knitted scarf" |
| **Action/pose** | "curled up asleep on a stack of old books" |
| **Setting** | "in a cozy attic library, rain on the skylight" |
| **Style/medium** | "watercolor illustration" / "35mm film photo" / "3D Pixar-style render" / "risograph print" |
| **Lighting** | "warm lamp light, soft shadows, golden hour" |
| **Camera/composition** | "close-up, shallow depth of field, eye-level, centered" |
| **Color palette** | "muted autumn tones, pops of teal" |
| **Mood** | "peaceful, nostalgic" |
| **Text (if any)** | `the words "Reading Nook" in hand-lettered serif at the top` |
| **Format** | "square", "16:9", "vertical 9:16 phone wallpaper" |

**Example:**
> *A red fox wearing a tiny knitted scarf, curled up asleep on a stack of old books in a cozy attic library, rain on the
> skylight. Watercolor illustration, warm lamp light, muted autumn palette with teal accents. Peaceful, nostalgic. Square.*

💡 **Let AI write your prompts:** *"Turn my idea into 3 detailed image prompts in different styles: [idea]."*

## Editing: the real superpower ✂️

Modern models edit images **conversationally**:
- *"Make it nighttime."* *"Change the scarf to yellow."* *"Remove the lamp."*
- **Inpainting:** select an area and describe what goes there.
- **Outpainting / expand:** extend the canvas ("show more of the room").
- **Style transfer:** *"Redo this photo as a Studio Ghibli–style background painting."*
- **Combine images:** *"Put the product from image 1 into the scene from image 2."*

## Consistency: same character, many images 🧑‍🎨

1. **Create a reference sheet first:** *"Character sheet: front, side, and back views of [character], plain background."*
2. **Reuse the reference image** in every generation: *"Using this character, show her at the beach."*
3. **Lock the description:** keep a fixed "character bible" paragraph you paste each time.
4. **Advanced:** train a small **LoRA** (Flux/SD) on 10–20 images of a character, product, or your own style.

## Practical uses that pay off 💼

| Use | Tips |
|---|---|
| Social posts & thumbnails | Generate the background, then add text in Canva for control |
| Product mockups | Your product photo + "place on a marble counter, soft morning light" |
| Presentations | A consistent illustration style across slides |
| Logos & brand exploration | Generate 20 directions fast, then refine the winner by hand or in vector tools |
| Storyboards | Consistent characters across frames for video projects ([Ch. 30](30-video-and-audio-production.md)) |
| Personal fun | Pet portraits in Renaissance style, D&D character art, custom wallpapers 🐶👑 |

## Automating image generation ⚙️
- **APIs:** OpenAI, Google (Gemini/Imagen), Stability, Black Forest Labs, Ideogram, Recraft, plus aggregators like **Replicate** and **fal**.
- **n8n/Make/Zapier:** a blog post is published → AI writes an image prompt → the image API → upload to your CMS.
- **MCP:** image-generation MCP servers let Claude or Cursor create images mid-conversation.
- **ComfyUI workflows:** node-based pipelines you can run locally or via API for batch jobs.

## Ethics & rights (the short, practical version) ⚖️
- **Don't** create images of real people in misleading, sexual, or harmful ways, or impersonate brands.
- **Check each tool's commercial-use terms** before selling or using images in ads.
- **Label AI images** when it matters (journalism, reviews, anything people might take as real).
- Prefer tools with **content credentials** (C2PA) for transparency.

---

### 🎮 Try this
**The brand-kit challenge:** invent a tiny business (e.g. "Pixel's Plant Shop 🌿"). Generate a logo concept, a color palette,
an Instagram post, and a product mockup, all visually consistent. Use at least two different tools. Share your favorite! 🎨

---

**Next:** [30 · Video & Audio Production with AI →](30-video-and-audio-production.md)
