import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VuetifyMask from './plugins/vuetifyMask'
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  VuetifyMask,
  render: h => h(App)
}).$mount('#app')
