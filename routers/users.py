from fastapi import APIRouter

router = APIRouter(prefix="/api/user", tags=["users"])

@router.get("/categories")
async def get_news_categories():
    pass