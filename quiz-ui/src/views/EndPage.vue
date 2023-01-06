<script setup>
import { ref} from "vue";
import participationStorageService from "@/services/ParticipationStorageService";

import { useRouter } from "vue-router";
const router = useRouter();

const username = ref(participationStorageService.getPlayerName());
const score = ref(participationStorageService.getParticipationScore());

function returnHome() {
  router.push("/");
}
</script>

<template>
  <div>
    <h5>Score : {{ score }}</h5>
    <h5>
      Merci d'avoir joué {{ username }}, ton score a bien été enregistré !
    </h5>
    <button type="button" class="btn btn-success" @click="returnHome">
      Retourner à l'accueil
    </button>
  </div>
</template>

<style></style>
