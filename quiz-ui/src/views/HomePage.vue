<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <!-- TODO : En faire un composant ?  -->
  <!-- <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link> -->
</template>

<script>
import quizApiService from "@/services/QuizApiService";

// let registeredScores = [{ playerName: 'Bob', score: 0 }, { playerName: 'Bobby', score: 1 }]
let registeredScores = []

export default {
  name: "HomePage",
  data() {
    return {
      // registeredScores: registeredScores
      registeredScores: registeredScores
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    registeredScores = await quizApiService.getQuizInfo()
    console.log(registeredScores)
  }

};
</script>