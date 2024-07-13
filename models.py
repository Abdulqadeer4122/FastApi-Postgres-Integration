from database import Base
from sqlalchemy import Column, Integer, String, Boolean, text, ForeignKey


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, nullable=False)
    question_text = Column(String, index=True)


class Choices(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, nullable=False)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
