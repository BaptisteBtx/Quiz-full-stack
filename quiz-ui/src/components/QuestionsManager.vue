<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionDisplay from './QuestionDisplay.vue'
import quizApiService from "@/services/QuizApiService";
import { useRouter } from 'vue-router';
import QuizApiService from '../services/QuizApiService';
import ParticipationStorageService from '../services/ParticipationStorageService';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

let currentQuestionPosition = ref(1)
let question = await quizApiService.getQuestion(currentQuestionPosition.value)
let quizInfo = await quizApiService.getQuizInfo()

let currentQuestion = {
  questionId: question.data.id,
  questionTitle: question.data.title,
  questionDescription: question.data.text,
  possibleAnswers: question.data.possibleAnswers,
  image: question.data.image
}



const totalQuestionNumber = quizInfo.data.size
let selectedAnswer = Array(totalQuestionNumber)

// Chargé la question en fonction de la position
async function loadQuestionByPosition() {



  if (currentQuestionPosition.value + 1 > totalQuestionNumber) { endQuiz() }
  else {
    //TO DO : Sauvegarder la réponse selectedAnswer

    let question = await quizApiService.getQuestion(currentQuestionPosition.value + 1)

    //TO DO : Indiquer à l'utilisateur qu'il doit entrer une réponse
    if (selectedAnswer[currentQuestionPosition.value - 1] === undefined) {
      //selectedAnswer[currentQuestionPosition.value - 1] = -1
      console.log("Veuillez entrer une réponse !")
      return
    }
    //TO DO : Gérer le cas de la question non disponible
    if (question === undefined) {
      selectedAnswer[currentQuestionPosition.value] = -1
      currentQuestionPosition.value += 1
      await loadQuestionByPosition()
      return
    }
    console.log(currentQuestionPosition.value)


    currentQuestion = {
      questionId: question.data.id + 1,
      questionTitle: question.data.title,
      questionDescription: question.data.text,
      possibleAnswers: question.data.possibleAnswers,
      image: question.data.image
    }

    currentQuestionPosition.value += 1

  }
}

function answerClickHandler(answerNumber) {

  selectedAnswer[currentQuestionPosition.value - 1] = answerNumber
  console.log('Réponse actuelle ', selectedAnswer)
  //TO DO
}

async function endQuiz() {

  //let score = await QuizApiService.getParticipationScore("Bob", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
  //ParticipationStorageService.saveParticipationScore(35)

  router.push('/');
}


// Export default : remplacé par script setup

</script>

<template>
  <div class="question_manager">
    <h1>Question : {{ currentQuestion.questionId }} / {{ totalQuestionNumber }}</h1>
    <QuestionDisplay :key="currentQuestionPosition" :question="{ currentQuestion }"
      @answer-selected="answerClickHandler"></QuestionDisplay>
    <button type="button" class="btn btn-success" @click="loadQuestionByPosition">Suivant</button>
  </div>
</template>
  
<style>

</style>
  