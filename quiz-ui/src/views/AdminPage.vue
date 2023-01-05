<script setup>

import { ref } from 'vue'
import { useRoute } from 'vue-router';

import LoginComponent from '../components/LoginComponent.vue'
import ListQuestionsAdmin from '../components/ListQuestionsAdmin.vue';

const route = useRoute();
const position = ref(0)
console.log("AdminPage route :", route)

//Récupération du token dans le sessionStorage

let token = ref(window.sessionStorage.getItem("token"))
const authorization = ref(false)

//Affichage de la modification de question

function updateQuestion(positions) {
  console.log('updatequestion')
  if (positions !== 0) {
    position.value = positions
  }
  else {
    position.value = 0
  }
}

//On vérifie la présence d'un token d'authentification

function verifyToken(tokens) {

  if (token.value !== undefined && token.value !== null && token.value !== "") {
    authorization.value = true
  } else if (tokens !== undefined && tokens !== null && tokens !== "") {
    token.value = tokens
    authorization.value = true
  } else {
    authorization.value = false
  }
  return authorization.value
}

function disconnect() {
  window.sessionStorage.setItem("token", "")
  token.value = undefined
  authorization.value = false
  return
}

</script>

<template >
  <div class="container">
    <h1>Admininistration</h1>

    <div v-if="verifyToken()">
      <Suspense>
        <ListQuestionsAdmin @position="updateQuestion"></ListQuestionsAdmin>
      </Suspense>
    </div>
    <div v-else>
      <Suspense>
        <LoginComponent @token="verifyToken"></LoginComponent>
      </Suspense>
    </div>
    <button type="button" class="btn btn-danger" @click="disconnect()">Déconnexion</button>
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
