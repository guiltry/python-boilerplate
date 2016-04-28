from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Pair(Base):
    __tablename__ = 'pairs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
