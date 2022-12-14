from flask import Flask, request
from flask_cors import CORS
import jwt_utils
import json
import functions as api

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size":0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def login():

	payload = request.get_json()
	
	if(payload['password']=='wrong'):
		return 'Wrong Password', 401
	else:
		token_gen = jwt_utils.build_token()
		response = {
			"token":token_gen
		}
		return json.dumps(response), 200

@app.route('/questions', methods=['POST'])
def questions():

	verif = api.verify_auth(request.headers)
	if not verif:
		return "Unauthorized Access", 401
	body = request.get_json()
	print('body', body)
	return "Response is correct", 200
if __name__ == "__main__":
    app.run()