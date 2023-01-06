"""
Les endpoints de l'api pour /
"""
from flask import Flask, request, Blueprint
from flask_cors import CORS
from ..jwt_utils import build_token
from ..crud import CRUD
from ..models import QuizInfo

app = Flask(__name__)
CORS(app)

root_bp = Blueprint('root_bp', __name__)


@root_bp.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    """
    Cette fonction permet de récupérer le nombre de questions et les scores enregistrés.
    """
    size = CRUD.DBinfo.count_qst()
    scores = CRUD.DBinfo.get_scores()
    infos = QuizInfo(size=size, scores=scores)

    return infos.dict(), 200


@root_bp.route('/login', methods=['POST'])
def login():
    """
    Obtenir un token d'authentification en tant qu'administrateur avec le bon mot de passe.
    """
    payload = request.get_json()
    if payload.get('password') == "flask2023":
        return {'token': build_token()}
    return 'Unauthorized', 401


@root_bp.route('/rebuild-db', methods=['POST'])
def rebuild_db():
    """
    Permet de reconstruire la base de données.
    """
    CRUD.Question.delete_all()
    CRUD.Participation.delete_all()
    return 'Ok', 200
