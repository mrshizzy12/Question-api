from pydantic import BaseModel
from app.main.schema import QuestionSchema
from typing import List


class UserBase(BaseModel):
    user_name: str
    
    
class UserSchema(UserBase):
    id: int
    expert: bool
    admin: bool
    questions: List[QuestionSchema] = []

    class Config:
        orm_mode = True