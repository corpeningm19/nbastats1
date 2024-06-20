<template>
    <AppTitle />
    <SearchBar context="landingPage"/>
    <ImageSlider />
    <LiveGames />
  </template>
  
  <script>
  import AppTitle from './AppTitle.vue'
  import SearchBar from './SearchBar.vue'
  import ImageSlider from './ImageSlider.vue'
  import LiveGames from './LiveGames.vue'
  
  export default {
    name: 'LandingPage',
    components: {
      AppTitle,
      SearchBar,
      ImageSlider,
      LiveGames
    },
  }
  </script>
  
  <style>
  </style>
  