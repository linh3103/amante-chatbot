from fastapi.responses import JSONResponse
from fastapi import Request

async def chat(request: Request):
    data = await request.json()
    message = data.get("message")
    
            
   