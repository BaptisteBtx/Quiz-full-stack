<script setup>
import { ref } from "vue";
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";

const questions = ref(null);

try {
  questions.value = await quizApiService.getAllQuestions().then((d) => d.data);
} catch (error) {
  console.log(error);
}

const quizAvailable = ref(false);
const token = participationStorageService.getToken();
const props = defineProps({
  updateQuestion: Function,
  deleteQuestion: Function,
});

const updateQuestion = props.updateQuestion;
const deleteQuestion = props.deleteQuestion;

if (questions.value) {
  quizAvailable.value = true;
}
</script>

<template>
  <div>
    <h5>Liste de questions :</h5>
    <div
      v-if="quizAvailable"
      v-for="q in questions"
      v-bind:key="q.id"
      class="question-wrapper"
    >
      <div
        class="d-flex justify-content-between align-items-center input-group"
      >
        <p>
          <strong>{{ q.title }}</strong> <br />
          {{ q.text }}
        </p>
        <div class="btn-group" role="group">
          <button
            type="button"
            class="btn btn-success"
            @click="updateQuestion(q)"
          >
            Modifier
          </button>
          <button
            type="button"
            class="btn btn-danger"
            @click="deleteQuestion(q, token)"
          >
            Supprimer
          </button>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </div>
</template>

<style>
.question-wrapper {
  border: solid 1px rgba(0, 0, 0, 0.1);
  padding: 10px;
}
</style>
