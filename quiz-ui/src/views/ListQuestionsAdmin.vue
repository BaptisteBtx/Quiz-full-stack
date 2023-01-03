<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import QuestionsList from '../components/QuestionsList.vue';


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
  router.push('/question_admin?p=' + number)
}

// Export default : remplacé par script setup

</script>

<template>
  <div>
    <h1>Liste de questions :</h1>
    <Suspense>
      <QuestionsList :update-question="updateQuestion"></QuestionsList>
    </Suspense>

    <button type="button" class="btn btn-success" @click="returnHome">Home</button>
  </div>
</template>
  
<style>

</style>
  