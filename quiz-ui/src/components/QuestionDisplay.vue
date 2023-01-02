<script setup>

// const quiz = ref(null)

//props
const props = defineProps({
  question: Object
})

const emits = defineEmits(["answer-selected"])

let currentQuestion = props.question.currentQuestion
console.log(currentQuestion)
// Export default : remplacé par script setup


</script>

<template>
  <div class="question">
    <h5> {{ currentQuestion.questionTitle }}</h5>
    <img v-if="currentQuestion.image" :src="currentQuestion.image" />


    <p> {{ currentQuestion.questionDescription }}</p>

    <div @click="$emit('answer-selected', index)" v-for="(answer, index) in currentQuestion.possibleAnswers"
      v-bind:key="answer.text">
      <a>
        {{ index }} - {{ answer.text }}
      </a>
    </div>
  </div>
</template>
  
<style>

</style>
  