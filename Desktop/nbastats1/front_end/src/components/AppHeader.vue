<template>
    <header>
      <img class="logo" src="../assets/basketball.png" alt="logo">
      <nav>
        <ul class="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="#">Example</a></li>
          <li><a href="/player-comparison">Players</a></li>
          <li class="dropdown">
            <a href="#" class="dropbtn">Teams</a>
            <div class="dropdown-content">
              <a v-for="(team, id) in teamIDNameMap" :key="id" :href="`/team-summary/${id}`">
                {{ team.team_name }}
              </a>
            </div>
          </li>

        </ul>
      </nav>
      <a class="cta" href="/SignIn"><button>Sign In</button></a>
    </header>
</template>
<script>
import teamIDNameMap from "@/utils/teamIDNameMap";
export default {
  name: 'AppHeader',
  computed: {
    teamIDNameMap() {
      return teamIDNameMap
    }
  },
}
</script>
<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

li, a, button {
  font-family: "Inria Sans", sans-serif;
  font-weight: 500;
  font-size: 16px;
  color: #1d428a;
  text-decoration: none;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 10%;
}

img {
  max-width: 5%;
}

.logo {
  cursor: pointer;
}

.nav-links {
  list-style: none;
}

.nav-links li {
  display: inline-block;
  padding: 0px 20px;
}

.nav-links li a {
  transition: all 0.3s ease 0s;
}

.nav-links li a:hover {
  color: #D00000;
}

button {
  color: #EDF4ED;
  padding: 9px 25px;
  background-color: #D00000;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s ease 0s;
}

button:hover {
  background-color: #FF4747;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  max-height: 300px; /* Adjust this value as needed */
  overflow-y: auto;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border-radius: 5px;
}

.dropdown-content a {
  color: #1d428a;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  transition: all 0.3s ease 0s;
}

.dropdown-content a:hover {
  text-decoration: underline;
  color: #1d428a;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropbtn {
  background-color: transparent;
  color: #1d428a;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropbtn:hover {
  color: #D00000;
}
</style>
