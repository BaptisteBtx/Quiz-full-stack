<template>
  <h1>Informations sur le quiz :</h1>
  <p>
    Bienvenue sur notre quiz sur l'écologie et l'environement. Grâce au menu de navigation
    vous pouvez démarrer le quiz (il vous faudra d'abord choisir un nom
    d'utilisateur). Vous pouvez aussi en apprendre plus sur nous dans la section
    "<em>A propos</em>". Si vous disposez du mot de passe, vous pouvez utiliser
    le panneau d'administration pour créer/modifier/supprimer des questions via
    la page "<em>Connexion / Déconnexion</em>". 
    <br> Amusez-vous bien !
  </p>
  <h3><u>Nombre de questions :</u> {{ questionsCount }}</h3>
  <h3><u>Scores : </u></h3>
  <div
    class="d-flex"
    v-for="scoreEntry in registeredScores"
    v-bind:key="scoreEntry.date"
  >
    <h4>
      {{ scoreEntry.playerName }} :
      <small class="text-muted">{{ scoreEntry.score }} </small>
      <span
        v-if="scoreEntry.score == bestScore"
        class="badge bg-warning"
        style="margin-left: 10px"
        >Record !</span
      >
    </h4>
    <p style="margin-left: 10px">({{ scoreEntry.date }})</p>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
    name: "HomePage",
    data() {
        return {
            registeredScores: [],
            bestScore: 0,
            questionsCount: 0,
            error: false
        };
    },
    async created() {
        console.log("Composant Home page 'created'");
        let quizInfo;
        try {
            quizInfo = await quizApiService.getQuizInfo();
        }
        catch (e) {
            console.log(e);
            this.error = true;
        }
        console.log("quizInfo : ",quizInfo);
        this.registeredScores = quizInfo.data.scores;
        this.registeredScores.forEach((e) => {
            if (e.score > this.bestScore)
                this.bestScore = e.score;
        });
        this.questionsCount = quizInfo.data.size;
    }
};
</script>
