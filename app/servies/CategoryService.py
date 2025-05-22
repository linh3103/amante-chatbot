import httpx
from app.config import BASE_URL
from app.shcemas.Category import CategoryListResponse

async def fetchCategories():
    endPoint = "/filter/category/list"
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}{endPoint}"
        print(url)
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return CategoryListResponse(**data).categories
        else:
            raise Exception(f"Error fetching categories: {response.status_code} - {response.text}")
