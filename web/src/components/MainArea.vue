<script>
import { wdeStore } from '../stores/counter'

export default {
    setup() {
        const store = wdeStore()

        return { store }
    },
    data() {
        return {

        }
    }
}
</script>

<template>
    <div class="p-2 flex-grow-1">
        <p>main area</p>
    </div>
</template>

<style scoped>

</style>