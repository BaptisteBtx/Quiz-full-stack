from flask import Flask, g
from flask_cors import CORS
from flask import Flask, request
from jwt_utils import build_token
from question import Question
import sqlite3
app = Flask(__name__)
CORS(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(':memory:')
        cur = db.cursor()
        cur.execute(
            '''
		CREATE TABLE questions (
			id INTEGER PRIMARY KEY,
			title TEXT,
			text TEXT,
			position TEXT,
			image BLOB, 
			answers TEXT
		);
		'''
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    if payload.get('password') == "flask2023":
        return {'token': build_token()}
    return 'Unauthorized', 401

@app.route('/questions', methods=['POST'])
def create_question():
	payload = request.get_json()
	question = Question.from_payload(payload)
	cur = get_db().cursor()
	try:
		question.insert(cur)
		return question.to_dict()
	finally:
		cur.close()

if __name__ == "__main__":
    app.run()
