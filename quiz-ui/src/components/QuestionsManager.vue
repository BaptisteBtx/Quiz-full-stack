<script setup>
import { ref, watchEffect } from "vue";
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from "./QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";
import { useRouter } from "vue-router";
import QuizApiService from "../services/QuizApiService";
import ParticipationStorageService from "../services/ParticipationStorageService";
const router = useRouter();

const error = ref(null);
const quizInfo = ref(null);
const username = ref(ParticipationStorageService.getPlayerName());
const questions = ref(null);

const questionLoaded = ref(false);

try {
  quizInfo.value = await quizApiService.getQuizInfo();
  questions.value = await quizApiService.getAllQuestions(); // Charge question 1 au lancement
} catch (error) {
  console.log(error);
  router.push("/"); // TODO : Page d'erreur
}

const totalQuestionNumber = quizInfo.value.data.size;

const question = ref(questions.value[0]);

const selectedAnswers = ref([]);
const selectedAnswer = ref(null);

async function loadNextQuestion() {
  selectedAnswers.value.push(selectedAnswer.value);
  if (question.value.position >= totalQuestionNumber) {
    endQuiz();
  } else {
    question.value = questions.value[question.value.position];
    console.log(selectedAnswers.value);
    // index de la question suivante = index courant + 1 = position courante
  }
  selectedAnswer.value = null;
}

async function endQuiz() {
  try {
    const participation = await QuizApiService.saveParticipation(
      username.value,
      selectedAnswers.value
    );
    const score = participation.score;
    ParticipationStorageService.saveParticipationScore(username, score);
  } catch (error) {
    console.log(error);
  }

  router.push("/");
}

function setSelectedAnswer(index) {
  selectedAnswer.value = index + 1;
}

// questionLoaded.value = true
</script>

<template>
  <div class="question_manager" v-if="question">
    <h1>
      Question : {{ question.position }} /
      {{ totalQuestionNumber }}
    </h1>
    <div class="question">
      <QuestionDisplay
        class="question"
        :key="question"
        :question="question"
        @answer-selected="setSelectedAnswer"
      ></QuestionDisplay>
    </div>
    <br />
    <p v-if="selectedAnswer">Réponse choisie : n°{{ selectedAnswer }}</p>
    <p v-else>Choisissez une réponse.</p>
    <button
      type="button"
      class="btn btn-success"
      @click="loadNextQuestion"
      :disabled="!selectedAnswer"
    >
      Suivant
    </button>
  </div>
  <div
    v-if="error"
    class="alert alert-danger d-flex align-items-center"
    role="alert"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="currentColor"
      class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2"
      viewBox="0 0 16 16"
      role="img"
      aria-label="Warning:"
    >
      <path
        d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"
      />
    </svg>
    <div>Erreur : {{ error }}</div>
  </div>
</template>

<style>
.question {
  display: flex;
  justify-content: center;
}
</style>
