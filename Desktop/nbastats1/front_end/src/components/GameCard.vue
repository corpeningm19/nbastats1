<template>
    <div class="game" :class="{'flash-effect': isFlashing }">
      <div class="game-time">{{ gameTime }}</div>
      <div class="team-container">
        <div class="team away-team">
          <img v-if="awayTeamLogo" :src="awayTeamLogo" alt="Away Team Logo" class="team-logo">
          <div class="team-name">{{ awayTeamName }}</div>
          <div class="team-record">{{ awayTeamRecord }}</div>
          <div v-if="awayTeamScore" class="team-score">{{ awayTeamScore }}</div>
        </div>
        <div class="team home-team">
          <img v-if="homeTeamLogo" :src="homeTeamLogo" alt="Home Team Logo" class="team-logo">
          <div class="team-name">{{ homeTeamName }}</div>
          <div class="team-record">{{ homeTeamRecord }}</div>
          <div v-if="homeTeamScore" class="team-score">{{ homeTeamScore }}</div>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  export default {
    name: 'GameComponent',
    props: {
      gameTime: String,
      homeTeamName: String,
      homeTeamRecord: String,
      homeTeamLogo: String,
      homeTeamScore: Number,
      awayTeamName: String,
      awayTeamRecord: String,
      awayTeamLogo: String,
      awayTeamScore: Number,
      period: Number
    },

    data() {
      return {
        isFlashing: false,
      }
    },

    watch: {
      gameTime: {
        immediate: false,
        handler(newVal, oldVal) {
          if (newVal !== oldVal) {
            this.triggerFlash();
          }
        }
      }
    },

    methods: {
      triggerFlash() {
        this.isFlashing = true;
        setTimeout(() => {
          this.isFlashing = false;
        }, 1000);
      }
    }
  }
  </script>
  
  <style>
    .flash-effect {
      animation: flashBackground 1s;
    }

    @keyframes flashBackground {
      from { background-color: lightblue; }
      to { background-color: #fafafa; }
    }
  </style>
  