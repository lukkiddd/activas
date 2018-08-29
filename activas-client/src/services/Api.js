import axios from 'axios'

let $axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
    headers: {
        'Content-Type': 'application/json',
    }
})

$axios.interceptors.response.use(function (response) {
    return response
}, function (error, c) {
    // Handle Error
    console.log(error)
    return Promise.reject(error)
})

export default () => {
    return $axios
}