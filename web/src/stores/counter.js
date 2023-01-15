import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const wdeStore = defineStore('wdestore', {

  state: () => ({
    user: {
      isActive: false,
      token: '',
    }
  }),
  getters: {
    userInfo: (state) => state.user
  },
  actions: {
    registration() {

    },
    async postAuthentification(login, password) {
      let responseToken
      const params = new URLSearchParams()
      params.append('username', login)
      params.append('password', password)
      await axios.post(`http://${import.meta.env.VITE_SERVER_IP}:8000/api/auth/authentificate`, params
      ).then(function (response) {
        responseToken = response.data.access_token
      }).catch(function (error) {
        console.log(error)
      })
      this.user.isActive = true
      this.user.token = responseToken
    },
    SignOut() {
      this.user.isActive = false
      this.user.token = ''
    }
  }
})