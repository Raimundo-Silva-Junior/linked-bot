from playwright.async_api import Page
from backend.config import BASE_URL


async def goto(page: Page, url: str):
    await page.goto(BASE_URL + url)