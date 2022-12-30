from typing import Union
from pydantic import BaseModel

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
    answers: Answers

class ParticipationEval(BaseModel):
    id: Union[int,None]
    playerName: str
    date: str
    score: int



