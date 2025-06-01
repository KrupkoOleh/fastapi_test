from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from mixins import TimestampMixin


class Comment(Base, TimestampMixin):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(100), nullable=False)
    text = Column(String(511), nullable=True)
    rating = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"))

    post = relationship("Post", back_populates="comments")
