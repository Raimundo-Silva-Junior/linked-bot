from typing import Final
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

BASE_URL: Final = 'https://www.linkedin.com'

SESSION: Final  = sessionmaker(
    bind=Engine(
        pool=None
    ),
    autocommit=True
)