from .database import engine, Base, SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


async def init_db():
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
        

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session