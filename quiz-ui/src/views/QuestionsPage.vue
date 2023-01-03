
<!-- 
  Cette page affiche le quiz : une question (Question Manager) par question
 -->

<script setup>
import { ref, watchEffect } from 'vue'
import participationStorageService from "@/services/ParticipationStorageService";
import QuestionsManager from '../components/QuestionsManager.vue';
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
    <Suspense>
      <QuestionsManager></QuestionsManager>
    </Suspense>
  </div>
</template>
  
<style>

</style>
  