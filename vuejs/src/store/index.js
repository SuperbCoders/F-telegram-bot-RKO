import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    drawer: null,
    authToken: localStorage.getItem("authToken") || null,
    user: null,
    data: null,
    isForegin: false,
    result: {},
    formData: [],
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
    ],
    leaderType: [
      {
        id: 1,
        title: 'Руководитель'
      },
      {
        id: 2,
        title: 'Управляющая компания'
      }
    ],
    dataCompany: {}
  },
  getters: {
    isList (state) {
      const result = []
      state.leaderList.map((item) => {
        result.push(item.title)
      })
      return result
    },
    isLeaderType (state) {
      const result = []
      state.leaderType.map((item) => {
        result.push(item.title)
      })
      return result
    },
    // isFormData (state) {
    //   state.formData.map((item) => {
    //    state.result = Object.assign(item)
    //   })
    //   return state.result
    // }
  },
  mutations: {
    toggleDrawer(state, value) {
      state.drawer = value;
    },
    setDataCompany(state, value){
      state.dataCompany = value;
    },
    isForeginStatus(state, status) {
      state.isForegin = status
    },
    addItemFormData (state, item) {
      state.formData.push(item)
    },
    IsFormData (state) {
      state.formData.map((item) => {
        state.result = Object.assign(item, state.result)
      })
    }
  },
  actions: {
  },
  modules: {},
});
