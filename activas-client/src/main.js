import Vue from 'vue'
import App from './App.vue'

import AtComponents from 'at-ui'
import 'at-ui-style'

Vue.config.productionTip = false
Vue.use(AtComponents)

new Vue({
  render: h => h(App)
}).$mount('#app')
