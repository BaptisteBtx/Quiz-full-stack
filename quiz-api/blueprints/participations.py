"""
Les endpoints de l'api pour /participations
"""
from flask import Blueprint, request
from pydantic import ValidationError
from ..crud import CRUD
from ..models import Participation, DbParticipation
from ..utils import login_required

participations_bp = Blueprint('participations_bp', __name__)


@participations_bp.route('', methods=['POST'], strict_slashes=False)
def create():
    """
    Cette fonction permet d'enregistrer un participation au quiz.
    Un résumé des réponses est ensuite retourné, le score final ainsi que le nom du joueur.
    Payload : Participation
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
    CRUD.Participation.insert(db_participation)
    return {
        "answersSummaries": answers_summaries,
        "playerName": p.playerName,
        "score": score
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
