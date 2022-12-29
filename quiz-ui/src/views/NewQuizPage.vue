<template>

  <div class="container px-4">
    <h1>Nouveau Quiz</h1>
    <p> Pour débuter un nouveau quiz, veuillez remplir ces informations :</p>
    <div class="d-flex justify-content-around align-items-center">
      <input class="p-3 border bg-light" placeholder="Pseudonyme" type="text" />

      <button type="button" class="btn btn-secondary ">Lancer le quiz</button>



    </div>
    <div class="p-2"></div>
    <div class="d-flex justify-content-around align-items-center">
      <router-link class="btn p-2 border bg-light" to="/">Retour</router-link>
    </div>
  </div>




</template>

<script>
//import quizApiService from "@/services/QuizApiService";

export default {
  name: "NewQuiz",

};
</script>