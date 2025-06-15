from sqlalchemy import Column, UUID, ForeignKey
from backend.models.base import Base

class MessageFriend(Base):
    __tablename__ = "message_friends"
    
    message_id = Column(UUID, ForeignKey("messages.id"), primary_key=True)
    friend_id = Column(UUID, ForeignKey("friends.id"), primary_key=True)
    