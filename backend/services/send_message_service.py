from backend.automations.send_message_automation import SendMessageAutomation
from backend.dtos.friend_dto import FriendDTO
from backend.utils.driver import driver

from playwright.async_api import Page


class SendMessageService:
    
    
    @driver
    async def send_first_message(self, page: Page, friends: list[FriendDTO], message: str) -> None:
        
        send_message_automation = SendMessageAutomation(page, "/mynetwork/invite-connect/connections/")
        await send_message_automation.enter_page()
        
        for friend in friends:
            if not friend.first_message_sent:
                await send_message_automation.find_friend(friend.name)
                await send_message_automation.send_message(message)        
