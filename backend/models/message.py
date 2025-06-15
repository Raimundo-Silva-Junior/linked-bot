from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(UUID, primary_key=True, index=True)
    message = Column(String)
    level = Column(Integer)
    
    friends = relationship("Friend", secondary="message_friends", back_populates="messages")

    