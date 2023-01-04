from flask import Blueprint, request
from ..crud import CRUD
from ..models import Question
from ..utils import login_required

questions_bp = Blueprint('questions_bp', __name__)


@questions_bp.route('/all', methods=['GET'])
def get_all():
    """
    Cette fonction permet de récupérer toutes les questions de la base de données.
    """
    db_question = CRUD.Question.get_all()
    return db_question, 200
    
@questions_bp.route('/<int:questionId>', methods=['GET'])
def get_by_id(questionId: int):
    """
    Cette fonction permet de récupérer le contenu d’une question à partir de son identifiant de base de données.
    """
    db_question = CRUD.Question.get_by_id(questionId)
    # if not db_question:
    #     raise f"Question {questionId} not found in db"
    return db_question.dict(), 200

@questions_bp.route('', methods=['GET'], strict_slashes=False)
def get_by_position():
    """
    Cette fonction permet de récupérer le contenu d'une question à partir de sa position de base de données.
    """
    p = request.args.get('position')
    db_question = CRUD.Question.get_by_position(p)
    return db_question.dict(), 200

       

@questions_bp.route('', methods=['POST'], strict_slashes=False)
@login_required
def create():
    """
    Cette fonction permet d'ajouter une question du quiz
    Need Auth
    """
    payload = request.get_json()
    q = Question(**payload)
    id = CRUD.Question.insert(q)
    return {"id": id}, 200

@questions_bp.route('/<int:questionId>', methods=['PUT'])
@login_required
def update(questionId: int):
    """
    Cette fonction permet de mettre à jour une question du quiz à partir de son identifiant base de données
    Need Auth
    """
    payload = request.get_json()
    q = Question(**payload, id=questionId)
    # q.id = questionId
    # try:
    #     db_question = CRUD.Question.get_by_id(q.id)
    #     if not db_question:
    #         raise f"Question {q.id} not found in db"
    CRUD.Question.update(q)
    return '', 204

@questions_bp.route('/<int:questionId>', methods=['DELETE'])
@login_required
def delete(questionId: int):
    """
    Cette fonction permet de supprimer une question du quiz à partir de son identifiant base de données
    Need Auth
    """
    CRUD.Question.delete(questionId)
    return '',204 # Vide

@questions_bp.route('/all', methods=['DELETE'])
@login_required
def delete_all():
    """
    Cette fonction permet de supprimer toutes les questions du quiz
    Need Auth
    """
    CRUD.Question.delete_all()
    return '',204 # Vide

    

