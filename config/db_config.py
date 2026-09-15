from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/fastapi?charset=utf8mb4"

# 创建异步引擎
async_engine = create_async_engine(
    DATABASE_URL,
    echo=True, # 输出SQL日志,默认False
)

# 创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Session依赖
async def get_db():
    async with async_engine.begin() as conn:
        try:
            yield conn
            await conn.commit()
        except Exception:
            await conn.rollback()
            raise
        finally:
            await conn.close()