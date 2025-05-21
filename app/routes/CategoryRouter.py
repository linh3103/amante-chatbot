from fastapi import APIRouter
from app.controllers.CategoryController import categoryList

router = APIRouter()
@router.get("/categories")
def read_categories():
    return categoryList()