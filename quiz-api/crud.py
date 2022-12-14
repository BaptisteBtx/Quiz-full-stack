from sqlite3 import Connection
import json
from models import Question, Participation
from utils import get_db
from werkzeug.exceptions import NotFound


class CRUD():
    class UnknownEntityException(Exception):
        pass

    class Question():
        @staticmethod
        def insert(q: Question) -> int:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    INSERT INTO questions (title, position, text, image, answers) 
                        SELECT
                            ?, ?, ?, ?, ?
                        WHERE (SELECT count(*)+1 from questions) >= ?
                    ''',
                    (q.title, q.position, q.text, q.image, q.possibleAnswers.json(), q.position)
                )
                db.commit()
                return cur.lastrowid
            finally:
                cur.close()
        
        @staticmethod
        def update(q: Question) -> None:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    UPDATE questions SET
                        title=?, position=?, text=?, image=?, answers=?
                    WHERE id=?
                    ''',
                    (q.title, q.position, q.text, q.image, q.possibleAnswers.json(), q.id)
                )
                db.commit()
                if cur.rowcount != 1:
                    raise NotFound()
            finally:
                cur.close()
    
        @staticmethod
        def get_by_id(id: int) -> Question:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    SELECT * FROM questions WHERE id=?
                    ''',
                    (id,)
                )
                row = cur.fetchone()
                d = dict(row)
                d['possibleAnswers'] = json.loads(d['answers']) # Convert back from json
                return Question(**d)
            except TypeError:
                raise NotFound()
            finally:
                cur.close()

        @staticmethod
        def get_by_position(position: int) -> Question:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    SELECT * FROM questions WHERE position=?
                    ''',
                    (position,)
                )
                row = cur.fetchone()
                d = dict(row)
                d['possibleAnswers'] = json.loads(d['answers']) # Convert back from json
                return Question(**d)
            except TypeError:
                raise NotFound()
            finally:
                cur.close()

        @staticmethod
        def delete(id: int) -> None:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    DELETE FROM questions WHERE id=?
                    '''
                    ,
                    (id,)
                )
                if cur.rowcount != 1:
                    raise NotFound()
            finally:
                cur.close()

        @staticmethod
        def delete_all() -> None:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    DELETE FROM questions
                    '''
                )
            finally:
                cur.close()

    class Participation():
        @staticmethod
        def insert(q: Participation) -> Participation:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    INSERT INTO questions(title, position, text, image, answers) VALUES(?, ?, ?, ?, ?)
                    ''', # TODO: SQL
                    (q.title, q.position, q.text, q.image, q.possibleAnswers.json())
                )
                db.commit()
                q.id = cur.lastrowid
                return q
            finally:
                cur.close()
    
        # @staticmethod
        # def get(id: int) -> Participation:
        #     db = get_db()
        #     cur = db.cursor()
        #     try:
        #         cur.execute(
        #             '''
        #             SELECT * FROM questions WHERE id=?
        #             ''',
        #             (id,)
        #         )
        #         row = cur.fetchone()
        #         d = dict(row)
        #         d['possibleAnswers'] = json.loads(d['answers']) # Convert back from json
        #         return Participation(**d)
        #     except TypeError:
        #         raise NotFound()
        #     finally:
        #         cur.close()

        @staticmethod
        def delete_all() -> None:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    DELETE FROM questions
                    '''
                )
            finally:
                cur.close()

