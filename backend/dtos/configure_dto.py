from uuid import UUID
from pydantic import BaseModel

class ConfigureDTO(BaseModel):
    
    id: UUID
    headless: bool