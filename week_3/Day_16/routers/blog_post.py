from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List


router = APIRouter(
    prefix='/blog',
    tags=['blog'])

class Image(BaseModel):
       url: str
       alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: dict ={'key1': 'val1'}
    image: Optional[Image] = None



@router.post('/new/{id}')
def creat_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
        }

@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
                    comment_id: int = Query(None,
                    title ='comment_id',
                    description='The id of the commments',
                    alias='commentId',
                    deprecated=True
                ),
                content: str = Body(...,
                        min_lenght=10,
                        max_lenght=50,
                        regex = '^[a-z\s]*$'
                ),
                v: Optional[List[str]] = Query([1.0,1.1,1.2])
    
            ):
            return {
                'blog': blog,
                'id': id,
                'comment_id': comment_id,
                'content': content,
                'version': v
    }

def required_functionality():
    return {'message': 'Learning FastAPI is important'}