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
            window.sessionStorage.setItem("score", participationScore);
      },
      getParticipationScore() {
            return window.sessionStorage.getItem("score");
      },
      getToken() {
            return window.sessionStorage.getItem("token");
      },
      disconnect() {
            window.sessionStorage.setItem("token", null)
      },

};
