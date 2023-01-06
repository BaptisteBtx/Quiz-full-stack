<script setup>
import { ref } from "vue";

import participationStorageService from "../services/ParticipationStorageService";
import quizApiService from "../services/QuizApiService";

const error = ref(null)
//props
const props = defineProps({
  question: Object,
});

const quizInfo = ref(null)
try {
  quizInfo.value = await quizApiService.getQuizInfo().then((d) => d.data)
} catch (e) {
  console.log(e)
  error.value = e
}


const baseQuestion = ref(props.question);
const editedQuestion = ref({
  title: "",
  text: "",
  possibleAnswers: [],
  position: quizInfo.value.size + 1,
  image: "",
});
if (baseQuestion.value) editedQuestion.value = baseQuestion.value;

const token = ref(participationStorageService.getToken());

function selectGoodAnswer(index) {
  for (let i = 0; i < editedQuestion.value.possibleAnswers.length; i++) {
    editedQuestion.value.possibleAnswers[i].isCorrect = i == index;
  }
  console.log(editedQuestion.value.possibleAnswers);
}

function addAnswer() {
  editedQuestion.value.possibleAnswers.push({ text: "", isCorrect: false });
}

function isGoodAnswer(index) {
  return editedQuestion.value.possibleAnswers[index].isCorrect;
}

// Image :

function handleImage(e) {
  const selectedImage = e.target.files[0];
  createBase64Image(selectedImage);
}
function createBase64Image(fileObject) {
  const reader = new FileReader();

  reader.onload = (e) => {
    const image = e.target.result;
    editedQuestion.value.image = image;
  };
  reader.readAsDataURL(fileObject);
}
</script>

<template>
  <div>
    <h5>Editeur de questions :</h5>
    <div class="input-group mb-3">
      <span class="input-group-text">Titre</span>
      <input v-model="editedQuestion.title" type="text" class="form-control" />
    </div>
    <div class="container image-editing">
      <p>Prévisualisation image :</p>
      <!-- Image preview -->
      <img
        class="img-responsive"
        style="width: 30em"
        v-if="editedQuestion.image"
        :src="editedQuestion.image"
      />
      <p v-else>Pas d'image</p>
      <!-- Image Upload -->
      <div class="container mt-10">
        <div id="img-input" class="card bg-white w-100">
          <input @change="handleImage" type="file" accept="image/*" />
        </div>
      </div>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">Question</span>
      <input v-model="editedQuestion.text" type="text" class="form-control" />
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">Position</span>
      <input
        v-model="editedQuestion.position"
        type="number"
        class="form-control"
        placeholder="Position dans le quiz"
      />
    </div>
    <!-- Radios -->
    <div
      class="input-group"
      v-for="(answer, index) in editedQuestion.possibleAnswers"
    >
      <div class="input-group-text">
        <input
          class="form-check-input mt-0"
          type="radio"
          name="radioAnswer"
          @click="selectGoodAnswer(index)"
          :checked="isGoodAnswer(index)"
        />
      </div>
      <input
        v-model="editedQuestion.possibleAnswers[index].text"
        type="text"
        class="form-control"
        :placeholder="'Réponse ' + (index + 1)"
      />
    </div>
    <button class="btn btn-primary" @click="addAnswer">Ajouter réponse</button>
  </div>
  <div class="d-flex justify-content-center" style="margin-top: 10px">
    <div class="btn-group" role="group">
      <button class="btn btn-warning" @click="$emit('cancel-editing')">
        Annuler
      </button>
      <button
        class="btn btn-success"
        @click="
          $emit('save-question', editedQuestion, Boolean(baseQuestion), token)
        "
      >
        <span v-if="baseQuestion">Enregistrer les modifications</span>
        <span v-else>Ajouter la question</span>
      </button>
    </div>
  </div>
</template>

<style>
#img-input {
  margin: 15px;
  margin-top: 0;
}
</style>
