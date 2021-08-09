from fastapi import FastAPI
from config import Config

settings = Config()

def create_app():
    app = FastAPI()
     
    from app.auth import auth
    app.include_router(auth, prefix='/api/auth', tags=['auth'])
    
    from app.user import user_bp
    app.include_router(user_bp, prefix='/api/user', tags=['user'])
    
    from app.main import main
    app.include_router(main, prefix='/api/question', tags=['questions'])
    
    from . import models
    
    return app