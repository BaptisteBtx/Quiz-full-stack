<script setup>

import quizApiService from '../services/QuizApiService';

//props
const props = defineProps({
  position: String
})


const emits = defineEmits(["answer-selected"])

let position = props.position

// Export default : remplacé par script setup
let question = await quizApiService.getQuestion(position)

function emitNewQuestion(titleInput, textInput, possibleAnswerSelected, imgSelected) {
  let answer = {
    title: titleInput,
    text: textInput,
    possibleAnswer: possibleAnswerSelected,
    img: imgSelected,

  }
  emits('answer-selected', answer)
}

let currentQuestion = {
  questionId: question.data.id,
  questionTitle: question.data.title,
  questionDescription: question.data.text,
  possibleAnswers: question.data.possibleAnswers,
  image: question.data.image
}

</script>

<template>
  <div class="question">
    <h5> {{ currentQuestion.questionTitle }}</h5>
    <img v-if="currentQuestion.image" :src="currentQuestion.image" />


    <p> {{ currentQuestion.questionDescription }}</p>

    <div @click="emitNewQuestion()" v-for="(answer, index) in currentQuestion.possibleAnswers" v-bind:key="answer.text">
      <a>
        {{ index }} - {{ answer.text }}
      </a>
    </div>
  </div>
</template>
  
<style>

</style>
  