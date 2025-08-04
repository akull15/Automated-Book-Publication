# 📚 Automated Book Publication Workflow 🚀

A fully agentic AI-powered system that:
- Scrapes book chapters from websites 📖
- Rewrites them using generative AI ✍️
- Refines them through AI + human feedback loops 🧠
- Tracks versions using ChromaDB 🔄
- Offers voice agent interaction 🎤

> 💡 Built during an internship evaluation for Soft-Nerve  
> 👨‍💻 Developed using OpenAI/Gemini, FastAPI, ChromaDB, and RL-based scoring

---

## 🌟 Features

✅ **Web Scraping & Screenshot**  
→ Extracts content from book sites and saves high-res screenshots using `Playwright`.

✅ **AI-Powered Chapter Spinning**  
→ Uses GPT-4 or Gemini Pro to rewrite chapters in a modern, engaging tone.

✅ **AI Reviewer with RL-Scoring**  
→ Reviews rewritten text for clarity, tone, and grammar with reward model via sentence similarity.

✅ **Human-in-the-Loop Review**  
→ Manual iterations supported with version control via ChromaDB and semantic search.

✅ **Voice Agent Interface**  
→ Accepts and returns speech using `pyttsx3` and `speech_recognition`.

✅ **FastAPI-Powered Backend**  
→ Run locally or deploy via REST API with `/spin/` endpoint.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| FastAPI | API backend |
| Playwright | Web scraping + screenshots |
| ChromaDB | Content versioning & semantic search |
| OpenAI/Gemini | Generative AI (writer & reviewer) |
| Sentence Transformers | Reward scoring (RL-style) |
| pyttsx3 + speech_recognition | Voice interface |
| GitHub | Version control |

---

## 🧪 Usage

### ▶️ Run ChromaDB

```bash
chromadb run --path ./chromadb
