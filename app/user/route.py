from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import user_bp
from sqlalchemy import select
from ..dependency import get_db
from ..auth.o_auth import get_current_user
from ..models import User
from . import schema
from ..auth import schema as auth_schema
from sqlalchemy.orm import selectinload



@user_bp.get('/all', response_model=List[schema.UserSchema], status_code=status.HTTP_200_OK)
async def get_all_users(current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    admin = await db.execute(select(User).filter(User.id == current_user.id))
    admin = admin.scalars().first()
    if admin.admin:
        users = await db.execute(select(User).order_by(User.id).options(selectinload(User.questions)))
        return users.scalars().all()   
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized.')
    
    

@user_bp.get('/experts', response_model=List[schema.UserSchema], status_code=status.HTTP_200_OK)
async def get_all_experts(current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    admin = await db.execute(select(User).filter(User.id == current_user.id))
    admin = admin.scalars().first()
    if admin.admin:
        users = await db.execute(select(User).filter(User.expert == True).options(selectinload(User.questions)))
        return users.scalars().all()
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Eorror! 401 Unauthorized.')
   


@user_bp.put('/{id}/promote/', response_model=schema.UserSchema, status_code=status.HTTP_202_ACCEPTED)
async def promote(id: int, current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    admin = await db.execute(select(User).filter(User.id == current_user.id))
    admin = admin.scalars().first()
    if admin.admin:
        user = await db.execute(select(User).filter(User.id == id).options(selectinload(User.questions)))
        user = user.scalars().first()
        if user:
            user.expert = True
            try:
                await db.commit()
            except Exception as e:
                await db.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error! 500 internal server error.')
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error! 404 Not Found.')
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Eorror! 401 Unauthorized.')
    return user