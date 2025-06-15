from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

BASE_URL = 'https://www.linkedin.com'

SESSION = sessionmaker(
    bind=Engine(
    ),
    autocommit=True
)