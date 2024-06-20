<template>
  <div class="player-comparison">
    <SearchBar context="playerComparison"></SearchBar>
    <h1 style="margin-top: 40px;" >Favorite Players</h1>
    <div class="chart-container">
      <Line :data="chartData" :options="options" :key="currentStat" />
    </div>
    <div class="buttons">
      <button
          v-for="stat in availableStats"
          :key="stat"
          :class="{ active: currentStat === stat }"
          @click="updateChart(stat)"
      >
        {{ stat }}
      </button>
    </div>
  </div>
</template>

<script>
import {Line} from 'vue-chartjs';
import SearchBar from './SearchBar.vue';
import {reactive, toRefs} from 'vue';
import {
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Title,
  Tooltip,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);

export default {
  components: {
    Line,
    SearchBar
  },
  setup() {
    const state = reactive({
      currentStat: 'Points',
      stats: {
        Points: {
          PlayerOne: [30, null, 35, 40],
          PlayerTwo: [28, 20, 27, 32],
        },
        Assists: {
          PlayerOne: [8, null, 9, 5],
          PlayerTwo: [6, 5, 7, 4],
        },
        Rebounds: {
          PlayerOne: [10, null, 9, 13],
          PlayerTwo: [11, 9, 10, 8],
        },
        Blocks: {
          PlayerOne: [1, null, 2, 1],
          PlayerTwo: [2, 1, 1, 3],
        },
        Steals: {
          PlayerOne: [4, null, 3, 2],
          PlayerTwo: [3, 4, 2, 1],
        }
      },
      chartData: {
        labels: ['Game 1', 'Game 2', 'Game 3', 'Game 4'],
        datasets: []
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
      availableStats: ['Points', 'Assists', 'Rebounds', 'Blocks', 'Steals'],
      chartColors: {
        PlayerOne: 'rgb(75, 192, 192)',
        PlayerTwo: 'rgb(255, 99, 132)',
      },
    });

    function updateChart(selectedStat) {
      state.chartData.datasets = Object.keys(state.stats[selectedStat]).map(player => ({
        label: player,
        data: state.stats[selectedStat][player],
        fill: false,
        borderColor: state.chartColors[player],
        tension: 0.1,
        spanGaps: true,
      }));
      state.currentStat = selectedStat;
    }

    updateChart(state.currentStat);

    return { ...toRefs(state), updateChart };
  },
};
</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  height: 400px;
  width: 800px;
}
.buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
  margin-top: 20px;
}
.buttons button {
  margin-right: 10px;
  background: #666666;
}

.buttons .active {
  color: #fff;
  background-color: #D00000;
}
</style>
