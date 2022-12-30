<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";

import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

//Validation des réponses
async function validateAnswer() {
  //TO DO
  console.log('Réponse validée pour ' + username.value)
}


// Export default : remplacé par script setup
</script>

<template>
  <div class="questions_page">
    <h1>Quiz</h1>
    <button type="button" class="btn btn-success" @click="validateAnswer">Valider</button>
  </div>
</template>
  
<style>

</style>
  