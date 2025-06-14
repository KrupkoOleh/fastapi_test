from fastapi import HTTPException
from sqlalchemy import select, asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

from comments import models, schemas


async def get_comments_list(db: AsyncSession,
                            sort_by: str = "created_at",
                            order: str = "desc"):
    if not hasattr(models.Comment, sort_by):
        sort_by = "created_at"

    sort_column = getattr(models.Comment, sort_by)
    order_func = asc if order == "asc" else desc
    queryset = select(models.Comment).order_by(order_func(sort_column))
    comment_list = await db.execute(queryset)
    return comment_list.scalars().all()


async def get_comment_by_id(db: AsyncSession, comment_id: int):
    result = await db.execute(select(models.Comment).filter(
        models.Comment.id == comment_id)
    )
    post = result.scalars().first()
    return post


async def create_comment(db: AsyncSession,
                         comment_data: schemas.CommentCreate):
    comment = models.Comment(
        author=comment_data.author,
        text=comment_data.text,
        rating=comment_data.rating
    )
    db.add(comment)
    await db.commit()
    await db.refresh(comment)
    return comment


async def update_comment(db: AsyncSession,
                         comment_id: int,
                         comment_data: schemas.CommentUpdate):
    comment = await db.get(models.Comment, comment_id)

    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    comment.author = comment_data.author
    comment.text = comment_data.text
    comment.rating = comment_data.rating

    await db.commit()
    await db.refresh(comment)
    return comment


async def delete_comment(db: AsyncSession, comment_id: int):
    comment = await db.get(models.Comment, comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    await db.delete(comment)
    await db.commit()
    return comment
