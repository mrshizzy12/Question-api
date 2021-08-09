from pydantic import BaseModel


class UserBase(BaseModel):
    user_name:str
    
    
class UserSchema(UserBase):
    id:int
    expert:bool
    admin:bool

    class Config:
        orm_mode = True