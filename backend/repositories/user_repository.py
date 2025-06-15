from sqlalchemy import text
from sqlalchemy.orm import Session


class UserRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_user(self, user_id: str):
        query = text("SELECT * FROM users WHERE id = :user_id")
        return self.ession.execute(query, {"user_id": user_id})
    