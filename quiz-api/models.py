from pydantic import BaseModel

class Answer(BaseModel):
    text: str
    isCorrect: bool

class Answers(BaseModel):
    __root__: list[Answer]

class Question(BaseModel):
    id: int | None = None
    title: str
    position: int
    text: str
    image: str
    possibleAnswers: Answers

class Participation(BaseModel):
    id: int | None = None
    playerName: str
    answers: Answers