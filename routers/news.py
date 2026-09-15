from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_config import get_db
from crud.news import get_all_news_categories
from schemas.news import NewsCategoryOut

# prefix：前缀名字，tags：所属标签分类用
router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/categories")
async def get_news_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await get_all_news_categories(db, skip, limit)
    return {
        "code": 200,
        "msg": "success",
        "data": [NewsCategoryOut.model_validate(item) for item in result],
    }
