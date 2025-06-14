from backend.automations.send_message_automation import SendMessageAutomation


class SendMessageService:
    
    def send_first_message(self):
        
        send_message_automation = SendMessageAutomation()
        send_message_automation.enter_page()
        
        send_message_automation.find_friend("name")
        send_message_automation.send_message("message")