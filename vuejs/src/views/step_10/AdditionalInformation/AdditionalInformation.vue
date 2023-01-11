<template>
    <div>
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>

        <v-form v-model="valid" ref="form" lazy-validation>
            <p class="text-left form_block_title"><span class="star">*</span>Дополнительная информация о ЕИО</p>
            <v-radio-group v-model="currentData.additional_inforamtion" class="checkboxs">
                <v-radio
                    label="ЕИО является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)"
                    value="ЕИО является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)" />
                <v-radio
                    label="ЕИО не является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)"
                    value="ЕИО не является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)" />
            </v-radio-group>
            <line-step :step='number_step' />
            <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
                Продолжить
            </v-btn>
        </v-form>
    </div>

</template>
<script>
import LineStep from '@/components/line_step/line_step.vue';
import { loadCurrentData } from '@/utils/loadStore'

export default {
    props: {
        number_step: {
            type: Number,
        }
    },
    data: () => ({
        currentData: {
            additional_inforamtion: ""
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
                });
                // this.$store.commit('addItemFormData', this.currentData)
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
        LineStep
    }
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

.purposes_block .v-label {
    color: #323E48 !important;
}

.checkboxs label {
    color: #323E48 !important;
}
</style>