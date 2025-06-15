import asyncio
from playwright.async_api import Page

async def check_page(page: Page, current_url: str, timeout: int):
    interval = 0
    while current_url == page.url:
        asyncio.sleep(1)
        interval += 1
        if interval == timeout:
            raise Exception("Timeout")
    
    return "/feed" in page.url