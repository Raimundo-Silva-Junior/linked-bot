from backend.automations.send_message_automation import SendMessageAutomation
from backend.models.friend import Friend


class SendMessageService:
    
    def send_first_message(self, friends: list[Friend], message: str):
        
        for friend in friends:
            if not friend.first_message_sent:
                send_message_automation = SendMessageAutomation()
                send_message_automation.enter_page()
                
                send_message_automation.find_friend(friend.name)
                send_message_automation.send_message(message)
                friend.first_message_sent = True
                friend.save()
                
        
