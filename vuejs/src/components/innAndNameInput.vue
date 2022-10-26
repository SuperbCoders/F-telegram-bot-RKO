<template>
    <v-combobox label="Введите ИНН или название компании" outlined
       required 
        class="mt-1 auth_form combobox"
        :value="value"
        @keyup="getListCompanyFromName" 
        :items="list"
        >
    </v-combobox>
</template>
<script>
import { getCompanyName } from "../api/getInfoCompany";

export default {
    name: "innAndNameInput",
    props: {
        value: {
            type: String
        }
    },
    data() {
        return {
            list: [],
            inn: "",
            name: "",
        }
    },
    methods: {
        async getListCompanyFromName(e) {
            const value = e.target.value;
            const data = await getCompanyName(value);
            if (value.match(/^\d+/)) {
                this.list = data.suggestions.map((elem) => elem.data.inn);
            } else {
                this.list = data.suggestions.map((elem) => `${elem.value}, ${elem.data?.address?.unrestricted_value}`);
            }
            this.$emit("input", value);
        },

        emitData(e){
            this.$emit("input", e);
            // if (value.match(/^\d+/)) {
            //     this.$emit("inn", e);
            // } else {
            //     this.$emit("name", e);
            // }
        }
    }
}
</script>
<style>

</style>