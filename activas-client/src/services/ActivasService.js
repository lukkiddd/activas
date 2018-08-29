import Api from '@/services/Api.js'

export default {
    get() {
        return Api().get('/activas/data')
    },
    save() {
        return Api().post('/activas/save')
    },
}