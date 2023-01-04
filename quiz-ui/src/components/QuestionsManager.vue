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
const quizInfo = ref(null)
const username = ref(ParticipationStorageService.getPlayerName())
const questions = ref(null)

const questionLoaded = ref(false)

try {
  quizInfo.value = await quizApiService.getQuizInfo();
  questions.value = await quizApiService.getAllQuestions(); // Charge question 1 au lancement
} catch (error) {
  console.log(error)
  router.push("/"); // TODO : Page d'erreur
}


const totalQuestionNumber = quizInfo.value.data.size;

const question = ref(questions.value[0])

const selectedAnswers = ref([]);
const selectedAnswer = ref(null)

async function loadNextQuestion() {
  selectedAnswers.value.push(selectedAnswer.value)
  if (question.value.position >= totalQuestionNumber) {
    endQuiz();
  } else {
    question.value = questions.value[question.value.position]
    console.log(selectedAnswers.value)
    // index de la question suivante = index courant + 1 = position courante
  }
  selectedAnswer.value = null

}

async function endQuiz() {
  try {
    const participation = await QuizApiService.saveParticipation(username.value, selectedAnswers.value)
    const score = participation.score
    ParticipationStorageService.saveParticipationScore(username, score)
  } catch (error) {
    console.log(error)
  }
  
  router.push("/");
}

function setSelectedAnswer(index) {
  selectedAnswer.value = index+1
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
    <br>
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


  <div class="toast-container position-fixed bottom-0 end-0 p-3" v-if="error">
    <div
      id="liveToast"
      class="toast"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-header">
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="toast"
          aria-label="Close"
        ></button>
      <div class="toast-body">Hello, world! This is a toast message.</div>
    </div>
  </div>
  
  </div>
</template>

<style>
.question {
  display: flex;
  justify-content: center;
}
</style>
