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
    <input type="text" class="input" placeholder="Введите ИНН или наименование компании">
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
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    padding: 16px 10px;
}

.input::-webkit-input-placeholder { /* WebKit browsers */
   color: #b9b9b9;
}
.input:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
   color:    #b9b9b9;
}
.input::-moz-placeholder { /* Mozilla Firefox 19+ */
   color:    #b9b9b9;
}
.input:-ms-input-placeholder { /* Internet Explorer 10+ */
   color:    #b9b9b9;
}
</style>