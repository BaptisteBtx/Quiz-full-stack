<script setup>
import { ref } from "vue";

import LoginComponent from "../components/LoginComponent.vue";
import ListQuestionsAdmin from "../components/ListQuestionsAdmin.vue";

const position = ref(0);

//Récupération du token dans le sessionStorage
const token = ref(window.sessionStorage.getItem("token"));

function updateQuestion(positions) {
  if (positions !== 0) {
    position.value = positions;
  } else {
    position.value = 0;
  }
}

function setToken(newToken) {
  token.value = newToken;
}
</script>

<template>
  <div class="container">
    <h1>Admininistration</h1>
    <LoginComponent @token="setToken"></LoginComponent>

    <div v-if="token">
      <Suspense>
        <ListQuestionsAdmin @position="updateQuestion"></ListQuestionsAdmin>
      </Suspense>
    </div>
    <p v-else>
      Entrez le mot de passe pour acceder au panneau d'administration.
    </p>
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
#deconnexion {
  margin: 20px;
}
</style>
