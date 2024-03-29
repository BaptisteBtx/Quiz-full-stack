"""
Ce fichiers contient un ensemble de fonctions nécessaires
au fonctionnement de l'api.
"""
import functools
import sqlite3
from flask import abort, request, g
from pydantic import ValidationError

from .jwt_utils import decode_token, JwtError


def login_required(view):
    """Le décorateur de fonction pour les endpoints ayant d'authentification"""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        try:
            token = request.headers.get('Authorization')
            token = token[7:]  # Remove Bearer
            decode_token(token)
            return view(**kwargs)
        except (TypeError, JwtError):
            return abort(401)

    return wrapped_view


def handle_validation_error(e: ValidationError):
    """
    Fonction qui sera appelée lorsqu'une erreur de validation pydantic a lieu.
    """
    return '', 400


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect('./quiz.db')
        g.db.row_factory = sqlite3.Row  # Queries return will behave like a dict
        g.db.isolation_level = None
    return g.db


def close_db(exception=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def create_tables():
    """
    Cette fonction crée les tables SQL si elles n'éxistent pas.
    """
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
            position INT,
            image TEXT,
            answers TEXT
        );
        '''
    )
    db.commit()
    cur.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.register_error_handler(ValidationError, handle_validation_error)
    with app.app_context():
        create_tables()
