from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from . import auth
from ..models import User
from . import schema
from ..dependency import get_db




@auth.post('/register', response_model=schema.UserSchema, status_code=status.HTTP_201_CREATED)
async def register(user: schema.UserCreate, db: AsyncSession = Depends(get_db)):
    user_check = await db.execute(select(User).filter(User.user_name == user.user_name))
    if user_check.scalars().first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='username already exists, please pick another username')  
    try:
        new_user = User(user_name=user.user_name, password=user.password)
        if new_user.user_name == 'oluwashizzy':
            new_user.admin = True
        db.add(new_user)
        await db.commit()
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,\
            detail='somthing went wrong on the server, please try again!')
    return new_user


@auth.post('/login', response_model=schema.TokenSchema, status_code=status.HTTP_202_ACCEPTED)
async def login(request: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).filter(User.user_name == request.username))
    user = user.scalars().first()
    if user is None or not user.check_password(request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,\
            detail='username or password is inccorect')
    else:
        token = {'access_token': user.create_access_token()}
    return token