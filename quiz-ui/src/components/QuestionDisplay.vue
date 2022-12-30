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
    <p>{{ currentQuestion.questionTitle }}</p>
    <a @click="$emit('answer-selected', 2)">{{ currentQuestion.questionDescription }}</a>
    <!-- <img v-if="question.image" :src="question.image" /> -->
  </div>
</template>
  
<style>

</style>
  