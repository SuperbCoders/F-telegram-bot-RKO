<template>
    <v-form ref="form" v-model="valid" lazy-validation>
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <h2 class="text-left mb-4">Учредители - юридические лица</h2>
        <div v-for="(itemForm, index) in currentData.founders" :key="index" class="form_input_block checkboxs">

            <div class="form_block">
                <p class="text-left form_block_title">Учередитель</p>
                <InnAndNameInput @input="({ inn, name, ogrn }) => {
    itemForm.inn = inn;
    itemForm.name = name;
    itemForm.ogrn = ogrn;
}" :value="itemForm.name" />
            </div>

            <div class="form_block mt-6">
                <p class="text-left form_block_title">Доля в уставном капитале</p>
                <v-text-field outlined v-model="itemForm.share" placeholder="Доля в уставном капитале"
                    class="mt-1 auth_form" v-mask="'###'">
                </v-text-field>
            </div>
        </div>
        <div class="form_block d-flex align-center justify-center">
            <a @click="deleteGroupList" :class="{ form_block_delete_link_delete: currentData.founders.length <= 1 }"
                class="form_block_delete_link text-decoration-none" href="#">
                <img src="@/assets/trash.svg" alt="">
                <span class="pl-2 ">Удалить</span>
            </a>
            <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="addGroupList()">
                <span class="pr-2">Добавить</span>
                <img src="@/assets/plus-circle.svg" alt="">
            </v-btn>
        </div>
        <line-step :step="7" />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
    </v-form>
</template>
<script>
import { mask } from "vue-the-mask";
import InnAndNameInput from '@/components/innAndNameInput.vue'
import LineStep from "@/components/line_step/line_step.vue";
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
            founders: [{
                inn: "",
                share: "",
                name: "",
                ogrn: "",
            }],
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

        if (this.$store.state.formData.step_1.opf.short !== "ИП") {
            this.next();
        }

    },

    methods: {
        validate() {
            this.$refs.form.validate();

            if (this.$refs.form.validate()) {
                this.$store.dispatch('addObjectFormData', {
                    object: 'step_7',
                    value: this.currentData
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

        addGroupList() {
            const defaultGroupItem = {
                inn: "",
                share: "",
                name: "",
                ogrn: "",
            };
            this.currentData.founders.push(defaultGroupItem);
        },
        deleteGroupList() {
            if (this.currentData.founders.length > 1) {
                this.currentData.founders.pop();
            }
        },

    },
    computed: {},
    components: {
        InnAndNameInput,
        LineStep,
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