import httpx
from fastapi.responses import JSONResponse

def categoryList():
    try:
        # Simulate a call to an external API
        response = httpx.get("http://175.126.226.143:3010/v1.0/filter/category/list")
        response.raise_for_status()  # Raise an error for bad responses
        categories = response.json()
        return JSONResponse(content=categories, status_code=200)
    except httpx.RequestError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    except httpx.HTTPStatusError as e:
        return JSONResponse(content={"error": str(e)}, status_code=e.response.status_code)