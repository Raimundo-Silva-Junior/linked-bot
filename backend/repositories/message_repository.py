from sqlalchemy import text
from sqlalchemy.orm import Session
from backend.dtos.message_dto import MessageDTO
from uuid import UUID


class MessageRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_messages(self, user_id: UUID) -> list[MessageDTO]:
        query = text("SELECT * FROM message WHERE user_id = :user_id")
        messages =  self.session.execute(query, {"user_id": user_id}).mappings().all()
        return [MessageDTO.model_validate_json(message) for message in messages]
    
    def find_message_by_level(self, user_id: UUID, level: int) -> MessageDTO:
        query = text("SELECT * FROM message WHERE user_id = :user_id AND level = :level")
        messages =  self.session.execute(query, {"user_id": user_id, "level": level}).mappings().first()
        return [MessageDTO.model_validate_json(message) for message in messages]