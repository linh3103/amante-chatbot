from fastapi import FastAPI
from app.routes.CategoryRouter import router as category_router
from app.routes.ChatRouter import router as chat_router

app = FastAPI()
app.include_router(category_router)
app.include_router(chat_router)