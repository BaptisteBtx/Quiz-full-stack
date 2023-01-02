<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';


const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

// Launch quiz 
async function returnHome() {
  router.push('/')
}

// Export default : remplacé par script setup

</script>

<template>
  <div>
    <h1>Liste de questions :
    </h1>
    <button type="button" class="btn btn-success" @click="returnHome">Home</button>
  </div>
</template>
  
<style>

</style>
  