from flask import Flask,request, Blueprint
from flask_cors import CORS
from ..jwt_utils import build_token
from ..crud import CRUD

app = Flask(__name__)
CORS(app)

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@root_bp.route('/quiz-info', methods=['GET'])
def get_quiz_info():
    """
    Cette fonction permet de récupérer des informations d'ordre général sur le quiz
    """
    size = CRUD.DBinfo.count_qst()
    scores = CRUD.DBinfo.get_scores()

    return {"size": size, "scores": scores}, 200 # Scores : tableau d'objet participationResult trié par scores décroissants (player name, score, date)


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
    CRUD.Question.delete_all()
    return 'Ok', 200
