from sqlalchemy import Column, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import BaseModel

class Configure(BaseModel):
    __tablename__ = "configures"
    
    id = Column(UUID, primary_key=True, index=True)
    headless = Column(String)
    
    user_id = Column(UUID, ForeignKey('users.id', index=True))
    user = relationship('User', backref='configures')