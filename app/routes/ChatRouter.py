from fastapi import APIRouter
from fastapi import Request
from app.controllers.chat import chat
router = APIRouter()

@router.post("/chat")
async def chatbot(request: Request):
    controllerRequest = request
    return await chat(controllerRequest)