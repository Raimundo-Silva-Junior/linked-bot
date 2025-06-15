from pydantic import BaseModel
from uuid import UUID

class MessageDTO(BaseModel):
    
    id: UUID
    message: str
    level: int