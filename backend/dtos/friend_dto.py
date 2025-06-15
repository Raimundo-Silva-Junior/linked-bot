from pydantic import BaseModel
from uuid import UUID

class FriendDTO(BaseModel):
    
    id: UUID
    name: str
    first_message_sent: bool