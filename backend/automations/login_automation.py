from backend.automations.base_automation import BaseAutomation
from backend.utils.check_page import check_page
from playwright.async_api import Cookie

class LoginAutomation(BaseAutomation):

    async def enter_credentials(self, name: str, password: str) -> None:
        
        await self.page.locator("#username").fill(name)
        await self.page.locator("#password").fill(password)
        await self.page.locator("//button[@type='submit]", has_text="Entrar").click()
    
    async def is_successfull(self, current_url: str, timeout: int) -> bool:
        return await check_page(self.page, current_url, timeout)
        
    async def get_cookies(self) -> list[Cookie]:
        cookies = await self.page.context.cookies()
        return cookies