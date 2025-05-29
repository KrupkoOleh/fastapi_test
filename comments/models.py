from sqlalchemy import Column, Integer, String

from database import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(100), nullable=False)
    text = Column(String(511), nullable=True)
    rating = Column(Integer, nullable=False)
