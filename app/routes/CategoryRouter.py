from fastapi import APIRouter
from app.controllers.CategoryController import categoryList

router = APIRouter()
@router.get("/categories")
async def read_categories():
    return await categoryList()