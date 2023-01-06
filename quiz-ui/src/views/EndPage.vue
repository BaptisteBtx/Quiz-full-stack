<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";

import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const score = ref(participationStorageService.getParticipationScore())
console.log("score base : ",score.value)

// Launch quiz 
async function returnHome() {
  router.push('/')
}

</script>

<template>
  <div>
    <h5>Score : {{ score }}</h5>
    <h5>Merci d'avoir joué {{ username }}, ton score a bien été enregistré !</h5>
    <button type="button" class="btn btn-success" @click="returnHome">Retourner à l'accueil</button>
  </div>
</template>
  
<style>

</style>
  