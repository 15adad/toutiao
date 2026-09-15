from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "mysql+aiomysql://root:root@localhost:3306/fastapi?charset=utf8mb4"

async_engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


# ✅ 依赖注入的是 session，不是 connection
async def get_db():
    async with AsyncSessionLocal() as session:      # ← 用 session 工厂
        try:
            yield session                            # ← 交出 session
            await session.commit()
        except Exception:
            await session.rollback()
            raise