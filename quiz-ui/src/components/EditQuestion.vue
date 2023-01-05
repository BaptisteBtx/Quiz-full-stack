<script setup>

import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService'
//props
const props = defineProps({
  position: Number,
});

let question = await quizApiService.getQuestion(props.position)
let token = participationStorageService.getToken()
console.log(token)
let index = 0

const currentQuestion = {
  image: question.data.image,
  description: question.data.text,
  title: question.data.title,
  possibleAnswers: question.data.possibleAnswers,
  position: question.data.position,
  id: question.data.id
}
//const emits = defineEmits(["answer-selected"]);

function answerSelected(number) {
  console.log(number)
  if (number) {
    index = number
  }
}

</script>

<template>
  <div class="container d-flex justify-content-center align-items-center flex-column ">
    <h5>Editing question {{ props.position }}</h5>

    <div class="container image-editing">
      <img class="img-responsive" style="width:30em" v-if="currentQuestion.image" :src="currentQuestion.image" />
    </div>

    <div class="title-editing d-flex justify-content-left aling-items-center p-2 w-100">
      <input class="w-100" type="text" aria-label="Title" aria-describedby="form-title"
        v-model="currentQuestion.title" />
    </div>

    <div class="desc-editing d-flex justify-content-left aling-items-center p-2 w-100">
      <input class="w-100" type="text" aria-label="Description" aria-describedby="form-title"
        v-model="currentQuestion.description" />
    </div>

    <div class="desc-editing d-flex justify-content-left aling-items-center p-2 w-100">
      <input class="w-100" type="text" aria-label="Position" aria-describedby="form-title"
        v-model="currentQuestion.position" />
    </div>

    <div class="form-check d-flex justify-content-center align-items-center" name="radioAnswer"
      v-for="(answer, index) in currentQuestion.possibleAnswers">
      <input class="form-check-input" name="radioAnswer" type="radio" :id="index" @click="answerSelected(index)" />
      <label class="form-check-label w-100" :for="index">
        <div class="title-editing d-flex justify-content-left aling-items-center p-2 w-100">
          <input class="w-100" type="text" aria-label="answer" v-model="answer.text" />
        </div>
      </label>
    </div>


    <button class="btn btn-success" @click="$emit('question-saved', currentQuestion, token)">Enregistrer les
      modifications</button>

    <!-- <div
      @click="$emit('answer-selected', index)"
      v-for="(answer, index) in currentQuestion.possibleAnswers"
      v-bind:key="answer.text"
    >
a>
  >-->
  </div>
</template>

<style>

</style>
