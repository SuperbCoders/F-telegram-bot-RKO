<template>
    <div class="auth_section">
        <v-form ref="form" v-model="valid" lazy-validation>

            <div class="form_block">
                <p class="text-left form_block_title">Email</p>
                <v-text-field type="email" id="oldName" label="Email" class="align-center border-none" name="oldName"
                    v-model="currentData.email" outlined :rules="requiredRules"
                    v-mask="/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/" masked="true"
                    :required="true"></v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Телефон</p>
                <v-text-field label="Контактный номер телефона" outlined v-model="currentData.phoneNumber"
                    :rules="requiredRules" :required="true" v-mask="'+# (###) ### ## ##'" masked="true"
                    class="mt-1 auth_form">
                </v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Доменное имя, указатель страницы сайта в сети "Интернет", с
                    использованием которых юридическим лицом оказываются услуги</p>
                <v-text-field label="Контактный номер телефона" outlined v-model="currentData.domainName"
                    :rules="requiredRules" v-mask="'+# (###) ### ## ##'" masked="true" class="mt-1 auth_form">
                </v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Факс</p>
                <v-text-field label="Факс" outlined v-model="currentData.domainName" :rules="requiredRules"
                    v-mask="'+# (###) ### ## ##'" masked="true" class="mt-1 auth_form">
                </v-text-field>
            </div>
        </v-form>
        <line-step :step="1" />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
    </div>
</template>
  
<script>
import LineStep from "@/components/line_step/line_step.vue";
import { VueMaskDirective } from "vue-the-mask";

export default {
    directives: { mask: VueMaskDirective },
    data: () => ({
        currentData: {
            email: null,
            phoneNumber: null,
            domainName: null,
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

.combobox .v-icon {
    display: none;
}
</style>