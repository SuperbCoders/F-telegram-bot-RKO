<template>
    <div class="approvals_section">
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <div class="form_block">
            <v-text-field label="Кодовое слово" @input="inputCodeword" outlined :value="formatCodeword" :required="true"
                class="mt-1 auth_form">
            </v-text-field>
        </div>
        <LineStep :step="12" class="mt-5" />
        <v-btn block large @click="redirect()" class="mt-10 auth_form_bth" color="primary">
            Продолжить
        </v-btn>
    </div>
</template>
  
<script>
import LineStep from "@/components/line_step/line_step.vue";
export default {
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
            const replace_text = val.replaceAll(/[^АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя]/g, "");
            console.log(replace_text);
            this.currentData.codeword = replace_text;
        },
        toggleText(e) {
            e.preventDefault();
        },
        next() {
            this.$router.push({ name: "step_13" });
        },
        back() {
            this.$router.push({ name: "step_11" });
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
};
</script>
  
<style>
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