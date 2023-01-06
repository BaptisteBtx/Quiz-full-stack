<!-- 
  Cette page affiche le quiz : une question (Question Manager) par question
 -->

<script setup>
import QuestionsManager from "../components/QuestionsManager.vue";

</script>

<template>
  <div class="questions_page">
    <Suspense>
      <QuestionsManager></QuestionsManager>
    </Suspense>
  </div>
</template>

<style></style>
