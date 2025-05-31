from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies import get_db
from posts import schemas, crud

router = APIRouter()


@router.get("/posts",
            tags=["posts"],
            summary='Отримати усі пости',
            response_model=list[schemas.PostGetWithRelationships])
async def get_posts(db: AsyncSession = Depends(get_db)):
    return await crud.get_post_list(db=db)


@router.get("/posts/{post_id}",
            tags=["posts"],
            summary='Отримати окремий пост з коментарями та темами '
                    'до нього за ID',
            response_model=schemas.PostGetWithRelationships)
async def get_post(post_id: int,
                   db: AsyncSession = Depends(get_db)):
    return await crud.get_post_by_id(db=db, post_id=post_id)


@router.post("/posts",
             tags=["posts"],
             summary='Отримати пост з коментарями та темами до нього',
             response_model=schemas.PostCreateWithRelationships)
async def create_posts(post: schemas.PostCreateWithRelationships,
                       db: AsyncSession = Depends(get_db),):
    return await crud.create_post(db=db, post_data=post)


@router.put("/posts/{post_id}",
            tags=["posts"],
            summary='Оновити окремий пост з коментарями та темами '
                    'до нього за ID',
            response_model=schemas.PostUpdateWithRelationships)
async def update_posts(post: schemas.PostUpdateWithRelationships,
                       post_id: int,
                       db: AsyncSession = Depends(get_db)):
    return await crud.update_post(db=db,
                                  post_id=post_id,
                                  post_data=post)


@router.delete("/posts/{post_id}",
               tags=["posts"],
               summary='Видалити окремий пост з прив\'язаними '
                       'коментарями за ID',
               response_model=schemas.PostDeleteWithRelationships)
async def delete_comments(post_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_post(post_id=post_id, db=db)
