from sqlalchemy import text
from sqlalchemy.orm import Session
from backend.dtos.user_dto import UserDTO


class UserRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_user(self, user_id: str) -> UserDTO:
        query = text("SELECT * FROM users WHERE id = :user_id")
        user = self.session.execute(query, {"user_id": user_id}).mappings().first()
        return UserDTO.model_validate_json(user)
    