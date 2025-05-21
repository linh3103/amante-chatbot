from fastapi import APIRouter

router = APIRouter()
@router.get("/categories")
def read_categories():
    return [{"id": 1, "name": "Category 1"}, {"id": 2, "name": "Category 2"}]