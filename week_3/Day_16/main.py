from fastapi import FastAPI
from routers import blog_get
from routers import blog_post





app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index1():
    return {"message": "Hello World"}

@app.get("/hello")
def index2():
    return {"message": "How are you doing today??"}