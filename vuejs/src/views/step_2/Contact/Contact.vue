<template>
    <div class="auth_section">
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <h2 class="mb-4">Контакты</h2>
        <v-form ref="form" v-model="valid" lazy-validation>

            <div class="form_block">
                <p class="text-left form_block_title"><span class="star">*</span>Email</p>
                <v-text-field type="email" id="oldName" label="Email" class="align-center border-none" name="oldName"
                    v-model="currentData.email" outlined :rules="emailRules"></v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title"><span class="star">*</span>Телефон</p>
                <v-text-field placeholder="+7 (000) 000 00 00" outlined v-model="currentData.contact_phone_number" :rules="requiredRules"
                    :required="true" v-mask="'+# (###) ### ## ##'" masked="true" class="mt-1 auth_form">
                </v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Сайт компании</p>
                <v-text-field placeholder="domain.ru" outlined v-model="currentData.donainname" class="mt-1 auth_form">
                </v-text-field>
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Факс</p>
                <v-text-field type="text" placeholder="7-000-000-0000" v-mask="'#-###-###-####'" masked="true" outlined v-model="currentData.fax" class="mt-1 auth_form">
                </v-text-field>
            </div>
        </v-form>
        <line-step :step="number_step" />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
    </div>
</template>

<script>
import LineStep from "@/components/line_step/line_step.vue";
import { mask } from "vue-the-mask";
import { loadCurrentData } from '@/utils/loadStore'

export default {
    directives: { mask },
    props: {
        number_step: {
            type: Number,
        }
    },
    data: () => ({
        currentData: {
            email: null,
            contact_phone_number: null,
            donainname: null,
            fax: null
        },

        valid: true,

        requiredRules: [(v) => !!v || "Это поле обязательно"],
        emailRules: [(v) => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.exec(v) !== null || "В это поле нужно написать Email"],

    }),

    async mounted() {
        const step_data = this.$store.state.formData.step_1;
        const phone_number = step_data.contact_number;
        this.currentData.contact_phone_number = phone_number;
        console.log(phone_number);

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

        onClose() {
            // this.$refs.email.blur();
            // this.$refs.contact_phone_number.blur();
            // this.$refs.donainname.blur();
            // this.$refs.fax.blur();
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