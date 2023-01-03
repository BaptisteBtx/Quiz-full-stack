<script setup>
// const quiz = ref(null)

//props
const props = defineProps({
  question: Object,
});

const emits = defineEmits(["answer-selected"]);

const currentQuestion = props.question;

</script>

<template>
  <div class="question">
    <h5>{{ currentQuestion.title }}</h5>
    <img v-if="currentQuestion.image" :src="currentQuestion.image" />

    <p>{{ currentQuestion.description }}</p>

    <div class="form-check" name="radioAnswer" v-for="(answer, index) in currentQuestion.possibleAnswers">
      <input
        class="form-check-input"
        name="radioAnswer"
        type="radio"
        :id="index"
        @click="$emit('answer-selected', index)"
      />
      <label class="form-check-label" :for="index">
        {{ answer.text }}
      </label>
    </div>

    <!-- <div
      @click="$emit('answer-selected', index)"
      v-for="(answer, index) in currentQuestion.possibleAnswers"
      v-bind:key="answer.text"
    >
      <a> {{ index }} - {{ answer.text }} </a>
    </div> -->
  </div>
</template>

<style></style>
