<script>

export default {
  setup() {
    const store = useCounterStore()

    return { store }
  },
  data() {
    return {

    }
  }
}
</script>

<template>
    <div class="p-2">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Регистрация</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Шаблоны</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Документы</a>
        </li>
      </ul>
    </div>
</template>

<style scoped>


</style>
