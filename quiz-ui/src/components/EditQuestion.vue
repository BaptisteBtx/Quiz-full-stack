<script setup>
import { ref } from 'vue'

import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService'
//props
const props = defineProps({
  question:Object,
  isNew:Boolean
});
console.log("question : ",props.question)
console.log("new = ",props.isNew)

const baseQuestion = ref(props.question)
const editedQuestion = ref(Object())
if (baseQuestion.value) editedQuestion.value = baseQuestion.value


const token = ref(participationStorageService.getToken())


function selectGoodAnswer(index){
  for (let i = 0; i < editedQuestion.value.possibleAnswers.length; i++) {
    editedQuestion.value.possibleAnswers[i].isCorrect = i==index
  }
  console.log(editedQuestion.value.possibleAnswers)
}

function handleImage(e) {
  const selectedImage = e.target.files[0]; // get first file
  createBase64Image(selectedImage);
}
function createBase64Image(fileObject) {
  const reader = new FileReader();

  reader.onload = (e) => {
    const image = e.target.result;
    console.log(image)
    editedQuestion.value.image = image
    // this.uploadImage();
  };
  reader.readAsDataURL(fileObject);
}



</script>

<template>
  <div>
    <div class="input-group mb-3">
      <span class="input-group-text">Titre</span>
      <input v-model="editedQuestion.title" type="text" class="form-control">
    </div>
    <div class="container image-editing">
      <!-- Image preview -->
      <img class="img-responsive" style="width:30em" v-if="editedQuestion.image" :src="editedQuestion.image" />
      <!-- Image Upload -->
      <div class="container mt-10">
        <div class="card bg-white">
          <input @change="handleImage" class="custom-input" type="file" accept="image/*">
        </div>
      </div>
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">Question</span>
      <input v-model="editedQuestion.text" type="text" class="form-control">
    </div>
    <div class="input-group mb-3">
      <span class="input-group-text">Position</span>
      <input v-model="editedQuestion.position" type="number" class="form-control" placeholder="Position dans le quiz">
    </div>
    <!-- Radios -->
    <div class="input-group" v-for="(answer, index) in editedQuestion.possibleAnswers"> 
      <div class="input-group-text">
        <input class="form-check-input mt-0" type="radio" name="radioAnswer" @click="selectGoodAnswer(index)">
      </div>
      <input v-model="editedQuestion.possibleAnswers[index].text" type="text" class="form-control" :placeholder="'Réponse '+(index+1)">
    </div>

  </div>
  <div class="d-flex justify-content-center" style="margin-top: 10px;">
    <div class="btn-group" role="group">
      <button class="btn btn-warning" @click="$emit('cancel-editing')">Annuler</button>
      <button class="btn btn-success" @click="$emit('save-question', editedQuestion, token)">
        <span v-if="baseQuestion">Enregistrer les modifications</span>
        <span v-else>Ajouter la question</span>
      </button>
    </div>
    
  </div>

</template>

<style>

</style>
