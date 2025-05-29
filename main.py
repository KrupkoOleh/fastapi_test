from fastapi import FastAPI

from topics import routes as topic_router

app = FastAPI()

app.include_router(topic_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
