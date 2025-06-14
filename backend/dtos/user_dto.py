from pydantic import BaseModel

class UserDto(BaseModel):
    email: str
    password: str
    cookies: str