from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.async_paginator import paginate
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from topics import schemas, crud

router = APIRouter()


@router.get("/topics",
            tags=["topics"],
            summary='Отримати усі теми',
            response_model=Page[schemas.TopicBaseSchema])
async def get_topics(db: AsyncSession = Depends(get_db),
                     sort_by: str = Query("title",
                                          description="Поле для сортування"),
                     order: str = Query("desc",
                                        description="Порядок сортування: "
                                                    "asc або desc")
                     ) -> Page[schemas.TopicBaseSchema]:
    try:
        return await paginate(await crud.get_topic_list(db=db,
                                                        sort_by=sort_by,
                                                        order=order))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/topics/{topic_id}",
            tags=["topics"],
            summary='Отримати тему за ID',
            response_model=schemas.TopicBaseSchema)
async def get_topic(topic_id: int,
                    db: AsyncSession = Depends(get_db)):
    try:
        return await crud.get_topic_by_id(db=db, topic_id=topic_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/topics",
             tags=["topics"],
             summary='Створити тему',
             response_model=schemas.TopicCreate)
async def create_topic(topic: schemas.TopicCreate,
                       db: AsyncSession = Depends(get_db), ):
    try:
        return await crud.create_topic(db=db, topic_data=topic)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/topics/{topic_id}",
            tags=["topics"],
            summary='Оновити тему за ID',
            response_model=schemas.TopicUpdate)
async def update_topic(topic: schemas.TopicUpdate,
                       topic_id: int,
                       db: AsyncSession = Depends(get_db)):
    try:
        return await crud.update_topic(db=db,
                                       topic_id=topic_id,
                                       topic_data=topic)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/topics/{topic_id}",
               tags=["topics"],
               summary='Видалити тему за ID',
               response_model=schemas.TopicDelete)
async def delete_topic(topic_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await crud.delete_topic(topic_id=topic_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
