from sqlalchemy import Column, String, UUID, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Friend(Base):
    __tablename__ = "friends"
    
    id = Column(UUID, primary_key=True)
    name = Column(String)
    friendship_date = Column(DateTime)
    
    user_id = Column(UUID, ForeignKey('users.id'))
    user = relationship('User', back_populates='friends')
    messages = relationship("Message", secondary="message_friends", back_populates="friends")
