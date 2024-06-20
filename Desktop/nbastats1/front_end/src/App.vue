<template>
  <AppHeader />
  <div class="mainContent">
    <RouterView />
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
  }
}
</script>

<style>

  @import '../public/index.css';
  
</style>
