from typing import Final
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker

BASE_URL: Final = 'https://www.linkedin.com'

SESSION: Final  = sessionmaker(
    bind=Engine(
        pool=None
    ),
    autocommit=True
)