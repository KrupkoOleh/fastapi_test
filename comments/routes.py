from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from comments import schemas, crud

router = APIRouter()


@router.get("/comments",
            tags=['comments'],
            summary='Отримати усі коментарі',
            response_model=list[schemas.CommentBaseSchema])
async def get_comments(db: AsyncSession = Depends(get_db)):
    return await crud.get_comments_list(db=db)


@router.get("/comments/{comment_id}",
            tags=['comments'],
            summary='Отримати окремий коментар за ID',
            response_model=schemas.CommentBaseSchema)
async def get_comment(comment_id: int,
                      db: AsyncSession = Depends(get_db)):
    return await crud.get_comment_by_id(db=db, comment_id=comment_id)


@router.post("/comments",
             tags=['comments'],
             summary='Створити коментар',
             response_model=schemas.CommentCreate)
async def create_comments(comment: schemas.CommentCreate,
                          db: AsyncSession = Depends(get_db),):
    return await crud.create_comment(db=db, comment_data=comment)


@router.put("/comments/{comment_id}",
            tags=['comments'],
            summary='Оновити коментар за ID',
            response_model=schemas.CommentUpdate)
async def update_comments(comment: schemas.CommentUpdate,
                          comment_id: int,
                          db: AsyncSession = Depends(get_db)):
    return await crud.update_comment(db=db,
                                     comment_id=comment_id,
                                     comment_data=comment)


@router.delete("/comments/{comment_id}",
               tags=['comments'],
               summary='Видалити коментар за ID',
               response_model=schemas.CommentDelete)
async def delete_comments(comment_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_comment(comment_id=comment_id, db=db)
