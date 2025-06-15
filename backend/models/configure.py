from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Configure(Base):
    __tablename__ = "configures"
    
    id = Column(UUID, primary_key=True)
    headless = Column(String)
    
    user_id = Column(UUID, ForeignKey('users.id'), unique=True)
    user = relationship('User', back_populates='configure')