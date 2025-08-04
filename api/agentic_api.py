from fastapi import FastAPI
from pydantic import BaseModel

from ai_agents.writer import ai_writer
from ai_agents.reviewer import ai_reviewer
from rl.reward_model import reward_score
from scraping.scraper import fetch_chapter
from human_in_loop.versioning import save_version
from utils.voice_support import speak

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/process/")
def process_chapter(req: URLRequest):
    # 1. Scrape & Screenshot
    speak("Fetching the chapter...")
    content, screenshot_path = fetch_chapter(req.url)

    # 2. AI Writing & Reviewing
    speak("Spinning the chapter with AI...")
    spun = ai_writer(content)
    reviewed = ai_reviewer(spun)

    # 3. RL Reward Score
    score = reward_score(content, reviewed)

    # 4. Save to ChromaDB
    doc_id = req.url.replace("/", "_")
    save_version(doc_id, reviewed)

    return {
        "url": req.url,
        "output": reviewed,
        "reward_score": score,
        "screenshot_saved": screenshot_path
    }

class ChapterRequest(BaseModel):
    text: str

@app.post("/spin/")
def spin_chapter(req: ChapterRequest):
    spun = ai_writer(req.text)
    reviewed = ai_reviewer(spun)
    return {"output": reviewed}

@app.get("/search/")
def search_chapters(q: str):
    from human_in_loop.versioning import search_versions
    results = search_versions(q)
    return {"results": results}