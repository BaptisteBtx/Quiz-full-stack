import json
from .models import Question, Participation, DbParticipation
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
                    SELECT * FROM participations ORDER BY score DESC
                    '''
                )
                scores = [DbParticipation(**dict(s)) for s in cur.fetchall()]
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
                    '''
                )
                questions = []
                for q in cur.fetchall():
                    d = dict(q)
                    d['possibleAnswers'] = json.loads(d['answers']) # Convert back from json
                    # questions.append(Question(**d))
                    questions.append(d)
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
                db.commit()
            finally:
                cur.close()
        
        @staticmethod
        def get_correct_answers_positions():
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    SELECT 
                        CAST(substr(fullkey , 3, LENGTH(fullkey) - 3) as INT) + 1 as correctPosition
                    FROM questions, json_each(questions.answers)
                        WHERE json_extract(value, '$.isCorrect') = 1
                    ORDER BY questions.position ASC
                    '''
                )
                rows = cur.fetchall()
                return [row['correctPosition'] for row in rows]
            finally:
                cur.close()

    class Participation():
        @staticmethod
        def insert(p: DbParticipation) -> int:
            db = get_db()
            cur = db.cursor()
            try:
                cur.execute(
                    '''
                    INSERT INTO participations(playerName, date, score) VALUES (?, ?, ?)
                    ''', 
                    (p.playerName, p.date, p.score)
                )
                db.commit()
                return cur.lastrowid
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
                db.commit()
            finally:
                cur.close()

