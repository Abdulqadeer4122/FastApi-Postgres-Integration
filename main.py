from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from pydantic import BaseModel
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
db_dependency = Annotated[Session, Depends(get_db)]


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


@app.get("/question/{question_id}")
def get_question(question_id: int, db: db_dependency):
    result = db.query(models.Question).filter(models.Question.id == question_id).first()
    if result:
        return result
    return HTTPException(status_code=404, detail="question not found")


@app.get("/choices/{q_id}")
async def get_choices(q_id: int, db: db_dependency):
    result = db.query(models.Choices).filter(models.Choices.question_id == q_id).all()
    if result:
        return result
    return HTTPException(status_code=404, detail="The id you provided not true")


@app.post("/question/")
def questions(question: QuestionBase, db: db_dependency):
    db_question = models.Question(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct,
                                   question_id=db_question.id)
        db.add(db_choice)
    db.commit()



