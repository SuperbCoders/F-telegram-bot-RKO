<template>
    <!-- <v-combobox label="Введите ИНН или наименование компании" outlined
       required 
        class="mt-1 auth_form combobox"
        :value="value"
        @input="emitData"
        @keyup="getListCompanyFromName" 
        :items="list"
        >
    </v-combobox> -->
    <input type="text" class="input">
</template>
<script>
import { getCompanyName } from "@/api/getInfoCompany";

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
            ogrn: "",
        }
    },
    methods: {
        async getListCompanyFromName(e) {
            const value = e.target.value;
            const data = await getCompanyName(value);
            console.log(data);
            if (value.match(/^\d+/)) {
                this.list = data.suggestions.map((elem) => elem.data.inn);
            } else {
                this.list = data.suggestions.map((elem) => `${elem.value}, ${elem.data?.address?.unrestricted_value}`);
            }
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
<style scoped>
.input {
    width: 100%;
    height: 40px;
    border: 1px solid #000;
}
</style>