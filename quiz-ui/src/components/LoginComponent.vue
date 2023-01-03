<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import quizApiService from '../services/QuizApiService';

const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const emits = defineEmits(["token"])
const badPassword = ref("")
const password = ref("")

// Return Home
async function returnHome() {
  router.push('/')
}

async function connect() {

  //Récupère le token via un appel API et l'initialise dans le sessionStorage

  let response = await quizApiService.login(password.value)

  if (response.status === 200) {
    badPassword.value = ""
    window.sessionStorage.setItem("token", response.data.token);
    emits("token", response.data.token)
    //router.push('/list_questions_admin')
  }
  else {
    badPassword.value = "Mauvais mot de passe"
  }
}

// Export default : remplacé par script setup

</script>

<template>
  <div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="form-username">Mot de passe</span>
      <input type="text" aria-label="Password" aria-describedby="form-username" v-model="password">
    </div>
    <p>{{ badPassword }}</p>
    <div class="d-flex justify-content-around">
      <button type="button" class="btn btn-success" @click="returnHome">Retour</button>
      <button type="button" class="btn btn-success" @click="connect">Connexion</button>

    </div>
  </div>
</template>
  
<style>

</style>
  