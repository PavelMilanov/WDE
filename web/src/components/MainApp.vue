<script>
import { wdeStore } from '../stores/counter'
import Auth from './Auth.vue'
import RootMenu from './RootMenu.vue'
import VerticalMenu from './VerticalMenu.vue'

export default {
    components: {
        Auth,
        RootMenu,
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
        <div class="d-flex">
            <div class="">
                <VerticalMenu />
            </div>
            <div class="flex-grow-1">
                <RootMenu />
            </div>
        </div>
    </div>
</template>

<style lang="less">
.d-flex {
    height: 100vh;
}
</style>