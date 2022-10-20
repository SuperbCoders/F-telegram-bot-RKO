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
        assigned_publ_pers_relation: false,
        accownt_own_living: false,
        assigned_publ_pers_registraion: false,
        result: {},
        formData: [],
        
        listSupervisotyBoardPersone: [],
        supervisoryBoardPersone: {},

        listCollegialExecutiveBody: [],
        collegialExecutiveBody: {},

        leaderList: [
            {
                id: 1,
                title: "Единственный участник (один участник с долей 100%)",
            },
            {
                id: 2,
                title: "Общее собрание участников (несколько участников)",
            },
            {
                id: 3,
                title: "Индивидуальный предприниматель",
            },
            {
                id: 4,
                title: "Единственный акционер",
            },
            {
                id: 5,
                title: "Общее собрание акционеров (несколько акционеров",
            },
        ],
        leaderType: [
            {
                id: 1,
                title: "Руководитель",
            },
            {
                id: 2,
                title: "Управляющая компания",
            },
        ],
        dataCompany: {},
    },
    getters: {
        isList(state) {
            const result = [];
            state.leaderList.map((item) => {
                result.push(item.title);
            });
            return result;
        },
        isLeaderTypeTitle(state) {
            const result = [];
            state.leaderType.map((item) => {
                result.push(item.title);
            });
            return result;
        },
    },
    mutations: {
        toggleDrawer(state, value) {
            state.drawer = value;
        },
        setDataCompany(state, value) {
            state.dataCompany = value;
        },
        isForeginStatus(state, status) {
            state.isForegin = status;
        },
        addItemFormData(state, item) {
            state.formData.push(item);
            state.formData.reverse()
            scroll(0, 0);
        },
        IsFormData(state) {
            state.formData.map((item) => {
                state.result = Object.assign(item, state.result);
            });
        },
        IsFormDataObject(state) {
            const object = Object.keys(state.formData);
            object.forEach((key) => {
                state.formData = Object.assign(
                    {
                        key: state.formData[key],
                    },
                    state.result
                );
                console.log(`${key} : ${state.formData[key]}`);
            });
            console.log(this.state.result);
        },
        addItemFormDataObject(state, payolad) {
            state.formData[payolad.object] = payolad.value;
        },

        setSupervisoryBoardPersone(state, {key, value}) {
            state.supervisoryBoardPersone[key] = value;
            scroll(0, 0);
        },
        setListSupervisoryBoardPersone(state) {
            state.listSupervisotyBoardPersone.push(Object.assign({}, state.supervisoryBoardPersone));
            state.supervisoryBoardPersone = {};
        },

        setCollegialExecutiveBody(state, {key, value}) {
            state.collegialExecutiveBody[key] = value;
            scroll(0, 0);
        },
        setListCollegialExecutiveBody(state) {
            state.listCollegialExecutiveBody.push(Object.assign({}, state.collegialExecutiveBody));
            state.collegialExecutiveBody = {};
        }
    },
    actions: {
        addObjectFormData(context, payolad) {
            context.commit("addItemFormDataObject", payolad);
        },
    },
    modules: {},
});
