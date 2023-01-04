<script setup>
import { RouterLink, RouterView } from 'vue-router'



</script>

<template>
  <div id="app-container">
    <header class="bg-light">
      <div id="logo-container">
        <img alt="Vue logo" class="logo" src="@/assets/logo.png" width="150" height="150" />
        <h2>Quiz écologie</h2>
      </div>
      

      <div>
        <nav class="navbar navbar-expand-lg navbar-light" fixed-top>
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
  /* max-height: 100vh; */
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
  /* background-color: grey; */
  background-image: url("assets/header_bg.png");
  background-position: right;
  background-clip: border-box;
  background-repeat: no-repeat;
}

.logo {
  align-self: center;
}


nav {
  width: 100%;
  height: 100%; 
  font-size: 16px;
  text-align: center;
  background-color: transparent;
  
}

nav a.router-link-exact-active {
  /* color: hsla(0, 0%, 10%, 0.2);; */
  background-color: hsla(138, 63%, 24%, 0.2);
  /* background-color: transparent; */
}

/* nav a.router-link-exact-active:hover {
  background-color: transparent;
} */

nav a {
  display: inline-block;
  text-decoration: none;
  color: rgb(8, 98, 6);
  background-color: rgb(241, 244, 243);;
  padding: 0 1rem;
  height: 50px;
  line-height: 45px;
  text-align: center;
  /* width: 25%; */
  flex-grow: 1;
  /* vertical-align: middle; */
  border: 1px solid rgb(8, 98, 6);
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
