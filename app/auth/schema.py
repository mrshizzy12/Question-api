from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_name: str
    
    
class UserCreate(UserBase):
    password: str

class UserSchema(UserBase):
    id: int
    expert: bool
    admin: bool
    
    class Config:
        orm_mode = True
        
        
class LoginSchema(UserCreate):
    pass

class TokenSchema(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    

class TokenData(BaseModel):
    id: int