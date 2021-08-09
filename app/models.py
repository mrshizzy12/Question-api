from sqlalchemy import *
from typing import Optional
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha256
from jose import jwt
from app import settings

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), unique=True)
    password_hash = Column(String(100))
    expert = Column(Boolean, default=False)
    admin = Column(Boolean, default=False)
    questions = relationship('Question', foreign_keys='Question.asker_id', backref='asker')
    answers = relationship('Question', foreign_keys='Question.expert_id', backref='expert')
    
    def __str__(self):
        return f'{self.user_name}'

    @property
    def password(self):
        return AttributeError('password property is not readable')
    
    @password.setter
    def password(self, unhashed_password):
        self.password_hash = pbkdf2_sha256.hash(unhashed_password)
        
    def check_password(self, unhashed_password):
        return pbkdf2_sha256.verify(unhashed_password, self.password_hash)
    
    def create_access_token(self, expires_in: Optional[timedelta] = timedelta(minutes=1)):
        token = jwt.encode({'id': self.id,\
            'exp': datetime.utcnow() + expires_in}, settings.SECRET_KEY, settings.ALGORITHM)
        return token
    
        
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text)
    answer = Column(Text)
    asker_id = Column(Integer, ForeignKey('users.id'))
    expert_id = Column(Integer, ForeignKey('users.id'))
    
    def __str__(self):
        return f'{self.question}'