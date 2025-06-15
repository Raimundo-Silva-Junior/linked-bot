from sqlalchemy import text
from sqlalchemy.orm import Session


class FriendRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_friends(self, user_id: str):
        query = text("SELECT * FROM friends WHERE user_id = :user_id")
        return self.ession.execute(query, {"user_id": user_id})