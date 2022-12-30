<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from './QuestionDisplay.vue'
import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

let currentQuestion = {
  questionTitle: 'Titre de la question',
  questionDescription: 'Description de la question',
  possibleAnswers: ['Réponse A', 'Réponse B', 'Réponse C']
}

let currentQuestionPosition = 1
let selectedAnswer = 0

// Chargé la question en fonction de la position
async function loadQuestionByPosition() {

  //TO DO : Implémenter le nombre total de question
  //if(currentQuestionPosition===totalQuestionNumber){endQuiz()}

  //TO DO : Sauvegarder la réponse selectedAnswer
  currentQuestionPosition += 1
  console.log('Chargement question ' + currentQuestionPosition)
  //TO DO : Changer de question
}

async function answerClickHandler(answerNumber) {
  selectedAnswer = answerNumber
  console.log('Réponse actuelle ', selectedAnswer)
  //TO DO
}

async function endQuiz() {
  router.push('/');
}

//props


// Export default : remplacé par script setup

</script>

<template>
  <div class="question_manager">
    <h3>Question {{ currentQuestionPosition }}</h3>
    <QuestionDisplay :question="{ currentQuestion }" @answer-selected="answerClickHandler"></QuestionDisplay>
    <button type="button" class="btn btn-success" @click="loadQuestionByPosition">Valider</button>
  </div>
</template>
  
<style>

</style>
  