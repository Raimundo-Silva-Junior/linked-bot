from playwright.async_api import Page
from backend.utils.goto import goto
from abc import ABC


class BaseAutomation(ABC):
    
    def __init__(self, page: Page, url: str) -> None:
        self.page = page
        self.url = url
        
    async def enter_page(self) -> None:
        await goto(self.page, self.url)