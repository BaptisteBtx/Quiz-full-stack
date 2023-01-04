<script setup>
import { RouterLink, RouterView } from 'vue-router'



</script>

<template>
  <div id="app-container">
    <header class="bg-light">
      <div>
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
        <h2>Quiz app</h2>
      </div>
      

      <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light" fixed-top>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/start_new_quiz">Démarrer le quiz !</RouterLink>
          <RouterLink to="/about">A propos</RouterLink>
          <RouterLink to="/admin">Connexion / Déconnexion</RouterLink>
        </nav>
        
      </div>
    </header>
    <RouterView />

    
  </div>
</template>

<style scoped>

#app-container {
  /* display: flex; */
  width: 100%;
}

header {
  line-height: 1.5;
  max-height: 100vh;
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

/* .logo {
  display: block;
  margin: 0 auto 2rem;
} */

nav {
  width: 100%;
  height: 100%;
  font-size: 16px;
  text-align: center;
  
}

nav a.router-link-exact-active {
  /* color: hsla(0, 0%, 10%, 0.2);; */
  background-color: hsla(0, 0%, 60%, 0.2);
}

/* nav a.router-link-exact-active:hover {
  background-color: transparent;
} */

nav a {
  display: inline-block;
  text-decoration: none;
  padding: 0 1rem;
  height: 50px;
  line-height: 45px;
  text-align: center;
  /* width: 25%; */
  flex-grow: 1;
  /* vertical-align: middle; */
  border: 1px solid black;
  /* border-radius: 10px; */
}

nav a:first-of-type {
  /* border: 0; */
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
nav a:last-of-type {
  /* border: 0; */
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}

@media (min-width: 1024px) {

  /* nav {
    text-align: center;
    height: 100%;
    margin-left: -1rem;
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  } */
}
</style>
