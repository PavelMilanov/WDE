<script setup>
import VerticalMenu from './components/VerticalMenu.vue'
import MainArea from './components/MainArea.vue'
import HeaderMenu from  './components/HeaderMenu.vue'
</script>

<template>
  <div class="container">
    <div class="row">
      <HeaderMenu />
    </div>
    <div class="row">
      <div class="d-flex align-items-stretch main">
          <VerticalMenu />
          <MainArea />
      </div>
    </div>
  </div>
</template>

<style scoped>
.main {
  height: 100vh;
}
</style>
