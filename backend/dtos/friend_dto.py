from pydantic import BaseModel
from uuid import uuid4, UUID

class FriendDto(BaseModel):
    
    id: UUID
    name: str
    first_message_sent: bool