from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from backend.models.base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    cookies = Column(String)
    
    configures = relationship('Configure', backref='user')
    friends = relationship('Friend', backref='user')