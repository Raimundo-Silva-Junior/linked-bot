from sqlalchemy import text
from sqlalchemy.orm import Session


class ConfigureRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_configure(self, user_id: str):
        query = text("SELECT * FROM configures WHERE user_id = :user_id")
        return self.ession.execute(query, {"user_id": user_id})