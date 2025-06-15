from sqlalchemy import text
from sqlalchemy.orm import Session
from uuid import UUID
from backend.dtos.friend_dto import FriendDTO

class FriendRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_friends(self, user_id: UUID) -> list[FriendDTO]:
        query = text("""SELECT * FROM friends WHERE user_id = :user_id""")
        friends = self.session.execute(query, {"user_id": user_id}).mappings().all()
        return [FriendDTO.model_validate_json(friend) for friend in friends]
    
    def find_friends_above_first_contanct(self, user_id: UUID) -> list[FriendDTO]:
        query = text(
            """
            SELECT f.*, m.*
            FROM friends f
            INNER JOIN message m ON f.id = m.friend_id
            WHERE f.user_id = :user_id AND m.level > 1
            """
        )
        friends = self.session.execute(query, {"user_id": user_id}).mappings().all()
        return [FriendDTO.model_validate_json(friend) for friend in friends]
    