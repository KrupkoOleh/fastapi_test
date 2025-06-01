from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.async_paginator import paginate
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from comments import schemas, crud

router = APIRouter()


@router.get("/comments",
            tags=['comments'],
            summary='Отримати усі коментарі',
            response_model=Page[schemas.CommentGet])
async def get_comments(db: AsyncSession = Depends(get_db),
                       sort_by: str = Query("created_at",
                                            escription="Поле для сортування"),
                       order: str = Query("desc",
                                          description="Порядок сортування: "
                                                      "asc або desc")
                       ) -> Page[schemas.CommentGet]:
    try:
        return await paginate(await crud.get_comments_list(db=db,
                                                           sort_by=sort_by,
                                                           order=order))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/comments/{comment_id}",
            tags=['comments'],
            summary='Отримати окремий коментар за ID',
            response_model=schemas.CommentGet)
async def get_comment(comment_id: int,
                      db: AsyncSession = Depends(get_db)):
    try:
        return await crud.get_comment_by_id(db=db, comment_id=comment_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/comments",
             tags=['comments'],
             summary='Створити коментар',
             response_model=schemas.CommentCreate)
async def create_comments(comment: schemas.CommentCreate,
                          db: AsyncSession = Depends(get_db), ):
    try:
        return await crud.create_comment(db=db, comment_data=comment)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/comments/{comment_id}",
            tags=['comments'],
            summary='Оновити коментар за ID',
            response_model=schemas.CommentUpdate)
async def update_comments(comment: schemas.CommentUpdate,
                          comment_id: int,
                          db: AsyncSession = Depends(get_db)):
    try:
        return await crud.update_comment(db=db,
                                         comment_id=comment_id,
                                         comment_data=comment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/comments/{comment_id}",
               tags=['comments'],
               summary='Видалити коментар за ID',
               response_model=schemas.CommentDelete)
async def delete_comments(comment_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await crud.delete_comment(comment_id=comment_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
