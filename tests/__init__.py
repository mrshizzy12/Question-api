from app import create_app
from app.dependency import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import engine, Base
from sqlalchemy.orm import sessionmaker



'''
async def override_get_db() -> AsyncSession:
    async with TestingSessionLocal() as session:
        yield session

app = create_app()
app.dependency_overrides[get_db] = override_get_db

auth = {"username":"johndoe", "password":"jupiter"}

TestingSessionLocal = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

'''