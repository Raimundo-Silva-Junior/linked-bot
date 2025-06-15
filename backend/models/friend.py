from sqlalchemy import Column, String, UUID, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.models.base import BaseModel

class Friend(BaseModel):
    __tablename__ = "friends"
    
    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    first_message_sent = Column(Boolean)
    
    user_id = Column(UUID, ForeignKey('users.id', index=True))
    user = relationship('User', backref='friends')