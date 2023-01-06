<script setup>
import { ref } from "vue";

import quizApiService from "../services/QuizApiService";

// Variables formulaire
const emits = defineEmits(["token"]);
const badPassword = ref(false);
const password = ref("");
const token = ref(window.sessionStorage.getItem("token"));

async function connect() {
  //Récupère le token via un appel API et l'initialise dans le sessionStorage

  let response;
  try {
    response = await quizApiService.login(password.value);
  } catch (error) {
    console.log(error);
  }

  if (response.status === 200) {
    badPassword.value = false;
    window.sessionStorage.setItem("token", response.data.token);
    token.value = response.data.token;
    emits("token", response.data.token);
  } else {
    badPassword.value = true;
  }
}
function disconnect() {
  window.sessionStorage.setItem("token", null);
  token.value = null;
  emits("token", null);
}
</script>

<template>
  <button
    v-if="token"
    id="deconnexion"
    type="button"
    class="btn btn-danger"
    @click="disconnect"
  >
    Déconnexion
  </button>
  <div v-else>
    <div class="input-group mb-3">
      <span class="input-group-text">Mot de passe</span>
      <input type="text" aria-label="Password" v-model="password" />
    </div>
    <div
      v-if="badPassword"
      class="alert alert-danger d-flex align-items-center"
      role="alert"
    >
      <div>Mauvais mot de passe.</div>
    </div>
    <button type="button" class="btn btn-success" @click="connect">
      Connexion
    </button>
  </div>
</template>

<style></style>
