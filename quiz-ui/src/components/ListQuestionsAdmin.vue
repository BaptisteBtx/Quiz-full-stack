<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import QuestionsList from './QuestionsList.vue';


const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
//let info = await quizApiService.getQuizInfo()
//console.log(info)

// Launch quiz 
async function returnHome() {
  router.push('/')
}

async function updateQuestion(number) {
  router.push('/admin?position=' + number)
}

// Export default : remplacé par script setup

</script>

<template>
  <div class="d-flex w-80 flex-column justify-content-center align-items-center">
    <h5>Liste de questions :</h5>
    <Suspense>
      <QuestionsList :update-question="updateQuestion"></QuestionsList>
    </Suspense>

    <button type="button" class="btn btn-success w-25" @click="returnHome">Home</button>
  </div>
</template>
  
<style>

</style>
  