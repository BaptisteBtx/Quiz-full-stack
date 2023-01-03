import axios from "axios";

const instance = axios.create({
  // baseURL: 'http://127.0.0.1:5000',
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
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
    return this.call("get", "questions/all").then(d => d.data);
  },
  saveParticipation(participation) {
    return this.post("", participation);
  },
  login(password) {
    //To Do : get Token for user
    return this.call("post", "login", { password: password })
  }
};