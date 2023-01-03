<script setup>

import { useRoute } from 'vue-router';
import QuizApiService from '../services/QuizApiService';
import QuestionAdminDisplay from '../components/QuestionAdminDisplay.vue';

const route = useRoute();
const position = route.query.p


</script>

<template>
  <div class="about">
    <h1>Question Admin</h1>
    <Suspense>
      <QuestionAdminDisplay position="1"></QuestionAdminDisplay>
    </Suspense>
    <button>Modifier</button>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
