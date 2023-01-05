<script setup>

import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService'
//props
const props = defineProps({
  position: Number,
  addQ: Boolean
});
let question
let currentQuestion

if (props.position === -1) {
  question = undefined
  currentQuestion = {
    image: undefined,
    description: "Description",
    title: "Titre",
    possibleAnswers: [{
      text: "0",
      isCorrect: true,
    }, {
      text: "1",
      isCorrect: false,
    }, {
      text: "2",
      isCorrect: false,
    }, {
      text: "3",
      isCorrect: false,
    }],
    position: 10
  }
}
else {
  question = await quizApiService.getQuestion(props.position)
  currentQuestion = {
    image: question.data.image,
    description: question.data.text,
    title: question.data.title,
    possibleAnswers: question.data.possibleAnswers,
    position: question.data.position,
    id: question.data.id
  }
}

let token = participationStorageService.getToken()
let addQ = props.addQ
let index = 0

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

    <div v-if="addQ" class="m-1">
      <button class="btn btn-success" @click="$emit('question-add', currentQuestion, token)">Créer question</button>
    </div>
    <div v-else>

      <button class="btn btn-success m-1" @click="$emit('question-saved', currentQuestion, token)">Enregistrer les
        modifications</button>
    </div>


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
