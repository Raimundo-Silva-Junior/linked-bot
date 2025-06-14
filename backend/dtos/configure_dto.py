from pydantic import BaseModel

class ConfigureDto(BaseModel):
    url: str
    headless: bool