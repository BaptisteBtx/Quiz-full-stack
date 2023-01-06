<script setup>

import { ref } from 'vue'
import { useRoute } from 'vue-router';

import LoginComponent from '../components/LoginComponent.vue'
import ListQuestionsAdmin from '../components/ListQuestionsAdmin.vue';

const route = useRoute();
const position = ref(0)
console.log("AdminPage route :", route)

//Récupération du token dans le sessionStorage

const token = ref(window.sessionStorage.getItem("token"))
// const authorization = ref(false)

//Affichage de la modification de question

function updateQuestion(positions) {
  if (positions !== 0) {
    position.value = positions
  }
  else {
    position.value = 0
  }
}

//On vérifie la présence d'un token d'authentification

// function verifyToken(tokens) {
//   console.log("token : ",token.value)

//   if (token?.value) {
//     authorization.value = true
//   } else if (tokens?.value) {
//     console.log("tokens",token)
//     token.value = tokens
//     authorization.value = true
//   } else {
//     authorization.value = false
//   }
//   return authorization.value
// }
function setToken(newToken) {
  token.value = newToken
}


</script>

<template >
  <div class="container">
    <h1>Admininistration</h1>
    <LoginComponent @token="setToken"></LoginComponent>
    

    <div v-if="token">
      <Suspense>
        <ListQuestionsAdmin @position="updateQuestion"></ListQuestionsAdmin>
      </Suspense>
    </div>
    <p v-else>Entrez le mot de passe pour acceder au panneau d'administration</p>
    <!-- <div v-else>
      <Suspense>
        
      </Suspense>
    </div> -->
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
