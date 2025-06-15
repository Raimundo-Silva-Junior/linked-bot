from playwright.async_api import async_playwright
from typing import Callable
from functools import wraps


def driver(func: Callable) -> Callable:
    
    @wraps(func)
    async def wrapper(*args, **kwargs) -> object:
        
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            return func(page, *args, **kwargs)

    return wrapper