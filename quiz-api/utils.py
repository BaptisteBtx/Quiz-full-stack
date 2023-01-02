import functools
from flask import abort, request, g
from .jwt_utils import decode_token, JwtError
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
        g.db = sqlite3.connect('./quiz.db')
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
		CREATE TABLE IF NOT EXISTS participations (
			id INTEGER PRIMARY KEY,
			playerName TEXT,
			date TEXT,
			score INTEGER
		);
		'''
    )
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
    
