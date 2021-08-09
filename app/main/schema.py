from typing import Optional
from pydantic import BaseModel

class QuestionBase(BaseModel):
    question: str
   
    
class QuestionCreate(QuestionBase):
    question: str
    expert_id: int

class Question(QuestionBase):
    id: int
    
    class Config:
        orm_mode = True

class Answer(QuestionBase):
    answer: Optional[str] = None
    
    class Config:
        orm_mode = True
        
class AnswerCreate(BaseModel):
    answer: str
    