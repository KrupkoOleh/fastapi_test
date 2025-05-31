from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from topics import schemas, crud

router = APIRouter()


@router.get("/topics",
            tags=["topics"],
            summary='Отримати усі теми',
            response_model=list[schemas.TopicBaseSchema])
async def get_topics(db: AsyncSession = Depends(get_db)):
    return await crud.get_topic_list(db=db)


@router.get("/topics/{topic_id}",
            tags=["topics"],
            summary='Отримати тему за ID',
            response_model=schemas.TopicBaseSchema)
async def get_topic(topic_id: int,
                    db: AsyncSession = Depends(get_db)):
    return await crud.get_topic_by_id(db=db, topic_id=topic_id)


@router.post("/topics",
             tags=["topics"],
             summary='Створити тему',
             response_model=schemas.TopicCreate)
async def create_topic(topic: schemas.TopicCreate,
                       db: AsyncSession = Depends(get_db),):
    return await crud.create_topic(db=db, topic_data=topic)


@router.put("/topics/{topic_id}",
            tags=["topics"],
            summary='Оновити тему за ID',
            response_model=schemas.TopicUpdate)
async def update_topic(topic: schemas.TopicUpdate,
                       topic_id: int,
                       db: AsyncSession = Depends(get_db)):
    return await crud.update_topic(db=db, topic_id=topic_id, topic_data=topic)


@router.delete("/topics/{topic_id}",
               tags=["topics"],
               summary='Видалити тему за ID',
               response_model=schemas.TopicDelete)
async def delete_topic(topic_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_topic(topic_id=topic_id, db=db)
