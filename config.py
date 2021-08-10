from pydantic import BaseSettings
from typing import Optional
import secrets


class Config(BaseSettings):
    SECRET_KEY: Optional[str] =  secrets.token_hex(16)
    ALGORITHM: str = 'HS256'
    
    class Config:
        env_file = '.env'