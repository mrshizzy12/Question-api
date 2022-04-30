from fastapi import Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Question
from typing import List
from app.main import main
from app.models import Question, User
from . import schema
from app.auth import schema as auth_schema
from app.auth.o_auth import get_current_user
from ..dependency import get_db



        
@main.get('/')
async def test():
    '''testing API connection'''
    return {'ping': 'pong'}


@main.get('/all', response_model=List[schema.QuestionSchema], status_code=status.HTTP_200_OK)
async def get_all_questions(db: AsyncSession = Depends(get_db)):
    questions = await db.execute(select(Question).filter(Question.answer != None))
    return questions.scalars().all()


@main.post('/ask', response_model=schema.QuestionSchema, status_code=status.HTTP_201_CREATED)
async def create_question(question: schema.QuestionCreate, current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    new_question = Question(question=question.question, asker_id=current_user.id, expert_id=question.expert_id)
    try:
        db.add(new_question)
        await db.commit()
    except Exception:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error! 500 Internal server error!')
    return new_question


@main.get('/{id}', response_model=schema.QuestionSchema, status_code=status.HTTP_200_OK)
async def get_question(id: int, db: AsyncSession = Depends(get_db)):
    question = await db.execute(select(Question).filter(Question.id == id))
    question = question.scalars().first()
    if question:
        return question
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error! 404 Not Found!')
    
    
@main.put('/{id}/answer/', response_model=schema.QuestionSchema, status_code=status.HTTP_202_ACCEPTED)
async def answer(id: int, answer: schema.AnswerCreate, current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    question = await db.execute(select(Question).filter(Question.expert_id == current_user.id).filter(Question.id == id))
    question = question.scalars().first()
    if question:
        question.answer = answer.answer
        try:
            await db.commit()
            return question
        except Exception:
           await db.rollback()
           raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error! 500 Internal server error!')
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error! 404 Not Found!')
     
     
@main.get('/unanswered/', response_model=List[schema.QuestionSchema], status_code=status.HTTP_200_OK)
async def unanswered(current_user: auth_schema.TokenData = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    user = await db.execute(select(User).filter(User.id == current_user.id))
    user = user.scalars().one()
    if user.expert:
       questions = await db.execute(select(Question).filter(Question.expert_id == current_user.id).filter(Question.answer==None))
       questions = questions.scalars().all()
    elif user.admin:
        questions = await db.execute(select(Question).filter(Question.answer==None))
        questions = questions.scalars().all()
    else:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Error! 401 unauthorized!')
    return questions