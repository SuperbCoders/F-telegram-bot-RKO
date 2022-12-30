<template>
    <div class="structure_form">
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <h2 class="text-left mb-5 font-bold form_block_label">
            Сведения о физических лицах организации
        </h2>
        <v-card elevation="2" class="pa-4 mb-2 d-flex" v-for="(val, key) in list_persone" :key="key">
            <div>{{ renderName(val['substep_1']) }}</div>
            <button style="margin-left: auto;" @click="editPersone(key)">Изменить</button>
            <button class="ml-5" @click="deletePersone(key)">Удалить</button>
        </v-card>
        <v-form ref="form" v-model="valid" lazy-validation>
            <div class="form_block mt-2">
                <div class="contain_btn_add">
                    <v-btn large style="width: 50%; background: #F3F4F4 !important; color: #5B656D !important" class="text-center
                  d-flex
                  align-center
                  justify-center
                  add_form" @click="createPersone">
                        <span class="pr-3">Добавить</span>
                        <v-icon>mdi-plus-circle-outline</v-icon>
                    </v-btn>
                </div>
            </div>

        </v-form>
        <line-step :step="4" class="mt-4" />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
            Продолжить
        </v-btn>
    </div>
</template>
<script>
import LineStep from "@/components/line_step/line_step.vue";
import { loadCurrentData } from '@/utils/loadStore'

export default {
    props: {
        number_step: {
            type: Number,
        }
    },
    data: () => ({
        valid: true,
        innRules: [
            (v) => !!v || "Это поле обязательно",
            (v) =>
                (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
        ],
        requiredRules: [(v) => !!v || "Это поле обязательно"],
    }),
    mounted() {
        loadCurrentData({
            currentData: this.currentData,
            step: `step_${this.number_step}`,
            vue: this,
        });
    },
    methods: {
        validate() {
            this.$refs.form.validate();

            if (this.$refs.form.validate()) {
                this.$store.dispatch("addObjectFormData", {
                    object: "step_4",
                    value: { list_persone: this.list_persone },
                });
                this.next();
            }
        },
        next() {
            this.$router.push({ name: `step_${this.number_step + 1}` });
        },
        back() {
            this.$router.push({ name: `step_${this.number_step - 1}` });
        },
        editPersone(key) {
            this.$router.push({
                name: "substep_1",
                params: {
                    id: key
                }
            })
        },
        deletePersone(key) {
            this.$store.commit("delPersoneIndex", { index: key });
        },
        async createPersone() {
            this.$store.commit("addPersone");
            await this.$store.dispatch('addObjectFormData', {
                object: 'step_4',
                value: { list_persone: this.list_persone },
            })

            this.$router.push({
                name: "substep_1",
                params: {
                    id: this.getLastIndexPerson
                }
            })
        },
        renderName(obj) {
            const account_own_lastname = obj?.account_own_lastname ?? "";
            const account_own_name = obj?.account_own_name ?? "";
            const account_own_surname = obj?.account_own_surname ?? "";
            return `${account_own_lastname} ${account_own_name} ${account_own_surname}`;
        }

    },
    computed: {
        list_persone() {
            return this.$store.state.formData.step_4.list_persone
        },
        getLastIndexPerson() {
            console.log(this.$store.getters.indexLastListPerson);
            return this.$store.getters.indexLastListPerson
        }
    },
    components: {
        LineStep,
    },
};
</script>
  
<style>
.structure_form_title {
    font-family: Geometria;
}

.form_block {
    font-family: Roboto;
    font-size: 14px;
}

.form_block_title {
    font-size: 12px;
    width: 300px;
}

.form_block_label {
    font-family: Roboto;
    color: black;
}

.add_btn {
    background: #F3F4F4 !important;
    color: #000 !important;
}

.auth_form_bth {
    border-radius: 10px;
    color: white !important;
    text-transform: capitalize;
    font-size: 14px;
}

.contain_btn_add {
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
}

.title_btn {
    color: #8E909B;
    font-size: 13px;
    margin-bottom: 3px;
}
</style>