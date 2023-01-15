<script>
import { wdeStore } from '../stores/counter'

export default {
    setup() {
        const store = wdeStore()

        return { store }
    },
    data() {
        return {
            authForm: true,
            login: '',
            password: '',
            positionItems: ['position1','position2'],
            rankItems: ['rank1', 'rank2'],
        }
    },
    methods: {
        changeForm() {
            if (this.authForm == true) {
                this.authForm = false
            } else {
                this.authForm = true
            }
        },
        async authentification(login, password) {
            await this.store.postAuthentification(login, password)
        }
    }
}
</script>

<template>
    <div class="d-flex justify-content-center align-items-center bg-secondary bg-gradient auth">
        <div v-if="authForm" class="bg-light shadow-lg rounded needs-validation">
            <div class="form-floating m-3">
                <input v-model="login" type="text" class="form-control" id="floatingInput">
                <label for="floatingInput">Логин</label>
            </div>
            <div class="form-floating m-3">
                <input v-model="password" type="password" class="form-control" id="floatingPassword">
                <label for="floatingPassword">Пароль</label>
            </div>
            <button @click="authentification(this.login, this.password)" type="submit" class="btn btn-primary m-3">Авторизоваться</button>
            <button @click="changeForm()" type="submit" class="btn btn-primary m-3">Зарегистрироваться</button>
        </div>
        <div v-else class="container bg-light shadow-lg rounded">
            <div class="row">
                <div class="col">
                    <div class="form-floating m-3">
                        <input type="text" class="form-control" id="floatingInput">
                        <label for="floatingInput">Фамилия</label>
                    </div>
                </div>
                <div class="col">
                    <div class="form-floating m-3">
                        <input type="text" class="form-control" id="floatingInput">
                        <label for="floatingInput">Логин</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="form-floating m-3">
                        <input type="text" class="form-control" id="floatingInput">
                        <label for="floatingInput">Имя</label>
                    </div>
                </div>
                <div class="col">
                    <div class="form-floating m-3">
                        <input type="password" class="form-control" id="floatingPassword">
                        <label for="floatingPassword">Пароль</label>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="form-floating m-3">
                        <input type="text" class="form-control" id="floatingInput">
                        <label for="floatingInput">Отчество</label>
                    </div>
                </div>
                <div class="col">
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="form-floating m-3">
                        <select id="inputState" class="form-select">
                            <option selected>Тест...</option>
                            <option v-for="item in positionItems">
                                {{ item }}
                            </option>
                        </select>
                        <label for="floatingPassword">Должность</label>
                    </div>
                </div>
                <div class="col">
                    <div class="form-floating m-3">
                        <select id="inputState" class="form-select">
                            <option selected>Тест...</option>
                            <option v-for="item in rankItems">
                                {{ item }}
                            </option>
                        </select>
                        <label for="floatingPassword">Звание</label>
                    </div>
                </div>
                <div class="col"></div>
            </div>
            <div class="row">
                <div class="col"></div>
                <div class="col">
                    <button type="submit" class="m-3 btn btn-primary">Зарегистрироваться</button>
                    <button @click="changeForm()" type="button" class="m-3 btn btn-primary"><i class="bi bi-x-lg"></i></button>
                </div>
                <div class="col"></div>
            </div>
        </div> 
    </div>
</template>

<style lang="less">
.auth {
    height: 100vh;
}

</style>