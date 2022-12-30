from flask import Blueprint, request
# from crud import CRUD
from ..crud import CRUD
from ..models import Participation
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
    
    questions = CRUD.Question.get_all()
    answers_summaries = []
    score = 0
    for q, a in map(questions, p.answers):
        answer_summary = {}
        for i,q_a in enumerate(q.possibleAnswers):
            if q_a.isCorrect:
                answer_summary["correctAnswerPosition"] = i
                break
        # good_answer = q.possibleAnswers[a].isCorrect
        answer_summary["wasCorrect "] = answer_summary["correctAnswerPosition"]==a
        if answer_summary["wasCorrect "] : 
            score += 1

        answers_summaries.append(answer_summary)
        
    id_participation = CRUD.Participation.insert(p)
    # return db_participation.dict()
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

    

