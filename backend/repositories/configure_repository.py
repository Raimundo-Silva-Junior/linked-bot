from sqlalchemy import text
from sqlalchemy.orm import Session
from backend.dtos.configure_dto import ConfigureDTO


class ConfigureRepository:
    
    def __init__(self, session: Session):
        self.session = session

    def find_configure(self, user_id: str) -> ConfigureDTO:
        query = text("SELECT * FROM configures WHERE user_id = :user_id")
        configure = self.session.execute(query, {"user_id": user_id}).mappings().first()
        return ConfigureDTO.model_validate_json(configure)