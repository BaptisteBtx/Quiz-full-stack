import json
from .models import Question, Participation
from .utils import get_db
from werkzeug.exceptions import NotFound, InternalServerError


class CRUD():
    class UnknownEntityException(Exception):
        pass

    class DBinfo():
        @staticmethod
        def count_qst():
            db = get_db()
            cur = db.cursor()
            try: 
                cur.execute(
                    '''
                    SELECT count(*) as cnt FROM questions
                    '''
                )
                count = dict(cur.fetchone())["cnt"]
                return count
            finally:
                cur.close()
        
        @staticmethod
        def get_scores():
            db = get_db()
            cur = db.cursor()
            try: 
                cur.execute(
                    '''
                    SELECT * FROM participations ORDER BY score
                    '''
                )
                scores = [Participation(**dict(s)) for s in cur.fetchall()]
                return scores
                
            finally:
                cur.close()
        
            

    class Question():
        @staticmethod
        def insert(q: Question) -> int:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute('''BEGIN''');
                cur.execute(
                    '''
                    UPDATE questions SET
                        position = position + 1
                    WHERE position >= ?
                    ''', (q.position,)
                )
                cur.execute(
                    '''
                    INSERT INTO questions (title, position, text, image, answers) 
                    VALUES (?, ?, ?, ?, ?)
                    ''',
                    (q.title, q.position, q.text, q.image, q.possibleAnswers.json())
                )
                db.commit()
                return cur.lastrowid
            except Exception as e:
                cur.execute("rollback")
                raise InternalServerError()
            finally:
                cur.close()
        
        @staticmethod
        def update(q: Question) -> None:
            db = get_db()
            cur = db.cursor()
            try:
                ## Transaction
                cur.execute('''BEGIN''')
                # DELETE
                cur.execute(
                '''
                    UPDATE questions SET
                        position = position - 1
                    WHERE position >= (SELECT position FROM questions WHERE id=?)
                ''', (q.id,)
                )
                cur.execute(
                    '''
                    DELETE FROM questions WHERE id=?
                    ''', (q.id,)
                )
                if cur.rowcount != 1:
                    raise NotFound()
                # INSERT
                cur.execute(
                    '''
                    UPDATE questions SET
                        position = position + 1
                    WHERE position >= ?
                    ''', (q.position,)
                )
                cur.execute(
                    '''
                    INSERT INTO questions (id, title, position, text, image, answers) 
                    VALUES (?, ?, ?, ?, ?, ?)
                    ''',
                    (q.id, q.title, q.position, q.text, q.image, q.possibleAnswers.json())
                )
                db.commit()
                rows_affected = cur.rowcount
            except NotFound:
                raise NotFound()
            except Exception as e:
                cur.execute("rollback")
                raise InternalServerError()
            finally:
                cur.close()

            if rows_affected != 1:
                raise NotFound()
           
            

            # db = get_db()
            # cur = db.cursor()

            # try:
            #     # Manage positions
            #     questions = CRUD.Question.get_all()
            #     for db_q in questions:
            #         if db_q.id == q.id:
            #             old_position = db_q.position
                    
            #     questions.insert(q.position-1, questions.pop(old_position-1)) # Switch positions
            #     for i in range(questions):
            #         questions[i].position = i+1

            #     cur.executemany(
            #         '''
            #         UPDATE questions SET position=?
            #         WHERE id=?
            #         ''',
            #         # (q.title, q.position, q.text, q.image, q.possibleAnswers.json(), q.id)
            #         (questions)
            #     )
            #     db.commit()
            #     if cur.rowcount != 1:
            #         raise NotFound()
            # finally:
            #     cur.close()
    
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
        def get_all() -> list[Question]:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    SELECT * FROM questions ORDER BY position
                    ''',
                    (id,)
                )
                questions = []
                for q in cur.fetchall():
                    d = dict(q)
                    d['possibleAnswers'] = json.loads(d['answers']) # Convert back from json
                    questions.append(Question(**d))

                return questions
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
            rows_affected = 0
            try:
                cur.execute('''BEGIN''');
                cur.execute(
                '''
                    UPDATE questions SET
                        position = position - 1
                    WHERE position >= (SELECT position FROM questions WHERE id=?)
                ''', (id,)
                );
                cur.execute(
                    '''
                    DELETE FROM questions WHERE id=?
                    ''', (id,)
                )
                db.commit()
                rows_affected = cur.rowcount
            except Exception:
                cur.execute("rollback")
                raise InternalServerError()
            finally:
                cur.close()
            
            if rows_affected != 1:
                raise NotFound()

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
        def insert(p: Participation) -> int:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    INSERT INTO participations(playerName, answers, date, score) VALUES(?, ?, ?, ?)
                    ''', 
                    (p.playerName, p.answers.json(), p.date, p.score)
                )
                db.commit()
                # p.id = cur.lastrowid
                return cur.lastrowid
            finally:
                cur.close()
    
        @staticmethod
        def get(id: int) -> Participation:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    SELECT * FROM participations WHERE id=?
                    ''',
                    (id,)
                )
                row = cur.fetchone()
                d = dict(row)
                d['answers'] = json.loads(d['answers']) # Convert back from json
                return Participation(**d)
            except TypeError:
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
                    DELETE FROM participations
                    '''
                )
            finally:
                cur.close()

