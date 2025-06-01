from fastapi import FastAPI

from topics import routes as topic_router
from comments import routes as comment_router
from posts import routes as post_router
from auth import routes as auth_router

from fastapi_pagination import add_pagination

app = FastAPI()
add_pagination(app)

app.include_router(topic_router.router)
app.include_router(comment_router.router)
app.include_router(post_router.router)
app.include_router(auth_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
