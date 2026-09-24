# 🏠 AI Home Lab in One Command

Your own **private ChatGPT-style assistant** plus an **automation engine**, running entirely on your machine:

| Service | What it is | URL |
|---|---|---|
| 🦙 **Ollama** | Runs open models locally (Gemma, Llama, Qwen, Mistral…) | http://localhost:11434 |
| 💬 **Open WebUI** | A beautiful chat UI with RAG, tools, multi-user support, and model switching | http://localhost:3000 |
| ⚙️ **n8n** | Workflow automation with AI Agent nodes | http://localhost:5678 |

## Prereqs
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Mac/Windows) or Docker Engine (Linux)
- 16 GB RAM recommended (8 GB works with small models)
- ~10 GB free disk for images and a model or two

## Start it 🚀

```bash
cd examples/homelab
docker compose up -d                              # first run downloads the images (a few minutes)
docker compose exec ollama ollama pull gemma3     # grab a model (or llama3.2, qwen3, mistral…)
```

1. Open **http://localhost:3000** → create the admin account → pick your model → chat! 🎉
2. Open **http://localhost:5678** → create the n8n owner account.

## Wire n8n to your local models 🔌
In n8n, add an **Ollama Chat Model** credential with base URL **`http://ollama:11434`** (containers reach
each other by service name). Now any AI Agent or LLM Chain node can use your local model for free, private,
unlimited automations.

## Cool things to try 🎮
- **Open WebUI → Documents:** upload PDFs and chat with them (built-in RAG).
- **Model arena:** Open WebUI can send one prompt to two models side by side.
- **n8n local agent:** import our [n8n workflows](../n8n-workflows/) and swap the Claude node for Ollama.
- **Mix local and cloud:** add an Anthropic or OpenAI API key in Open WebUI to switch between private and frontier models in one UI.

## Everyday commands
```bash
docker compose ps                  # what's running
docker compose logs -f open-webui  # watch logs
docker compose pull && docker compose up -d   # update everything
docker compose down                # stop (your data stays in volumes)
```

## GPU acceleration ⚡
- **NVIDIA (Linux/Windows WSL):** install the NVIDIA Container Toolkit and uncomment the `deploy:` block in `docker-compose.yml`.
- **Apple Silicon Macs:** Docker can't use the Mac GPU. For max speed, install **Ollama natively** (ollama.com), remove the `ollama`
  service, and set `OLLAMA_BASE_URL=http://host.docker.internal:11434` for Open WebUI (and use that URL in n8n).

## Safety notes 🔒
- These ports are bound for local use. **Don't expose them to the internet** without authentication and HTTPS.
  For remote access, use **Tailscale** (private network) instead of port-forwarding.
- Back up the Docker volumes (`ollama`, `open-webui`, `n8n_data`) if you care about the data.

Full chapter: [Manual Ch. 27: Home Lab](../../manual/part-7-local-ai/27-home-lab.md).
