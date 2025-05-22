import httpx
from fastapi.responses import JSONResponse
from app.servies.CategoryService import fetchCategories

async def categoryList():
    try:
        categories = await fetchCategories()
        if not categories:
            return JSONResponse(content={"message": "No categories found"})
        else:
            return JSONResponse(
                content={
                    "success": True,
                    "message": "Categories fetched successfully",
                    "categories": [c.model_dump() for c in categories],
                }
            )
    except httpx.RequestError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    except httpx.HTTPStatusError as e:
        return JSONResponse(content={"error": str(e)}, status_code=e.response.status_code)