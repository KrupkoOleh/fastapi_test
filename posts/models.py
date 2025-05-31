from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(511), nullable=False)
    author = Column(String(100), nullable=True)

    comments = relationship("Comment",
                            back_populates="post",
                            lazy="joined",
                            cascade="all, delete-orphan")
    topics = relationship("Topic",
                          back_populates="post",
                          lazy="joined")
