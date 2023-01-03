<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router';

const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

let quizInfo = await quizApiService.getQuizInfo()
let questions = Array(10)


const totalQuestionNumber = quizInfo.data.size
console.log(quizInfo.data, totalQuestionNumber)
for (let i = 0; i < totalQuestionNumber; i += 1) {
  let question = await quizApiService.getQuestion(i + 1)
  questions[i] = question.data
}
console.log(questions)
// Chargé la question en fonction de la position
async function loadQuestionByPosition() {



}



function answerClickHandler(answerNumber) {

  //Charger la page de question
  //TO DO
}



// Export default : remplacé par script setup

</script>

<template>
  <div>
    <p>QuestionsList</p>
    <div v-for="q in questions" v-bind:key="q.id">
      {{ q.title }} - {{ q.text }}
    </div>
  </div>
</template>
  
<style>

</style>
  