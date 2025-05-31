from pydantic import Field, BaseModel

from comments.schemas import CommentBaseSchema
from topics.schemas import TopicBaseSchema


class PostBaseSchema(BaseModel):
    title: str
    content: str = Field(example='Hello World!')
    author: str

    class Config:
        from_attributes = True


class PostCreate(PostBaseSchema):
    pass


class PostUpdate(PostBaseSchema):
    pass


class PostDelete(PostBaseSchema):
    pass


class PostGetWithRelationships(PostBaseSchema):
    comments: list[CommentBaseSchema] = []
    topics: list[TopicBaseSchema] = []


class PostCreateWithRelationships(PostBaseSchema):
    comments: list[CommentBaseSchema] = []
    topics: list[TopicBaseSchema] = Field(min_items=1)


class PostUpdateWithRelationships(PostBaseSchema):
    comments: list[CommentBaseSchema] = []
    topics: list[TopicBaseSchema] = []


class PostDeleteWithRelationships(PostBaseSchema):
    comments: list[CommentBaseSchema] = []
    topics: list[TopicBaseSchema] = []
