from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from backend.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    cookies = Column(String)
    
    configure = relationship('Configure', back_populates='user', uselist=False)
    friends = relationship('Friend', back_populates='user')