from flask import Blueprint, request
from pydantic import ValidationError
from ..crud import CRUD
from ..models import Participation, DbParticipation
from ..utils import login_required

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
    correctAnswers = CRUD.Question.get_correct_answers_positions()

    if len(p.answers) != len(correctAnswers):
        raise ValidationError(None, None)
    
    answers_summaries = []
    score = 0
    for q, a in zip(correctAnswers, p.answers):
        answers_summaries.append({
            "correctAnswerPosition": q,
            "wasCorrect": q == a
        })
        if q == a:
            score += 1
    
    db_participation = DbParticipation(playerName=p.playerName, score=score)
    id_participation = CRUD.Participation.insert(db_participation)
    return {
        "answersSummaries":answers_summaries,
        "playerName":p.playerName,
        "score":score
    }, 200


@participations_bp.route('/all', methods=['DELETE'])
@login_required
def delete_all():
    """
    Cette fonction permet de supprimer toutes les participations du quiz
    Need Auth
    """
    CRUD.Participation.delete_all()
    return "", 204

    

