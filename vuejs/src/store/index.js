import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: null,
    authToken: localStorage.getItem("authToken") || null,
    user: null,
    data: null,
  },
  getters: {
  },
  mutations: {
    toggleDrawer(state, value) {
      state.drawer = value;
    },
  },
  actions: {
  },
  modules: {},
});
