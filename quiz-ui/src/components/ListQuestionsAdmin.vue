<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import EditQuestion from './EditQuestion.vue';
import QuestionsList from './QuestionsList.vue';


const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const question = ref(undefined)
const questionUpdate = ref(false)

//let info = await quizApiService.getQuizInfo()
//console.log(info)

// Launch quiz 
async function returnHome() {
  router.push('/')
}

async function updateQuestion(number) {

  if (number) {
    console.log("number: ", number)
    question.value = number
  }
  else {
    console.log("no number")
    question.value = undefined
  }
  verifyQuestion()
}

function verifyQuestion() {
  console.log("verifyQuestion")
  if (question.value) {
    questionUpdate.value = true
  } else {
    questionUpdate.value = false
  }
  return questionUpdate.value
}

// Export default : remplacé par script setup

</script>

<template>
  <div class="d-flex w-80 flex-column justify-content-center align-items-center">
    <h5>Liste de questions :</h5>
    <Suspense>
      <div v-if="!verifyQuestion()">
        <QuestionsList :update-question="updateQuestion"></QuestionsList>
      </div>
      <div v-else>
        <EditQuestion :position="question">

        </EditQuestion>
        <button class="btn btn-success" @click="updateQuestion(undefined)">Enregistrer les modifications</button>
      </div>
    </Suspense>
    <button type="button" class="btn btn-success w-25" @click="returnHome">Home</button>
  </div>
</template>
  
<style>

</style>
  