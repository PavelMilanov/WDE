<script>
import { wdeStore } from '../stores/counter';


export default {
  setup() {
    const store = wdeStore()

    return { store }
  },
  data() {
    return {

    }
  },
  methods: {
    exit() {
      this.store.SignOut()
    }
  }
}
</script>

<template>
      <ul class="navbar-nav me-auto bg-secondary">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Личный кабинет</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Шаблоны</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Документы</a>
        </li>
        <li class="nav-item">
          <a @click="exit()" class="nav-link active" aria-current="page" href="#">
            <i class="bi bi-box-arrow-right ms-4"></i>
          </a>
        </li>
      </ul>
</template>

<style scoped>
.bi-box-arrow-right {
  font-size: 26px;
}
</style>
