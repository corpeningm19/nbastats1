<template>
  <div class="team-summary">
    <h1 :style="{color: teamColor}" >{{ teamName }}</h1>
    <div class="chart-container">
      <Bar :data="chartData" :options="options" :key="currentStat" />
    </div>
    <div class="buttons">
      <button
          v-for="(statData, statType) in stats"
          :key="statType"
          :class="{ active: currentStat === statType }"
          @click="updateChart(statType)"
          :style="{background: teamColor }"
          style="padding: 9px 25px;"
      >
        {{ statType }}
      </button>
    </div>
  </div>

  <br>
  <div style="overflow-x: auto; width: 95%; margin-left: auto; margin-right: auto;">
    <h3 style="text-align: center;">{{ teamName }} - Player Stat Averages</h3>
    <table class="dataTable">
        <thead>
          <tr>
            <th></th>
            <th v-for="player in allData.Names" :key="player" style="padding-left: 13px;"> {{ player }}</th>
          </tr>
        </thead>
          <tr>
            <th>Points</th>
            <td v-for="stat in allData.Points" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Assists</th>
            <td v-for="stat in allData.Assists" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Rebounds</th>
            <td v-for="stat in allData.Total_Rebounds" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Steals</th>
            <td v-for="stat in allData.Steals" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Blocks</th>
            <td v-for="stat in allData.Blocks" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Field Goals Made</th>
            <td v-for="stat in allData.Field_Goals_Made" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Field Goals Attempted</th>
            <td v-for="stat in allData.Field_Goals_Attempted" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Field Goal Percentage</th>
            <td v-for="stat in allData.Field_Goal_Percentage" :key="stat" style="padding-left: 13px;">{{ stat }}%</td>
          </tr>
          <tr>
            <th>Three Pointers Made</th>
            <td v-for="stat in allData.Three_Pointers_Made" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Three Pointers Attempted</th>
            <td v-for="stat in allData.Three_Pointers_Attempted" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Three Pointer Percentage</th>
            <td v-for="stat in allData.Three_Pointer_Percentage" :key="stat" style="padding-left: 13px;">{{ stat }}%</td>
          </tr>
          <tr>
            <th>Free Throws Made</th>
            <td v-for="stat in allData.Free_Throws_Made" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Free Throw Attempts</th>
            <td v-for="stat in allData.Free_Throw_Attempts" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Free Throw Percentage</th>
            <td v-for="stat in allData.Free_Throw_Percentage" :key="stat" style="padding-left: 13px;">{{ stat }}%</td>
          </tr>
          <tr>
            <th>Offensive Rebounds</th>
            <td v-for="stat in allData.Offensive_Rebounds" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Defensive Rebounds</th>
            <td v-for="stat in allData.Defensive_Rebounds" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Turn Overs</th>
            <td v-for="stat in allData.Turn_Overs" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Personal Fouls</th>
            <td v-for="stat in allData.Personal_Fouls" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
          <tr>
            <th>Minutes</th>
            <td v-for="stat in allData.Minutes" :key="stat" style="padding-left: 13px;">{{ stat }}</td>
          </tr>
    </table>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js';
import { reactive, toRefs, onMounted, computed } from 'vue';
import axios from "axios";
import teamColorMap from "@/utils/teamColorMap";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default {
  components: {
    Bar,
  },
  props: {
    teamId: {
      type: String,
      required: true
    }
  },
  
  setup(props) {
    const state = reactive({
      teamName: '',
      currentStat: '',
      allData: {},
      stats: {
        Points: [],
        Assists: [],
        Rebounds: [],
        Steals: [],
        Blocks: [],
      },
      chartData: {
        labels: [],
        datasets: [
          {
            label: '',
            backgroundColor: teamColorMap[props.teamId],
            data: [],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });

    const teamColor = computed(() => {
      return teamColorMap[props.teamId] || '#000';
    });

    function fetchStats() {
      axios.get(`http://localhost:5000/nba_stats/get_team_summary/${props.teamId}`)
          .then(response => {
            const fetched = response.data
            state.allData = response.data
            // Assign the response data to the chart data
            state.teamName = fetched.team_name;
            state.currentStat = "Points";
            state.chartData.labels = fetched.Names;
            state.stats.Points = fetched.Points;
            state.stats.Assists = fetched.Assists;
            state.stats.Rebounds = fetched.Total_Rebounds;
            state.stats.Steals = fetched.Steals;
            state.stats.Blocks = fetched.Blocks;
            
            console.log(state.allData);
            updateChart(state.currentStat);
          })
          .catch(error => {
            console.error("There was an error fetching the team stats:", error);
          });
    }

    let updateChart = (statType) => {
      state.currentStat = statType;
      state.chartData.datasets[0].data = state.stats[statType];
      state.chartData.datasets[0].label = `${state.teamName} 2023-24 ${statType} Per Game`;
    };

    onMounted(() => {
      fetchStats();
    });

    return {...toRefs(state), updateChart, teamColor};
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

.dataTable {
  width: 100%;
  border-collapse: collapse;
  /* margin-right: 15px; */
  /* margin-left: 15px; */
  margin-bottom: 100px;
  font-size: 12px;
}

.dataTable th, .dataTable td {
  border: 1px solid #ddd;
  padding: 6px;
  text-align: center;
}

.dataTable th {
  background-color: #f2f2f2;
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
  background-color: purple;
}
</style>
