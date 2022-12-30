<template>
    <div class="approvals_section">
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <div class="form_block">
            <p class="text-left form_block_input"><span class="star">*</span>Кодовое слово</p>
            <input type="text" @input="inputCodeword" class="mt-1 auth_form input" ref="codewords"
                placeholder="Кодовое слово" :required="true">
        </div>
        <LineStep :step="12" class="mt-5" />
        <v-btn block large @click="redirect()" class="mt-10 auth_form_bth" color="primary">
            Продолжить
        </v-btn>
    </div>
</template>
  
<script>
import LineStep from "@/components/line_step/line_step.vue";
import { loadCurrentData } from '@/utils/loadStore'
import { mask } from "vue-the-mask";

export default {
    directives: { mask },
    props: {
        number_step: {
            type: Number,
        }
    },
    components: {
        LineStep,
    },
    data() {
        return {
            currentData: {
                codeword: "",

            },
        };
    },
    methods: {
        redirect() {
            this.$store.dispatch('addObjectFormData', {
                object: 'step_12',
                value: this.currentData
            })
            this.next();
        },
        onClose() {
            this.$refs.codeword.blur()
        },
        inputCodeword(event) {
            const val = event.target.value;
            let replace_text = val.replaceAll(/[^АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя ]/g, "");
            if (replace_text.length >= 35) {
                replace_text = replace_text.slice(0, 35);
            }
            this.currentData.codeword = replace_text;
            this.$refs.codewords.value = replace_text;
        },
        toggleText(e) {
            e.preventDefault();
        },
        next() {
            this.$router.push({ name: `step_${this.number_step + 1}` });
        },
        back() {
            this.$router.push({ name: `step_${this.number_step - 1}` });
        },
    },
    computed: {
        isList() {
            if (this.currentData.informationGoals.length >= 1) {
                return true;
            }
            return false;
        },
        formatCodeword() {
            const replace_text = this.currentData.codeword.replaceAll(/[^АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]/g, "");
            console.log(replace_text);
            return replace_text
        },
    },
    mounted() {
        loadCurrentData({
            currentData: this.currentData,
            step: `step_${this.number_step}`,
            vue: this,
        });
    },
};
</script>
  
<style scoped>
.input {
    width: 100%;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    padding: 16px 12px;
}

.v-input__slot {
    display: flex;
    align-items: flex-start;
}

.toggleText {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.checkboxs label {
    color: #323E48 !important;
}
</style>