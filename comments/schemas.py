from pydantic import BaseModel, Field


class CommentBaseSchema(BaseModel):
    author: str
    text: str
    rating: int = Field(ge=0, le=5)


class CommentCreate(CommentBaseSchema):
    pass


class CommentUpdate(CommentBaseSchema):
    pass


class CommentDelete(CommentBaseSchema):
    pass
