<script setup>
import { ref, watchEffect } from 'vue'

import { useRouter } from 'vue-router';
import participationStorageService from '../services/ParticipationStorageService';
import quizApiService from '../services/QuizApiService'

const router = useRouter()

// const quiz = ref(null)

// Variables formulaire
const username = ref(participationStorageService.getPlayerName())
const badPassword = ref("")
const password = ref("")


// Launch quiz 
async function returnHome() {
  router.push('/')
}

async function connect() {
  let token = quizApiService.login(password)
  console.log(token)
  if (token === undefined) {
    badPassword.value = "Mauvais mot de passe"
  }
  else {
    badPassword.value = ""
    router.push('/list_questions_admin')
  }


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
    </div>
  </div>
</template>
  
<style>

</style>
  