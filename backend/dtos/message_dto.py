from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class MessageDTO(BaseModel):
    
    id: UUID
    message: str
    level: int
    data: datetime