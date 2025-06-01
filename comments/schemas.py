from datetime import datetime

from pydantic import BaseModel, Field


class CommentBaseSchema(BaseModel):
    author: str
    text: str
    rating: int = Field(ge=0, le=5)

    class Config:
        from_attributes = True


class CommentGet(CommentBaseSchema):
    created_at: datetime
    updated_at: datetime


class CommentCreate(CommentBaseSchema):
    pass


class CommentUpdate(CommentBaseSchema):
    pass


class CommentDelete(CommentBaseSchema):
    pass
