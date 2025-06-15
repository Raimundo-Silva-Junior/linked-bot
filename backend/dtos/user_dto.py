from uuid import UUID
from pydantic import BaseModel

class UserDto(BaseModel):
    
    id: UUID
    username: str
    password: str
    cookies: str