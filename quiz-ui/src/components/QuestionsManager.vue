<script setup>
import { ref } from "vue";
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

try {
  quizInfo.value = await quizApiService.getQuizInfo().then((d) => d.data);
  questions.value = await quizApiService.getAllQuestions().then((d) => d.data); // Charge toutes les questions au lancement
} catch (e) {
  console.log("erreur : ",e);
  error.value = e;
}

const totalQuestionNumber = quizInfo.value.size;

const question = ref(questions.value[0]);

const selectedAnswers = ref([]);
const selectedAnswer = ref(null);

function loadNextQuestion() {
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
    ).then((d) => d.data);
    const score = participation.score;
    ParticipationStorageService.saveParticipationScore(score);
  } catch (e) {
    console.log(e);
    error.value = e;
  }

  router.push("/score");
}

function setSelectedAnswer(index) {
  selectedAnswer.value = index + 1;
}
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
    <div class="d-flex justify-content-center flex-column align-items-center">
      <p v-if="selectedAnswer">Réponse choisie : n°{{ selectedAnswer }}</p>
      <p v-else>Choisissez une réponse.</p>
      <button
        type="button"
        class="btn btn-success"
        @click="loadNextQuestion"
        :disabled="!selectedAnswer"
        style="width: 150px;"
      >
        Suivant
      </button>
    </div>
    
  </div>
</template>

<style>
.question {
  display: flex;
  justify-content: center;
}
</style>
