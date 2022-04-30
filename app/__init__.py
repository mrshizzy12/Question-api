from fastapi import FastAPI
from config import Setting
from fastapi.middleware.cors import CORSMiddleware


settings = Setting()

def create_app():
    app = FastAPI(title=settings.PROJECT_NAME)
    
    app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
           
    from app.auth import auth
    app.include_router(auth, prefix='/api/auth', tags=['auth'])
    
    from app.user import user_bp
    app.include_router(user_bp, prefix='/api/user', tags=['user'])
    
    from app.main import main
    app.include_router(main, prefix='/api/question', tags=['questions'])
    
    
    return app

from . import models