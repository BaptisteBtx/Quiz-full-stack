import axios from "axios";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
	json: true,
});

export default {
	async call(method, resource, data = null, token = null) {
		var headers = {
			"Content-Type": "application/json",
		};
		if (token != null) {
			headers.authorization = "Bearer " + token;
		}

		return instance({
			method,
			headers: headers,
			url: resource,
			data,
		})
			.then((response) => {
				return { status: response.status, data: response.data };
			})
			.catch((error) => {
				return error;
			});
	},
	getQuizInfo() {
		return this.call("get", "quiz-info");
	},
	getQuestion(position) {
		return this.call("get", "questions?position=" + position);
	},
	getAllQuestions() {
		return this.call("get", "questions/all");
	},
	saveParticipation(username, participation) {
		return this.call("post", "participations", { playerName: username, answers: participation });
	},
	login(password) {
		return this.call("post", "login", { password: password });
	},
	saveQuestion(question, token) {
		const id = question.id
		delete question.id
		return this.call("put", "questions/" + id, question, token);
	},
	deleteQuestion(question, token) {
		return this.call("delete", "questions/" + question.id, question, token);
	},
	addQuestion(question, token) {
		return this.call("post", "questions", question, token)
	}
};
