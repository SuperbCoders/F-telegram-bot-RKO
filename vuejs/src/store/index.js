import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

function isEmptyObject(value) {
    return Object.keys(value).length === 0 && value.constructor === Object;
  }

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
        formData: {
            step_1: {
                inn: "",
                company_name: "",
                contact_number: "",
                ogrn: "",
            },
            step_2: {
                addresses: [
                    {
                        typeAdress: [],
                        legal_address: "",
                        physic_address: "",
                        mail_address: "",
                        address: "",
                        basis: "",
                    },
                ]
            },
            step_3: {
                supreme_management_body: "Единственный участник (один участник с долей 100%)",
                supreme_management_person: "Руководитель",
                supreme_management_inn: "",

                is_supervisoty: false,
                collegiate_person: "",
                list_supervisoty_board_persone: [],

                is_collegiate_body: false,
                supervisoty_board_persone_name: "",
                list_collegial_executive_body: [],
            },
            step_4: {
                company_group_name: null,
                start_date: null,
                end_date: null,
                group_members: [
                    {
                        name: null,
                        inn: null,
                        ogrn: null,
                    },
                ],
            },
            step_5: {
                employers_volume: 0,
                salary_debt: 0,
            },
            step_6: {
                licence_type: null,
                licence_number: null,
                licence_issued_by: null,
                licence_date_issue: null,
                licenced_validity: null,
                licenced_activity: null,
            },
            step_7: {
                planned_operations: [],
            },
            step_8: {
                beneficiaries: null,
            },
            step_9: {
                account_operations: [],
                operation_volume: null,
                operation_sum: null,
                operation_nalition: null,
                sum_per_month: null,
                outside_contracts_volume: null,
                cash_source: [],
                state_employers: null,

            }
        },

        list_supervisoty_board_persone: [],
        supervisoryBoardPersone: {},

        list_collegial_executive_body: [],
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
        }
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
            scroll(0, 0);
        },

        IsFormData(state) {
            const object = Object.keys(state.formData);
            const result = [];
            object.forEach((key) => {
                result.push(state.formData[key]);
            });
            result.reverse();
            result.map((item) => {
                state.result = Object.assign(item, state.result);
            });
        },

        addItemFormDataObject(state, payolad) {
            state.formData[payolad.object] = Object.assign({}, payolad.value);
            scroll(0, 0);
        },



        addSupervisoryBoardPersone(state) {
            state.formData.step_3.list_supervisoty_board_persone.push({});
        },
        delSupervisoryBoardPersone(state) {
            state.formData.step_3.list_supervisoty_board_persone.pop();
        },
        async setSupervisoryBoardPersone(state, { key, value }) {
            const length = state.formData.step_3.list_supervisoty_board_persone.length;
            const is_element = length > 0;
            if (is_element) {
                const last_element = state.formData.step_3.list_supervisoty_board_persone[length - 1];
                last_element[key] = value;
            }
            const contact_number = state.formData.step_1.contact_number;
            const response_data = Object.assign({ last_step: `${key}*supervisory` }, state.formData.step_3);

            await fetch(process.env.VUE_APP_HOST_API+`/api/loan-application/current/${contact_number}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                },
                body: JSON.stringify(response_data)
            })
            scroll(0, 0);
        },




        addCollegialExecutiveBody(state) {
            state.formData.step_3.list_collegial_executive_body.push({});
        },

        delCollegialExecutiveBody(state) {
            state.formData.step_3.list_collegial_executive_body.pop();
        },

        async setCollegialExecutiveBody(state, { key, value }) {
            const length = state.formData.step_3.list_collegial_executive_body.length;
            const is_element = length > 0;
            if (is_element) {
                const last_element = state.formData.step_3.list_collegial_executive_body[length - 1];
                last_element[key] = value;
            }
            const contact_number = state.formData.step_1.contact_number;
            const response_data = Object.assign({ last_step: `${key}*collegial` }, state.formData.step_3);

            await fetch(process.env.VUE_APP_HOST_API+`/api/loan-application/current/${contact_number}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                },
                body: JSON.stringify(response_data)
            })
            scroll(0, 0);
        },
    },
    actions: {
        async addObjectFormData(context, payolad) {
            const object = payolad.object
            const value = payolad.value;

            let response_data = null;
            
            if (isEmptyObject(value)) {
                response_data = { last_step: object };
            } else {
                response_data = Object.assign({ last_step: object }, value);
                context.commit("addItemFormDataObject", { object, value });
            }

            const contact_number = context.state.formData.step_1.contact_number;
            
            
             

            await fetch(process.env.VUE_APP_HOST_API+`/api/loan-application/current/${contact_number}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                },
                body: JSON.stringify(response_data)
            })
        },
        async loadObjectFormData(context, payolad) {
            const formData = payolad;
            console.log(formData);

            for (const step_name in context.state.formData) {
                const step = context.state.formData[step_name];
                for (const key in step) {
                    if (formData[key]) {
                        step[key] = formData[key]
                    }

                }
            }
        }
    },
});
