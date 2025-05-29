from sqlalchemy import Column, Integer, String

from database import Base


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
