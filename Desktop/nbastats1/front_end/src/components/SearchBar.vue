<template>
    <div class="search-container">
      <form class="search-bar">
        <input type="text" placeholder="Search Player or Team Stats" v-model="searchQuery">
      </form>
      <div class="suggestions" v-if="searchQuery">
        <div v-for="(item, index) in filteredItems" :key="index" class="suggestion">
          <span @click="goToPage(item)">{{ item.Name }}</span>
          <span @click="toggleFavorite(item)" class="heart">
            <img :src="isFavorite(item) ? require('@/assets/heart-filled.png') : require('@/assets/heart.png')" alt="heart">
          </span>
        </div>
      </div>
    </div>
</template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        searchQuery: '',
        items: [
          { name: 'LeBron James', type: 'player' },
          { name: 'Stephen Curry', type: 'player' },
          { name: 'Los Angeles Lakers', type: 'team' },
          { name: 'Golden State Warriors', type: 'team' },
          // Add more items...
        ],
        favorites: [],
        allPlayers: [],
        allTeams: []
      };
    },

    props: ['context'],

    computed: {
      filteredItems() {
        if (this.context == 'landingPage'){
          return this.allPlayers.concat(this.allTeams).filter(info =>
            info.Name.toLowerCase().includes(this.searchQuery.toLowerCase())
          );
        } else if (this.context == 'playerComparison') {
            return this.allPlayers.filter(player =>
              player.Name.toLowerCase().includes(this.searchQuery.toLowerCase()))
        } else {
          return []
        }
      },
    },

    mounted() {
      this.getPlayers();
      this.getTeams();
    },

    methods: {
      goToPage(item) {
        if (Object.prototype.hasOwnProperty.call(item, 'Team_id')) {
          this.$router.push(`team-summary/${item.Team_id}`);
        }
      },

      getPlayers() {
        axios.get('http://localhost:5000/nba_stats/get_player_names')
          .then(response => {
            this.allPlayers = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the games:", error);
          });
      },


      getTeams() {
        axios.get('http://localhost:5000/nba_stats/get_team_names')
          .then(response => {
            this.allTeams = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the games:", error);
          });
      },

      toggleFavorite(item) {
        const index = this.favorites.findIndex(fav => fav.Name === item.Name);
        if (index >= 0) {
          this.favorites.splice(index, 1);
        } else {
          this.favorites.push(item);
        }
      },

      isFavorite(item) {
        return this.favorites.some(fav => fav.Name === item.Name);
      },
    },
  };
  </script>
  
  <style scoped>
  .suggestions {
    position: absolute;
    top: 35%; /* Align the top of the dropdown with the bottom of the search bar */
    left: 64vh;
    width: calc(40% - 10px); /* Match the width of the input field */
    background: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 0 0 60px 60px; /* Match the border radius of the search bar */
    overflow: hidden; /* Hide overflow to maintain the border radius */
    margin: 30px 20px; /* Align with the padding of the search bar */
}

.suggestion {
    padding: 10px 20px;
    border-bottom: 1px solid #ccc;
    cursor: pointer;
}

.suggestion:last-child {
    border-bottom: none;
}

.suggestion:hover {
    background-color: #f0f0f0;
}

.heart {
    float: right;
    margin-right: 70px;
    width: 50%;
    height: auto;
}
  </style>
  