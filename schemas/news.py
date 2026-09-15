# schemas/news.py
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class NewsCategoryOut(BaseModel):
    # 允许从 ORM 对象的属性读取（关键）
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sort_order: int
    created_at: datetime
    updated_at: datetime