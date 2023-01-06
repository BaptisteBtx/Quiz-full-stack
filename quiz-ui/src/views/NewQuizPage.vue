<script setup>
import { ref } from "vue";
import participationStorageService from "@/services/ParticipationStorageService";

import { useRouter } from "vue-router";
const router = useRouter();

// Variable formulaire
const username = ref(participationStorageService.getPlayerName());

// Launch quiz
function launchNewQuiz() {
  participationStorageService.savePlayerName(username.value);
  console.log("Lauch quiz with username : ", username.value);
  // Push route :
  router.push("/questions");
}
</script>

<template>
  <div class="new_quiz_form">
    <h1>Entrez votre nom afin de commencer un quiz :</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="form-username">Username</span>
      <input
        type="text"
        class="form-control"
        placeholder="Username"
        aria-label="Username"
        aria-describedby="form-username"
        v-model="username"
      />
    </div>
    <button type="button" class="btn btn-success" @click="launchNewQuiz">
      GO
    </button>
  </div>
</template>

<style></style>
