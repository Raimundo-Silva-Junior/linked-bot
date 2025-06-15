from backend.automations.send_message_automation import SendMessageAutomation
from backend.repositories.friend_repository import FriendRepository
from backend.repositories.message_repository import MessageRepository
from backend.services.base_service import BaseService
from backend.models.message_friend import MessageFriend  
from backend.utils.driver import driver
from uuid import UUID
from playwright.async_api import Page


class SendMessageService(BaseService):
    
    
    @driver
    async def send_first_message(self, page: Page, user_id: UUID) -> None:
        
        friends = FriendRepository(self.session).find_friends_above_first_contanct(user_id)
        message = MessageRepository(self.session).find_message_by_level(user_id, 1)
        
        send_message_automation  = SendMessageAutomation(page, "/mynetwork/invite-connect/connections/")
        await send_message_automation.enter_page()
        
        for friend in friends:
            await send_message_automation.find_friend(friend.name)
            await send_message_automation.send_message(message.message)
            self.session.add(MessageFriend(message_id=message.id, friend_id=friend.id))
            
                       
