<script setup>
const props = defineProps({
  question: Object,
});

const emits = defineEmits(["answer-selected"]);

const currentQuestion = props.question;
</script>

<template>
  <div class="card d-flex align-items-center">
    <div class="img-wrapper">
      <img
        v-if="currentQuestion.image"
        :src="currentQuestion.image"
        class="card-img-top img-responsive"
        style="object-fit: contain"
      />
    </div>
    
    <div class="card-body">
      <h5 class="card-title">{{ currentQuestion.title }}</h5>
      <p class="card-text">{{ currentQuestion.text }}</p>
    </div>
    <ul class="list-group list-group-flush">
      <li
        class="list-group-item"
        v-for="(answer, index) in currentQuestion.possibleAnswers"
      >
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
      </li>
    </ul>
  </div>
</template>

<style>
label {
  padding-left: 10px;
}
.card {
  width: 66%;
  max-width: 700px;
  /* max-height: 700px; */
}
</style>
