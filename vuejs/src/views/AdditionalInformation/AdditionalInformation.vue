<template>
    <v-form v-model="valid" ref="form" lazy-validation>
        <p class="text-left form_block_title"><span class="star">*</span>Дополнительная информация о ЕИО</p>
        <v-radio-group v-model="eioType">
            <v-radio
                label="ЕИО является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)"
                value="1" />
            <v-radio
                label="ЕИО не является публичным должностным лицом или лицом, связанным с публичным должностным лицом родственными, партнерскими или иными отношениями (Отец, Мать, Брат, Сестра, Супруг(а), Сын, Дочь, Бабушка, Дедушка, Внук\внучка, Усыновленный, Усыновитель)"
                value="2" />
        </v-radio-group>
        <v-btn :disabled="!valid" @click="validate">Отправить</v-btn>
    </v-form>
</template>
<script>
import { VueMaskDirective } from "vue-the-mask";

export default {
    directives: { mask: VueMaskDirective },
    data: () => ({
        currentData: {
            eioType: ""
        },
        valid: true,

        requiredRules: [(v) => !!v || "Это поле обязательно"],

    }),

    async mounted() {


    },

    methods: {
        validate() {
            this.$refs.form.validate();

            if (this.$refs.form.validate()) {
                this.$store.dispatch('addObjectFormData', {
                    object: 'step_1',
                    value: this.currentData
                });
                // this.$store.commit('addItemFormData', this.currentData)
                this.next();
            }
        },
        next() {
            this.$router.push({ name: "step_2" });
        },

    },
    computed: {},
    components: {
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

.combobox .v-icon {
    display: none;
}
</style>