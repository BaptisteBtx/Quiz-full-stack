from typing import Union
from pydantic import BaseModel, Field
from datetime import datetime

class Answer(BaseModel):
    text: str
    isCorrect: bool

class Answers(BaseModel):
    __root__: list[Answer]

class Question(BaseModel):
    id: Union[int, None]
    title: str
    position: int
    text: str
    image: str
    possibleAnswers: Answers


class Participation(BaseModel):
    playerName: str
    answers: list[int]

class DbParticipation(BaseModel):
    playerName: str
    date: datetime = Field(default_factory=datetime.utcnow)
    score: int

    class Config:
        json_encoders = {
            datetime: lambda v: v.strftime('%d/%m/%Y')
        }

class DbParticipations(BaseModel):
    __root__: list[DbParticipation]

class QuizInfo(BaseModel):
    size: int
    scores: DbParticipations