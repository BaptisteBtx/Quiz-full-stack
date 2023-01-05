<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService';
import EditQuestion from './EditQuestion.vue';
import QuestionsList from './QuestionsList.vue';


const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const question = ref(undefined)
const questionUpdate = ref(false)
let quizInfo = ref(await quizApiService.getQuizInfo())

let addQ = ref(false)
console.log(quizInfo)
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



function saveQuestion(newQuestion, token) {
  updateQuestion(undefined)
  console.log("question saved : ", newQuestion, token)
  quizApiService.saveQuestion(newQuestion, token)
}

async function deleteQuestion(newQuestion, token) {


  quizInfo.value = await quizApiService.getQuizInfo()

  console.log("question deleted : ", newQuestion)
  await quizApiService.deleteQuestion(newQuestion, token)
  updateQuestion(undefined)
}

async function addQuestion(newQuestion, token) {
  console.log("addQestion : ", newQuestion)
  quizApiService.addQuestion(newQuestion, token)
}

function createQuestion() {
  addQ.value = true
  updateQuestion(-1)
}

// Export default : remplacé par script setup

</script>

<template>
  <div class="d-flex w-80 flex-column justify-content-center align-items-center">
    <h5>Liste de questions :</h5>
    <Suspense>
      <div v-if="!verifyQuestion()">
        <QuestionsList :delete-question="deleteQuestion" :update-question="updateQuestion"></QuestionsList>
        <button type="button" class="btn btn-success w-25" @click="createQuestion">Créer Question</button>
      </div>
      <div v-else>
        <EditQuestion @question-saved="saveQuestion" @question-add="addQuestion" :addQ="addQ" :position="question">

        </EditQuestion>
      </div>
    </Suspense>
    <button type="button" class="btn btn-success w-25" @click="returnHome">Home</button>

  </div>
</template>
  
<style>

</style>
  