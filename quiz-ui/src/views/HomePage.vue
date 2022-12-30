<template>
  <h1>Informations sur le quiz : </h1>
  <h3>Nombre de questions : {{ questionsCount }}</h3>
  <h3>Scores :</h3>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
  <!-- TODO : En faire un composant ?  -->
  <!-- <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link> -->
</template>

<script>
import quizApiService from "@/services/QuizApiService";

// let registeredScores = [{ playerName: 'Bob', score: 0 }, { playerName: 'Bobby', score: 1 }]
// let registeredScores = []
// let questionsCount = 0

export default {
  name: "HomePage",
  data() {
    return {
      // registeredScores: registeredScores
      registeredScores: [],
      questionsCount: 0
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    let quizInfo = await quizApiService.getQuizInfo()
    console.log(quizInfo)
    this.registeredScores = quizInfo.data.scores
    this.questionsCount = quizInfo.data.size
    console.log(this.registeredScores)
    console.log(this.questionsCount)
  }

};
</script>