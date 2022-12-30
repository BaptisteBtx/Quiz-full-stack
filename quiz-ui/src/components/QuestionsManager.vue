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
  questionTitle: '',
  questionDescription: '',
  possibleAnswers: [],
}

let currentQuestionPosition = 1

// Chargé la question en fonction de la position
async function loadQuestionByPosition() {
  console.log('Chargement question ' + currentQuestionPosition)
  //TO DO
}

async function answerClickHandler() {
  console.log('Question validée')
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
    <QuestionDisplay :question="{ currentQuestion }"></QuestionDisplay>
    <button type="button" class="btn btn-success" @click="answerClickHandler">Valider</button>
  </div>
</template>
  
<style>

</style>
  