from sqlite3 import Cursor
import json


class Question():
    id: int
    title: str
    position: int
    text: str
    image: bytes
    possibleAnswers: str

    def __init__(self, title: str, position: int, text: str, image: bytes, possibleAnswers: str,  id: int = None) -> None:
        self.id = id
        self.title = title
        self.position = position
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers

    @staticmethod
    def from_payload(p: dict):
        p['possibleAnswers'] = json.dumps(p['possibleAnswers'])
        return Question(**p)

    @staticmethod
    def get_by_id(cur: Cursor, id: int):
        res = cur.execute(
            "SELECT id, title, position, text, image, answers FROM questions WHERE id=?", id)
        q = res.fetchone()
        if q:
            q = q[0]
            return Question(*q)
        return None

    def insert(self, cur: Cursor):
        cur.execute(
            '''
            INSERT INTO questions(title, position, text, image, answers) VALUES(?, ?, ?, ?, ?)
            ''',
            (self.title, self.position, self.text, self.image, self.possibleAnswers)
        )
        self.id = cur.lastrowid

    def to_dict(self) -> dict:
        d = {'id': self.id,
             'title': self.title,
             'position': self.position,
             'text': self.text,
             'image': self.image,
             'possibleAnswers': json.loads(self.possibleAnswers)
             }
        return d
