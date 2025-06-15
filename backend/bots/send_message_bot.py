from backend.services.send_message_service import SendMessageService
from sqlalchemy.orm import Session
from uuid import UUID

class SendMessageBot:
    def __init__(self, session: Session, user_id: UUID):
        send_message_service = SendMessageService(session)
        
        self.services = {
            "send_first_message": lambda: send_message_service.send_first_message(user_id=user_id)
        } 
    
    def run(self, service: str):
        self.services[service]()