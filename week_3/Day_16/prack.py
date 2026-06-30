from fastapi import FastAPI, Response
from enum import Enum
from typing import Optional
from routers.blog_get import BlogType
from fastapi import status





app = FastAPI()



@app.get('/status/type')
def get_status(type: BlogType):
    return {'message': f'the application is running perfectly my {type}.'}

@app.get('/blog/{id}', status_code = status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id> 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f' Blog with id {id}'}
    
