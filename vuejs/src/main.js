import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueTheMask from 'vue-the-mask';
import VueClosable from 'vue-closable'

Vue.use(VueTheMask);
Vue.use(VueClosable);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
