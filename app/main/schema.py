from typing import Optional
from pydantic import BaseModel

class QuestionBase(BaseModel):
    question: str
   
    
class QuestionCreate(QuestionBase):
    expert_id: int

class QuestionSchema(QuestionBase):
    id: int
    answer: Optional[str] = None
    
    class Config:
        orm_mode = True

        
class AnswerCreate(BaseModel):
    answer: str
    