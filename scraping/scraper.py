from playwright.sync_api import sync_playwright
import os

def fetch_chapter(url, screenshot_name="chapter1.png"):
    os.makedirs("screenshots", exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_timeout(2000)

        content = page.inner_text("body")
        screenshot_path = f"screenshots/{screenshot_name}"
        page.screenshot(path=screenshot_path, full_page=True)

        browser.close()
        return content, screenshot_path