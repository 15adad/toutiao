from fastapi import APIRouter

# prefix：前缀名字，tags：所属标签分类用
router = APIRouter(prefix="/api/news", tags=["news"])

@router.get("/categories")
async def get_news_categories():
    pass