import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: null,
    authToken: localStorage.getItem("authToken") || null,
    user: null,
    data: null,
    leaderList: [
      {
        id: 1,
        title: 'Единственный участник (один участник с долей 100%)'
      },
      {
        id: 2,
        title: 'Общее собрание участников (несколько участников)'
      },
      {
        id: 3,
        title: 'Индивидуальный предприниматель'
      },
      {
        id: 4,
        title: 'Единственный акционер'
      },
      {
        id: 5,
        title: 'Общее собрание акционеров (несколько акционеров'
      },
    ]
  },
  getters: {
    isList (state) {
      const result = []
      state.leaderList.map((item) => {
        result.push(item.title)
      })
      return result
    }
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
