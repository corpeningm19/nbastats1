<template>
    <div style="">
      <h3 class="header-2">Today's Games</h3>
      <div class="scoreboard-container">
        <div class="game-container">
          <!-- Dynamically generate game cards from fetched games data -->
          <GameCard
            v-for="game in sortedTodayGames"
            :key="game.game_id"
            :gameTime="game.game_status_text"
            :homeTeamName="game.home_team.nickname"
            :awayTeamName="game.away_team.nickname"
            :awayTeamRecord="game.away_team.record"
            :homeTeamRecord="game.home_team.record"
            :homeTeamLogo="game.homeTeamLogo"
            :awayTeamLogo="game.awayTeamLogo"
            :homeTeamScore="game.home_team.home_team_score"
            :awayTeamScore="game.away_team.away_team_score"
            :period="game.period"
            />
        </div>
      </div>
    </div>
    <div>
      <h3 class="header-2">Tomorrow's Games</h3>
      <div class="scoreboard-container">
        <div class="game-container">
          <!-- Dynamically generate game cards from fetched games data -->
          <GameCard
            v-for="game in tomorrow_games"
            :key="game.game_id"
            :gameTime="game.game_status_text"
            :homeTeamName="game.home_team.nickname"
            :awayTeamName="game.away_team.nickname"
            :awayTeamRecord="game.away_team.record"
            :homeTeamRecord="game.home_team.record"
            :homeTeamLogo="game.homeTeamLogo"
            :awayTeamLogo="game.awayTeamLogo"
            :homeTeamScore="game.home_team.home_team_score"
            :awayTeamScore="game.away_team.away_team_score"
            :period="game.period"
            />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import GameCard from '@/components/GameCard.vue';
  import teamLogoMap from '@/utils/teamLogoMap';
  
  export default {
    name: 'LiveGames',
    components: {
      GameCard,
    },

    data() {
      return {
        tomorrow_games: [],
        today_games: [],
      };
    },

    computed: {
      sortedTodayGames() {
        return [...this.today_games].sort((a, b) => {
          return a.game_id - b.game_id;
        });
      }
    },


    mounted() {
      this.fetchGames();
      this.scheduleDataFetch();
    },

    methods: {
      fetchGames() {
        axios.get('http://localhost:5000/nba_stats/get_games')
          .then(response => {
            this.today_games = response.data.today_games;
            this.tomorrow_games = response.data.tomorrow_games;
            this.today_games = this.addLogos(this.today_games);
            this.tomorrow_games = this.addLogos(this.tomorrow_games);
          })
          .catch(error => {
            console.error("There was an error fetching the games:", error);
          });
      },

      addLogos(gamesList) {
        return gamesList.map(game => ({
          ...game,
          homeTeamLogo: teamLogoMap[game.home_team.team_id],
          awayTeamLogo: teamLogoMap[game.away_team.team_id]
        }));
      },

      scheduleDataFetch() {
        setInterval(this.fetchGames, 30000);
      }
    },
  }
  </script>
  
  <style>
  /* Add your CSS styling here */
  </style>
  