from playwright.async_api import Page
from backend.utils.goto import goto


class SendMessageAutomation:
    
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url
    
    async def enter_page(self):
        await goto(self.page, self.url)
    
    async def find_friend(self, name: str):
        self.page.locator('text="name"')
        
    async def send_message(self, message: str):
        self.page.locator('text="name"')
