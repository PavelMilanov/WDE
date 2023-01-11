import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const wdestore = defineStore('wdestore', {

  state: () => ({
    user: {
      isActive: false
    },
  }),
  getters: {
    doubleCount: (state) => state.count * 2,
  },
  actions: {
    registration() {

    },
    authentification() {
      axios.post(`http://${import.meta.env.SERVER_IP}:8000/api/auth/authentificate`)
    }
  }
})