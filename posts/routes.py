from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.async_paginator import paginate
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from posts import schemas, crud

router = APIRouter()


@router.get("/posts",
            tags=["posts"],
            summary='Отримати усі пости',
            response_model=Page[schemas.PostGetWithRelationships])
async def get_posts(db: AsyncSession = Depends(get_db),
                    sort_by: str = Query("created_at",
                                         description="Поле для сортування"),
                    order: str = Query("desc",
                                       description="Порядок сортування: "
                                                   "asc або desc")
                    ) -> Page[schemas.PostGetWithRelationships]:
    try:
        return await paginate(await crud.get_post_list(db=db,
                                                       sort_by=sort_by,
                                                       order=order))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/posts/{post_id}",
            tags=["posts"],
            summary='Отримати окремий пост з коментарями та темами '
                    'до нього за ID',
            response_model=schemas.PostGetWithRelationships)
async def get_post(post_id: int,
                   db: AsyncSession = Depends(get_db)):
    try:
        return await crud.get_post_by_id(db=db, post_id=post_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/posts",
             tags=["posts"],
             summary='Створити пост з коментарями та темами до нього',
             response_model=schemas.PostCreateWithRelationships,
             status_code=201)
async def create_posts(post: schemas.PostCreateWithRelationships,
                       db: AsyncSession = Depends(get_db), ):
    try:
        return await crud.create_post(db=db, post_data=post)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/posts/{post_id}",
            tags=["posts"],
            summary='Оновити окремий пост з коментарями та темами '
                    'до нього за ID',
            response_model=schemas.PostUpdateWithRelationships)
async def update_posts(post: schemas.PostUpdateWithRelationships,
                       post_id: int,
                       db: AsyncSession = Depends(get_db)):
    try:
        return await crud.update_post(db=db,
                                      post_id=post_id,
                                      post_data=post)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/posts/{post_id}",
               tags=["posts"],
               summary='Видалити окремий пост з прив\'язаними '
                       'коментарями за ID',
               response_model=schemas.PostDeleteWithRelationships)
async def delete_comments(post_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await crud.delete_post(post_id=post_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
