<script>
import { wdeStore } from '../stores/counter'
import Auth from './Auth.vue'
import HeaderMenu from './HeaderMenu.vue'
import VerticalMenu from './VerticalMenu.vue'

export default {
    components: {
        Auth,
        HeaderMenu,
        VerticalMenu
    },
    setup() {
        const store = wdeStore()

        return { store }
    },
    data() {
        return {

        }
    },
    methods: {
        
    }
}
</script>

<template>
    <div v-if="this.store.userInfo.isActive === false" class="container-fluid">
        <Auth />
    </div>
    <div v-else class="container-fluid">
       <HeaderMenu />
       <VerticalMenu />
    </div>
</template>

<style scoped>

</style>