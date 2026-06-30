from fastapi import APIRouter, status
from pydantic import BaseModel


router = APIRouter(
    prefix='/blog',
    tags=['blog'])

class BlogModel(BaseModel):
    pass

@router.post('/new')
def creat_blog(_):
    pass