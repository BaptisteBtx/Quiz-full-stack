<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router';
import QuestionDisplay from './QuestionDisplay.vue'

const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

let quizInfo = await quizApiService.getQuizInfo()
let questions = Array(10)
let quizAvailable = ref(false)
const props = defineProps({
  updateQuestion: Function
})

const totalQuestionNumber = quizInfo.data.size
let updateQuestion = props.updateQuestion
console.log(updateQuestion(0))
loadQuiz()
// Chargé la question en fonction de la position
async function loadQuestionByPosition() {



}

async function loadQuiz() {

  for (let i = 0; i < totalQuestionNumber; i += 1) {
    let question = await quizApiService.getQuestion(i + 1)
    questions[i] = question.data
  }
  quizAvailable.value = true
}





// Export default : remplacé par script setup

</script>

<template>
  <div>

    <div v-if="quizAvailable === true" v-for="q in questions" v-bind:key="q.id">
      <div class="d-flex justify-content-between align-items-center input-group mb-2">
        {{ q.title }} - {{ q.text }}
        <button type="button" class="btn btn-success" @click="updateQuestion(q.id)">Modifier</button>
      </div>
    </div>
    <div v-else>
      <p>Loading</p>
    </div>
  </div>
</template>
  
<style>

</style>
  