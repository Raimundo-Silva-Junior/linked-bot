from uuid import UUID
from pydantic import BaseModel

class ConfigureDto(BaseModel):
    
    id: UUID
    headless: bool