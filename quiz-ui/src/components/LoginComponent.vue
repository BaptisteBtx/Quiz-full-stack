<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import quizApiService from '../services/QuizApiService';

const router = useRouter()

// Variables formulaire
const emits = defineEmits(["token"])
const badPassword = ref(false)
const password = ref("")
const token = ref(window.sessionStorage.getItem("token"))

async function connect() {

  //Récupère le token via un appel API et l'initialise dans le sessionStorage

  let response = await quizApiService.login(password.value)

  if (response.status === 200) {
    badPassword.value = false
    window.sessionStorage.setItem("token", response.data.token);
    token.value = response.data.token
    emits("token", response.data.token)
    //router.push('/list_questions_admin')
  }
  else {
    badPassword.value = true
  }
}
function disconnect() {
  window.sessionStorage.setItem("token", null)
  token.value = null
  emits("token", null)
}

</script>

<template>
  <button v-if="token" id="deconnexion" type="button" class="btn btn-danger" @click="disconnect">Déconnexion</button>
  <div v-else>
    <div class="input-group mb-3">
      <span class="input-group-text" id="form-username">Mot de passe</span>
      <input type="text" aria-label="Password" aria-describedby="form-username" v-model="password">
    </div>
    <div
      v-if="badPassword"
      class="alert alert-danger d-flex align-items-center"
      role="alert"
    >
      <div>Mauvais mot de passe.</div>
    </div>
    <button type="button" class="btn btn-success" @click="connect">Connexion</button>

  </div>
</template>
  
<style>

</style>
  