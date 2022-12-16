<template>
    <div>
        <div class="all_data_table">
            <h2 class="form_block_label mb-10">
                Сведения о связанных физических лицах
            </h2>

            <div v-for="(listObj, indexObj) in isList" :key="indexObj">
                <div v-for="(itemOrder, indexOrder) in formOrder" :key="indexOrder">
                    <div v-for="(item, index) in listObj" :key="index">

                        <div v-for="(val, name) in item" :key="name" class="all_data_table-row d-flex">
                            <div class="data_table_block" v-if="val && itemOrder === name">
                                <p class="form_block_title">
                                    {{ isTitle(name) }}
                                </p>
                            </div>

                            <div class="data_table_block" v-if="val && itemOrder === name">
                                <div v-if="name === 'first_passport_page'" class="form_block_title d-block">
                                    {{ val[0].name }}
                                </div>
                                <div v-else-if="isArray(val)" class="form_block_title d-block">
                                    <div v-for="(val2, name2) in val" :key="name2">
                                        <div v-if="isObject(val2)">
                                            <div v-for="(val3, key) in item" :key="key">
                                                <div v-if="val3">
                                                    {{ isTitle(key) }} => {{ val3 }}
                                                </div>
                                            </div>
                                        </div>
                                        <p class="d-flex" v-else>- {{ val2 }}</p>

                                    </div>
                                </div>
                                <p class="text-left form_block_title" v-else>
                                    {{ val }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <hr class="mt-2 mb-2" />
            </div>



            <div class="form_block d-flex align-center justify-center mt-4">
                <a @click="del()" class="form_block_delete_link text-decoration-none" href="#">
                    <img src="@/assets/trash.svg" alt="">
                    <span class="pl-2">Удалить</span>

                </a>
                <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="add()">
                    <span class="pr-2">Добавить</span>
                    <img src="@/assets/plus-circle.svg" alt="">
                </v-btn>
            </div>
            <v-btn elevation="2" class="card_content_button" large @click="next()">Продолжить</v-btn>

        </div>
    </div>
</template>
<script>
import { translateMixin } from '@/mixin/translate'
import { formOrderPersone } from '@/mixin/formOrder'

export default {
    mixins: [ translateMixin, formOrderPersone ],
    data() {
        return {
            formData: {},
            
        };
    },

    methods: {
        isObject(element) {
            if (typeof element == 'object') {
                return true
            } else {
                return false
            }
        },
        isArray(element) {
            if (Array.isArray(element)) {
                return true
            } else {
                return false
            }
        },
        isTypeObject(object) {
            if (Array.isArray(object)) {
                return ''
            } else {
                return ''
            }

        },
        
        del() {
            this.$store.dispatch('addObjectFormData', {
                object: 'step_2',
                value: {}
            });
            if (this.$route.query?.type === 'SupervisoryBoard') {
                this.$store.commit('delSupervisoryBoardPersone')
            } else if (this.$route.query?.type === 'CollegialExecutive') {
                this.$store.commit('delCollegialExecutiveBody')
            }

            this.$router.push("/sctructure")
        },
        add() {
            if (this.$route.query?.type === 'SupervisoryBoard') {
                this.$store.commit('addSupervisoryBoardPersone')
            } else if (this.$route.query?.type === 'CollegialExecutive') {
                this.$store.commit('addCollegialExecutiveBody')
            }
            this.$router.push({ path: "/individual-info", query: this.$route.query })
        },
        next() {
            this.$store.dispatch('addObjectFormData', {
                object: 'step_2',
                value: {}
            });
            this.$router.push("/sctructure");


        },
    },
    computed: {
        isList() {
            if (this.$route.query?.type === 'SupervisoryBoard') {
                return this.$store.state.formData.step_3.list_supervisoty_board_persone;
            } else if (this.$route.query?.type === 'CollegialExecutive') {
                return this.$store.state.formData.step_3.list_collegial_executive_body;
            } else {
                return []
            }
        }

    },

};
</script>
<style>
.card_content_button {
    width: 100%;
    box-shadow: 0 0 4px #00000030;
    background: #d41367 !important;
    border-radius: 6px;
    margin-top: 20px;
    font-family: Roboto;
    font-size: 14px !important;
    color: #fff !important;
    font-weight: 500;
    padding: 16px 30px !important;
    text-transform: none;
}

.all_data_table {
    width: 100%;
}

.data_table_block {
    width: 50%;
    display: flex;
    align-items: flex-start;
    justify-content: center;
}

.form_block_title {
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
}

.form_block_delete_link,
.add_form {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 50%;
    text-align: center;
    font-family: 'Roboto' !important;
    font-style: normal !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    line-height: 22px !important;
}
</style>