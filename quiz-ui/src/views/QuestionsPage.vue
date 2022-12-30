<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionsManagerVue from '../components/QuestionsManager.vue';
import { useRouter } from 'vue-router';
const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())

//Validation des réponses



// Export default : remplacé par script setup
</script>

<template>
  <div class="questions_page">
    <h1>Quiz</h1>
    <QuestionsManagerVue></QuestionsManagerVue>
  </div>
</template>
  
<style>

</style>
  