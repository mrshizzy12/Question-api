from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from app import settings
from . import schema


oauth2 = OAuth2PasswordBearer(tokenUrl='api/auth/login')


async def get_current_user(token: str = Depends(oauth2)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid credentials!',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id = payload.get('id')
        if id is None:
            raise credential_exception
        token_data = schema.TokenData(id=id)
        return token_data
    except JWTError as e:
        raise credential_exception