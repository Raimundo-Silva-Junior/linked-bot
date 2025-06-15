from sqlalchemy import Column, String, UUID, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Message(Base):
    __tablename__ = "messages"
    
    id = Column(UUID, primary_key=True)
    message = Column(String)
    level = Column(Integer)
    date = Column(DateTime, default=datetime.now)
    
    friends = relationship("Friend", secondary="message_friends", back_populates="messages")

    