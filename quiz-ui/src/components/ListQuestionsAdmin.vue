<script setup>
import { ref } from "vue";
import ParticipationStorageService from "../services/ParticipationStorageService";
import quizApiService from "../services/QuizApiService";
import EditQuestion from "./EditQuestion.vue";
import QuestionsList from "./QuestionsList.vue";

const editingQuestion = ref(false);
const question = ref(null);

function updateQuestion(qst) {
  question.value = qst;
  editingQuestion.value = true;
  console.log("Update : ", question);
}
function createQuestion() {
  console.log("Create new question");
  editingQuestion.value = true;
}
function cancelEditing() {
  editingQuestion.value = false;
  question.value = null;
}

async function deleteQuestion(question, token) {
  console.log("Delete : ", question);
  try {
    await quizApiService.deleteQuestion(question, token);
    // reload questions
    forceListUpdate();
  } catch (error) {
    console.log(error);
    ParticipationStorageService.disconnect()
    throw(error)
  }
}
async function saveQuestion(editedQuestion, newQst, token) {
  console.log("Save : ", editedQuestion);
  // API
  try {
    if (newQst) await quizApiService.saveQuestion(editedQuestion, token);
    else await quizApiService.addQuestion(editedQuestion, token);
    cancelEditing();
  } catch (error) {
    console.log(error);
    ParticipationStorageService.disconnect()
    throw(error)
  }
}
// Pour recharger QuestionList
const questionsListKey = ref(0);
function forceListUpdate() {
  questionsListKey.value++;
}
</script>

<template>
  <div
    class="d-flex w-80 flex-column justify-content-center align-items-center"
  >
    <Suspense>
      <div v-if="editingQuestion">
        <EditQuestion
          @save-question="saveQuestion"
          @cancel-editing="cancelEditing"
          :question="question"
        ></EditQuestion>
      </div>
      <div v-else>
        <QuestionsList
          :delete-question="deleteQuestion"
          :update-question="updateQuestion"
          :key="questionsListKey"
        ></QuestionsList>
        <div class="d-flex justify-content-center">
          <button
            type="button"
            class="btn btn-success w-25"
            @click="createQuestion"
          >
            Créer une question
          </button>
        </div>
      </div>
    </Suspense>
  </div>
</template>

<style></style>
