from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional



router = APIRouter(
    prefix='/blog',
    tags=['blog']


)
@router.get("/hello")
def index2():
    return {"message": "How are you doing today??"}

@router.get('/all')
def get_all_blogs(page, page_size):
    return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/summerization')
def get_summerization(page, page_size: Optional[int] = None):
    return {'message': f'Summeraization blogs on page {page} with page size {page_size}'}

@router.post('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

    
@router.post('/type/{type}')
def get_blog(type: BlogType):
    return {"messsage": f'Blog type {type}'}
