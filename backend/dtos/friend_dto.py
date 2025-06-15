from pydantic import BaseModel
from uuid import UUID
from backend.dtos.message_dto import MessageDTO

class FriendDTO(BaseModel):
    
    id: UUID
    name: str
    messages: list[MessageDTO]
    
    @property
    def first_message_sent(self) -> bool:
        return bool(list(filter(lambda message: message.level == 1, self.messages)))
    
    class Config:
        arbitrary_types_allowed = True