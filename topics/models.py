from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))

    post = relationship("Post", back_populates="topics")
