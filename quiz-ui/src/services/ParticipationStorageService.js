export default {
      clear() {
            // todo : implement
      },
      savePlayerName(playerName) {
            window.localStorage.setItem("playerName", playerName);
      },
      getPlayerName() {
            return window.localStorage.getItem("playerName")
      },
      saveParticipationScore(participationScore) {
            return window.sessionStorage.setItem("score", participationScore);
      },
      getParticipationScore() {
            return window.sessionStorage.getItem("score");
      }
};