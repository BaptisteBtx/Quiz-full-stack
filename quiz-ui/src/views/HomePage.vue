<template>
  <h1>Informations sur le quiz : </h1>
  <br>
  <h3><u>Nombre de questions :</u> {{ questionsCount }}</h3>
  <h3><u>Scores : </u></h3>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    <h4>
      {{ scoreEntry.playerName }} : <small class="text-muted">{{ scoreEntry.score }}  </small>
      <span v-if="scoreEntry.score == bestScore" class="badge bg-warning">Record !</span>
    </h4>

    <!-- <p class="font-size-100"> - </p> -->
  </div>
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
      registeredScores: [],
      bestScore: 0,
      questionsCount: 0
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    let quizInfo = await quizApiService.getQuizInfo()
    console.log(quizInfo)
    this.registeredScores = quizInfo.data.scores
    this.registeredScores.forEach(e => {
      if (e.score > this.bestScore) this.bestScore = e.score
    });
    this.questionsCount = quizInfo.data.size
  }

};
</script>