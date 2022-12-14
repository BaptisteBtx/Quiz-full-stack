import functools
from flask import abort, request, g
from jwt_utils import decode_token, JwtError
import sqlite3
 
def login_required(view):
    """View decorator to validate token"""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        try:
            token = request.headers.get('Authorization')
            token = token[7:] # Remove Bearer
            decode_token(token)
            return view(**kwargs)
        except (TypeError, JwtError):
            return abort(401)

    return wrapped_view


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect('./testV2.db')
        g.db.row_factory = sqlite3.Row # Queries return will behave like a dict
        g.db.isolation_level = None
    return g.db


def close_db(exception = None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def create_tables():
    db = get_db()
    cur = db.cursor()
    cur.execute(
        '''
		CREATE TABLE IF NOT EXISTS questions (
			id INTEGER PRIMARY KEY,
			title TEXT,
			text TEXT,
			position TEXT,
			image TEXT, 
			answers TEXT
		);
		'''
    )
    cur.execute(
        '''
        CREATE TRIGGER IF NOT EXISTS pos_after_insert
        BEFORE INSERT ON questions
        BEGIN
            UPDATE questions SET
                position = position + 1
            WHERE position >= NEW.position;
        END;
        '''
    )
    cur.execute(
        '''
        CREATE TRIGGER IF NOT EXISTS pos_after_update
        AFTER UPDATE ON questions
        WHEN OLD.position != NEW.position
        BEGIN
            UPDATE questions SET
                position = CASE
                        WHEN (OLD.position > position AND position >= NEW.position) THEN position + 1
                        WHEN (OLD.position < position AND position < NEW.position) THEN position - 1
                        ELSE position
                    END
            WHERE id != OLD.id;
        END;
        '''
        #         CREATE TRIGGER IF NOT EXISTS pos_after_update
        # AFTER UPDATE ON questions
        # WHEN OLD.position != NEW.position
        # BEGIN
        #     UPDATE questions SET
        #         position = CASE position
        #                 WHEN OLD.position <= NEW.position THEN position - 1
        #                 WHEN OLD.position >= NEW.position THEN position + 1
        #                 ELSE position
        #             END
        #     WHERE id != NEW.id
        #         AND position >= min(OLD.position, NEW.position)
        #         AND position <= max(OLD.position, NEW.position);
        # END;
    )
    cur.execute(
        '''
        CREATE TRIGGER IF NOT EXISTS pos_after_delete
        AFTER DELETE ON questions
        BEGIN
            UPDATE questions SET
                position = position - 1
            WHERE
                position >= OLD.position;
        END;
        '''
    )
    cur.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    with app.app_context():
        create_tables()
    
