from fastapi import HTTPException
from sqlalchemy import select, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from topics import models, schemas


async def get_topic_list(db: AsyncSession,
                         sort_by: str = "title",
                         order: str = "desc"):
    if not hasattr(models.Topic, sort_by):
        sort_by = "title"

    sort_column = getattr(models.Topic, sort_by)
    order_func = asc if order == "asc" else desc
    queryset = select(models.Topic).order_by(order_func(sort_column))
    topic_list = await db.execute(queryset)
    return topic_list.scalars().all()


async def get_topic_by_id(db: AsyncSession, topic_id: int):
    result = await db.execute(select(models.Topic).filter(
        models.Topic.id == topic_id)
    )
    post = result.scalars().first()
    return post


async def create_topic(db: AsyncSession, topic_data: schemas.TopicCreate):
    topic = models.Topic(
        title=topic_data.title
    )
    db.add(topic)
    await db.commit()
    await db.refresh(topic)
    return topic


async def update_topic(db: AsyncSession,
                       topic_id: int,
                       topic_data: schemas.TopicUpdate):
    topic = await db.get(models.Topic, topic_id)

    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    topic.title = topic_data.title

    await db.commit()
    await db.refresh(topic)
    return topic


async def delete_topic(db: AsyncSession, topic_id: int):
    topic = await db.get(models.Topic, topic_id)
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    await db.delete(topic)
    await db.commit()
    return topic
