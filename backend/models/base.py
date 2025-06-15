from sqlalchemy.ext.declarative import declarative_base
from backend.config import SESSION

Base = declarative_base() 

class BaseModel(Base):
    __abstract__ = True
    
    def save(self):
        with SESSION.begin() as session:
            session.add(self)
    
    def delete(self):
        with SESSION.begin() as session:
            session.delete(self)
    
    @classmethod    
    def update(cls, **kwargs):
        with SESSION.begin() as session:
            session.query(cls).update(values=kwargs)

            
    