from fastapi import FastAPI
from app.routes.CategoryRouter import router as category_router

app = FastAPI()
app.include_router(category_router)