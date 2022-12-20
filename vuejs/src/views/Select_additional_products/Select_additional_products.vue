<template>
    <v-form v-model="valid" ref="form" lazy-validation>
        <div class="form_block">
            <h2 class="text-left">
                Выберите дополнительные продукты к подключению
            </h2>
            <v-checkbox v-model="currentData.additional_products.sms" class="checkboxs" label="СМС-оповещение" value="СМС-оповещение"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.internet_acquiring" class="checkboxs" label="Интернет-эквайринг" value="Интернет-эквайринг"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.merchant_acquiring" class="checkboxs" label="Торговый-эквайринг" value="Торговый-эквайринг"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.community" class="checkboxs" label="Комьюнити" value="Комьюнити"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.Accounting" class="checkboxs" label="Бухгалтерия" value="Бухгалтерия"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.legal_support" class="checkboxs" label="Юридическая поддержка" value="Юридическая поддержка"
                hide-details>
            </v-checkbox>
            <v-checkbox v-model="currentData.additional_products.promotion" class="checkboxs" label="Продвижение" value="Продвижение"
                hide-details>
            </v-checkbox>
        </div>

        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
    </v-form>
</template>
<script>

export default {
    data: () => ({
        currentData: {
            additional_products: [
            ],

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
                this.next();
            }
        },
        next() {
            this.$router.push({ name: "step_2" });
        },

        addGroupList() {
            const defaultGroupItem = {
                founder_inn: null,
                capital: null,
            };
            this.currentData.addresses.push(defaultGroupItem);
        },
        deleteGroupList() {
            if (this.currentData.addresses.length > 1) {
                this.currentData.addresses.pop();
            }
        },

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