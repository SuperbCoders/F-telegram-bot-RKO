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
                opf: {},
                short: "",
                is_conditions: false,
            },

            step_2: {
                email: "",
                contact_phone_number: "",
                donainname: "",
            },
            step_3: {
                addresses: [
                    {
                        type_address: [],
                        legal_address: "",
                        mail_address: "",
                        address: "",
                    },
                ]
            },
            step_4: {
                list_persone: [],
            },
            step_5: {
                document_certifying_identity_executive_file: null,
                document_confirming_real_activity_file: null,
                document_licenses_file: null,
                document_certifying_identity_ceo_file: null,

                document_certifying_identity_executive: [],
                document_confirming_real_activity: [],
                document_licenses: [],
                document_certifying_identity_ceo: [],
            },
            step_6: {
                structure_value: "",
            },
            step_7: {
                founders: [{
                    inn: "",
                    share: "",
                    name: "",
                    ogrn: "",
                }],
            },
            step_8: {
                beneficiaries: "",
                third_parties: "",
            },
            step_9: {
                additional_inforamtion: "",
            },
            step_10: {
                planned_operations: [],
                planned_other: "",
            },
            step_11: {
                information_goals: [],
            },
            step_12: {
                codeword: "",
            },
            step_13: {
                information_counterparties: null,
                information_counterparties_two: null,
                name_organization: null,
                name_organization_two: null,
            },
            step_14: {
                subject_licensing: "",
                history_reputation: "",
                num_transactions_month: "",
                num_transactions_week: "",
                num_transactions_quarter: "",
                num_transactions_age: "",
                sum_transactions_month: "",
                sum_transactions_week: "",
                sum_transactions_quarter: "",
                sum_transactions_age: "",
                monthly_cash_withdrawal: "",
                week_cash_withdrawal: "",
                quarter_cash_withdrawal: "",
                age_cash_withdrawal: "",
                sum_mouth_cash_withdrawal: "",
                sum_week_cash_withdrawal: "",
                sum_quarter_cash_withdrawal: "",
                sum_age_cash_withdrawal: "",
                foreign_trade_contracts_month: "",
                foreign_trade_contracts_week: "",
                foreign_trade_contracts_quarter: "",
                foreign_trade_contracts_age: "",
                foreign_sum_contracts_month: "",
                foreign_sum_contracts_week: "",
                foreign_sum_contracts_quarter: "",
                foreign_sum_contracts_age: "",
                sources_cash_receipts: "",
                headcount: "",
                hasConstantPayers: "",
                hasConstantPayersDetails: "",
            },
            step_15: {
                tariff: null,
                additional_products: [],
            },
        },

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
        indexLastListPerson(state) {
            return state.formData.step_4.list_persone.length - 1;
        }
    },
    mutations: {
        toggleDrawer(state, value) {
            state.drawer = value;
        },
        setDataCompany(state, value) {
            state.dataCompany = value;
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

        addPersone(state) {
            state.formData.step_4.list_persone.push({});
        },
        delPersoneLast(state) {
            state.formData.step_4.list_persone.pop();
        },
        delPersoneIndex(state, { index }) {
            state.formData.step_4.list_persone.splice(index, 1);
        },
        async setPersone(state, { key, value, index }) {
            const last_element = state.formData.step_4.list_persone[index];
            last_element[key] = value;

            const contact_number = state.formData.step_1.contact_number;
            const response_data = Object.assign({ last_step: `${key}` }, state.formData.step_4);

            await fetch(process.env.VUE_APP_HOST_API + `/api/loan-application/current/${contact_number}/`, {
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
        async addObjectFormData(context, { object, value }) {

            let response_data = null;

            if (isEmptyObject(value)) {
                response_data = { last_step: object };
            } else {
                response_data = Object.assign({ last_step: object }, value);
                context.commit("addItemFormDataObject", { object, value });
            }
            const contact_number = context.state.formData.step_1.contact_number;

            await fetch(process.env.VUE_APP_HOST_API + `/api/loan-application/current/${contact_number}/`, {
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
