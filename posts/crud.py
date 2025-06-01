from fastapi import HTTPException
from sqlalchemy import select, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from comments.models import Comment
from posts import models, schemas
from posts.schemas import PostDeleteWithRelationships
from topics.models import Topic


async def get_post_list(db: AsyncSession,
                        sort_by: str = "created_at",
                        order: str = "desc"):
    if not hasattr(models.Post, sort_by):
        sort_by = "created_at"

    sort_column = getattr(models.Post, sort_by)
    order_func = asc if order == "asc" else desc
    queryset = select(models.Post).options(
        selectinload(models.Post.comments),
        selectinload(models.Post.topics)
    ).order_by(order_func(sort_column))
    post_list = await db.execute(queryset)
    return post_list.scalars().all()


async def get_post_by_id(db: AsyncSession, post_id: int):
    result = select(models.Post).options(
        selectinload(models.Post.comments),
        selectinload(models.Post.topics)
    ).filter(models.Post.id == post_id)
    post = await db.execute(result)
    return post.scalars().first()


async def create_post(db: AsyncSession,
                      post_data: schemas.PostCreateWithRelationships):
    post = models.Post(
        title=post_data.title,
        content=post_data.content,
        author=post_data.author,
        topics=[],
        comments=[]
    )

    db.add(post)
    await db.flush()

    for comment_data in post_data.comments:
        comment = Comment(
            author=comment_data.author,
            text=comment_data.text,
            rating=comment_data.rating,
            post=post
        )
        db.add(comment)

    topics_to_add = []
    for topic_data in post_data.topics:
        result = await db.execute(select(Topic).where(
            Topic.title == topic_data.title)
        )
        topic = result.scalars().first()
        if not topic:
            topic = Topic(title=topic_data.title)
            db.add(topic)
            await db.flush()
        topics_to_add.append(topic)

    post.topics = topics_to_add

    result = await db.execute(
        select(models.Post)
        .options(
            selectinload(models.Post.comments),
            selectinload(models.Post.topics)
        )
        .where(models.Post.id == post.id)
    )
    post_with_relations = result.scalar_one()
    await db.commit()
    await db.refresh(post)
    return post_with_relations


async def update_post(db: AsyncSession,
                      post_id: int,
                      post_data: schemas.PostUpdateWithRelationships):
    post = await db.get(models.Post, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.title = post_data.title
    post.content = post_data.content
    post.author = post_data.author

    post.comments.clear()
    post.topics.clear()
    await db.flush()

    for comment_data in post_data.comments:
        comment = Comment(
            author=comment_data.author,
            text=comment_data.text,
            rating=comment_data.rating,
            post=post
        )
        db.add(comment)

    for topic_data in post_data.topics:
        existing_topic = await db.execute(select(Topic).where(
            Topic.title == topic_data.title)
        )
        topic = existing_topic.scalars().first()
        if not topic:
            topic = Topic(title=topic_data.title)
        post.topics.append(topic)

    await db.commit()
    await db.refresh(post)

    return post


async def delete_post(db: AsyncSession, post_id: int):
    post = await db.get(models.Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    post_data = PostDeleteWithRelationships.from_orm(post)

    await db.delete(post)
    await db.commit()
    return post_data
