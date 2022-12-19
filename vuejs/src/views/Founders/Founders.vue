<template>
    <v-form ref="form" v-model="valid" lazy-validation>
        <div v-for="(itemForm, index) in currentData.addresses" :key="index" class="form_input_block checkboxs">

            <div class="form_block">
                <p class="text-left form_block_title">Учередитель</p>
                <InnAndNameInput @input="({inn})=>{currentData.founder_inn = inn}" />
            </div>

            <div class="form_block">
                <p class="text-left form_block_title">Доля в уставном капитале</p>
                <v-text-field outlined v-model="currentData.capital"
                    class="mt-1 auth_form">
                </v-text-field>
            </div>
        </div>
        <div class="form_block d-flex align-center justify-center">
            <a @click="deleteGroupList" :class="{ form_block_delete_link_delete: currentData.addresses.length <= 1 }"
                class="form_block_delete_link text-decoration-none" href="#">
                <img src="@/assets/trash.svg" alt="">
                <span class="pl-2 ">Удалить</span>
            </a>
            <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="addGroupList()">
                <span class="pr-2">Добавить</span>
                <img src="@/assets/plus-circle.svg" alt="">
            </v-btn>
        </div>
        <line-step :step="1" />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
    </v-form>
</template>
<script>
import { VueMaskDirective } from "vue-the-mask";
import InnAndNameInput from '@/components/innAndNameInput.vue'

export default {
    directives: { mask: VueMaskDirective },
    data: () => ({
        currentData: {
            addresses: [
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
                // this.$store.commit('addItemFormData', this.currentData)
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