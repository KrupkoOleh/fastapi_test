from pydantic import BaseModel


class TopicBaseSchema(BaseModel):
    title: str

    class Config:
        from_attributes = True


class TopicCreate(TopicBaseSchema):
    pass


class TopicUpdate(TopicBaseSchema):
    pass


class TopicDelete(TopicBaseSchema):
    pass
