import os
from pydantic import BaseSettings, AnyHttpUrl
from typing import Optional, List
import secrets
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(basedir, '.env'))


class Setting(BaseSettings):
    SECRET_KEY: Optional[str] =  secrets.token_hex(16)
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DATABASE_URL: str = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}' #'sqlite+aiosqlite:///./db.sqlite'
    ALGORITHM: str = 'HS256'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    PROJECT_NAME: str = 'Question-API'
    
    class Config:
        env_file = '.env'
        case_sensitive = True