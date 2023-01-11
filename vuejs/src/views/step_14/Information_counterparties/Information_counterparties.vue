<template>
    <div>
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <v-form v-model="valid" ref="form" lazy-validation>
            <h2>Сведения о контрагентах</h2>
            <div class="form_block">
                <p class="text-left form_block_title">
                    Имеются постоянные или предполагаемые плательщики по операциям с
                    денежными средствами на счете
                </p>
                <v-radio-group v-model="currentData.information_counterparties" class="checkboxs">
                    <v-radio label="Имеются" value="Имеются" />
                    <v-radio label="Не имеются" value="Не имеются" />
                </v-radio-group>
            </div>

            <div class="form_block" v-if="currentData.information_counterparties == 'Имеются'">
                <p class="text-left form_block_title">Наименование организации</p>
                <v-text-field label="Наименование организации" outlined v-model="currentData.name_organization"
                    class="mt-1 auth_form">
                </v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Имеются постоянные или предполагаемые получатели по операциям с
                    денежными средствами на счете </p>
                <v-radio-group v-model="currentData.information_counterparties_two" class="checkboxs">
                    <v-radio label="Имеются" value="Имеются" />
                    <v-radio label="Не имеются" value="Не имеются" />
                </v-radio-group>
            </div>

            <div class="form_block" v-if="currentData.information_counterparties_two == 'Имеются'">
                <p class="text-left form_block_title">Наименование организации</p>
                <v-text-field label="Наименование организации" outlined v-model="currentData.name_organization_two"
                    class="mt-1 auth_form">
                </v-text-field>
            </div>

            <LineStep :step="number_step" class="mt-5" />

            <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary"
                @click="validate">Продолжить
            </v-btn>
        </v-form>
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
        currentData: {
            information_counterparties: null,
            information_counterparties_two: null,

            name_organization: null,
            name_organization_two: null,
        },
        valid: true,

        requiredRules: [(v) => !!v || "Это поле обязательно"],

    }),

    async mounted() {
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
                this.$store.dispatch('addObjectFormData', {
                    object: `step_${this.number_step}`,
                    value: this.currentData
                })
                this.next();
            }
        },
        next() {
            this.$router.push({ name: `step_${this.number_step + 1}` });
        },
        back() {
            this.$router.push({ name: `step_${this.number_step - 1}` });
        },
    },
    computed: {},
    components: {
        LineStep,
    },
};
</script>
<style scoped>
.auth_title_block {
    margin-top: 30px;
}

.auth_form {
    border-radius: 8px;
    font-family: face;
}

.auth_form_bth {
    border-radius: 10px;
    text-transform: capitalize;
    font-size: 14px;
    font-weight: 400;
}

.auth_form_link_container {
    font-size: 14px;
}

.combobox .v-icon {
    display: none;
}
</style>