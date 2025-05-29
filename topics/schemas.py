from pydantic import BaseModel


class TopicBaseSchema(BaseModel):
    title: str


class TopicCreate(TopicBaseSchema):
    pass


class TopicUpdate(TopicBaseSchema):
    pass


class TopicDelete(TopicBaseSchema):
    pass
