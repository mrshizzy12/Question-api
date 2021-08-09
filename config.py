from pydantic import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv
import secrets


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(BaseSettings):
    SECRET_KEY: Optional[str] = os.getenv('SECRET_KEY', secrets.token_hex(16))
    ALGORITHM: str = 'HS256'