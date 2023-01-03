<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService';

const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const badPassword = ref("")
const password = ref("")
let token = ref(window.sessionStorage.getItem('token'))

// Launch quiz 
async function returnHome() {
  router.push('/')
}

async function connect() {



  let response = await quizApiService.login(password.value)

  if (response.status === 200) {
    badPassword.value = ""
    window.sessionStorage.setItem("token", response.data.token);
    router.push('/list_questions_admin')
  }
  else {

    badPassword.value = "Mauvais mot de passe"
  }
}

function disconnect() {
  badPassword.value = "Déconnexion réussi"
  token.value = null
  participationStorageService.disconnect()
}

// Export default : remplacé par script setup

</script>

<template>
  <div>
    <h1>Login</h1>
    <div class="input-group mb-3">
      <span class="input-group-text" id="form-username">Mot de passe</span>
      <input type="text" aria-label="Password" aria-describedby="form-username" v-model="password">
    </div>
    <p>{{ badPassword }}</p>
    <div class="input-group mb-3">
      <button type="button" class="btn btn-success" @click="returnHome">Accueil</button>
      <button type="button" class="btn btn-success" @click="connect">Connexion</button>
      <button type="button" class="btn btn-success" @click="disconnect">Déconnexion</button>

    </div>
  </div>
</template>
  
<style>

</style>
  