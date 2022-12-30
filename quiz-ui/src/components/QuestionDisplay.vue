<script setup>

// const quiz = ref(null)

//props
const props = defineProps({
  question: Object
})


console.log(props.question)
// Export default : remplacé par script setup

</script>

<template>
  <div class="question">
    <!-- <img v-if="question.image" :src="question.image" /> -->
  </div>
</template>
  
<style>

</style>
  