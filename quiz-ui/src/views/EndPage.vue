<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";

import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const score = ref(participationStorageService.getParticipationScore())

// Launch quiz 
async function returnHome() {
  router.push('/')
}

// Export default : remplacé par script setup

</script>

<template>
  <div>
    <h5>Thanks for playing {{ username.value }}, you're score has been updated !</h5>
    <button type="button" class="btn btn-success" @click="returnHome">GO</button>
  </div>
</template>
  
<style>

</style>
  