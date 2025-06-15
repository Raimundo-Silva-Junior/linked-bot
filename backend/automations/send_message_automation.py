from backend.automations.base_automation import BaseAutomation


class SendMessageAutomation(BaseAutomation):
    
    async def find_friend(self, name: str) -> None:
        await self.page.locator("#mn-connections-search-input").fill(name)
        
    async def send_message(self, message: str):
        await self.page.locator("//button[@class='artdeco-pill__text']", has_text="Enviar").click()
