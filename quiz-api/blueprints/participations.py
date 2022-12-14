from flask import Blueprint, request
# from crud import CRUD
from crud import CRUD
from models import Participation
from utils import login_required

participations_bp = Blueprint('participations_bp', __name__)


# @questions_bp.route('/<int:id>', methods=['GET'])
# def get_by_id(id: int):
#     """
#     Cette fonction permet de récupérer le contenu d’une question à partir de son identifiant de base de données.
#     """
#     db_question = CRUD.Question.get_by_id(id)
#     if not db_question:
#         raise f"Question {id} not found in db"
#     return db_question.dict()
      

@participations_bp.route('/', methods=['POST'])
def create():
    """
    Cette fonction permet d'envoyer la liste des réponses sélectionnées par un participant pour l'ensemble du quiz
    Payload : player_name, answers
    """
    payload = request.get_json()
    p = Participation(**payload) 
    # db_question = CRUD.Question.get_by_position(q.position)
    # if not db_question:
        # raise f"Question {q.position} not found in db"
    db_participation = CRUD.Participation.insert(p)
    # return db_participation.dict()
    return {
        "answersSummaries":[],
        "playerName":p.playerName,
        "score":p.score
        

    }


@participations_bp.route('/all', methods=['DELETE'])
@login_required
def delete_all():
    """
    Cette fonction permet de supprimer toutes les participations du quiz
    Need Auth
    """
    CRUD.Participation.delete_all()

    

