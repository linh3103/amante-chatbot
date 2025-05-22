from pydantic import BaseModel

class CategoryBase(BaseModel):
    CAT_CODE        : int
    CAT_M_CODE      : int
    CAT_NAME        : str
    CAT_NAME_EN     : str
    MB_ICON_FILE_NM2: str

class Category3(CategoryBase):
    pass
    
class Category2(CategoryBase):
    category_3: list[Category3]

class Category1(CategoryBase):
    category_2: list[Category2]

class CategoryListResponse(BaseModel):
    success: bool
    categories: list[Category1]