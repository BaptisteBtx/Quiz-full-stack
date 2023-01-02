<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from './QuestionDisplay.vue'
import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

let currentQuestionPosition = 1
let question = await quizApiService.getQuestion(currentQuestionPosition)
let quizInfo = await quizApiService.getQuizInfo()

let currentQuestion = {
  questionId: question.data.id,
  questionTitle: question.data.title,
  questionDescription: question.data.text,
  possibleAnswers: question.data.possibleAnswers,
  image: question.data.image
}


let selectedAnswer = 0
const totalQuestionNumber = quizInfo.data.size

// Chargé la question en fonction de la position
async function loadQuestionByPosition() {



  if (currentQuestionPosition > totalQuestionNumber) { endQuiz() }
  else {
    //TO DO : Sauvegarder la réponse selectedAnswer
    currentQuestionPosition += 1

    console.log('Chargement question ' + currentQuestionPosition)

    let question = await quizApiService.getQuestion(currentQuestionPosition)
    console.log(question)

    /* currentQuestion = {
      questionId: question.data.id,
      questionTitle: question.data.title,
      questionDescription: question.data.text,
      possibleAnswers: question.data.possibleAnswers,
      image: question.data.image
    } */
  }
}

function answerClickHandler(answerNumber) {
  selectedAnswer = answerNumber
  console.log('Réponse actuelle ', selectedAnswer)
  //TO DO
}

async function endQuiz() {
  router.push('/');
}


// Export default : remplacé par script setup

</script>

<template>
  <div class="question_manager">
    <h1>Question : {{ currentQuestion.questionId }} / {{ totalQuestionNumber }}</h1>
    <QuestionDisplay :question="{ currentQuestion }" @answer-selected="answerClickHandler"></QuestionDisplay>
    <button type="button" class="btn btn-success" @click="loadQuestionByPosition">Suivant</button>
  </div>
</template>
  
<style>

</style>
  