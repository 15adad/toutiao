from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.news import NewsCategory


async def get_all_news_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(NewsCategory).offset(skip).limit(limit)  # 1. 独立函数 select()
    result = await db.execute(stmt)  # 2. 会话执行
    return result.scalars().all()  # 3. 取标量
