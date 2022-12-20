<template>
    <v-form v-model="valid" ref="form" lazy-validation>
        <h2>Согласие на получение информационной рассылки</h2>
        <div class="form_block">
            <p class="form_block_title">Заявитель дает согласие на получение им предложений, информации о продуктах/
                услугах, рекламы и иной информации от Банка, Партнеров Банка по почте, по сетям электросвязи, в том
                числе путем контактов по телефону, электронной почте, с помощью СМС - сообщений и иными способами.</p>
            <v-radio-group v-model="currentData.is_newsletter">
                <v-radio label="Да" value="Да" />
                <v-radio label="Нет" value="Нет" />
            </v-radio-group>
        </div>

        <v-btn :disabled="!valid" @click="validate">Отправить</v-btn>
    </v-form>
</template>
<script>
import InnAndNameInput from '@/components/innAndNameInput.vue'

export default {
    data: () => ({
        currentData: {
            is_newsletter: 'Да',
        },
        valid: true,

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
                this.next();
            }
        },
        next() {
            this.$router.push({ name: "step_2" });
        },
    },
    computed: {},
    components: {
        InnAndNameInput,
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