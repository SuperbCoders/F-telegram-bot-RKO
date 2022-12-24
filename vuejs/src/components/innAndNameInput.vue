<template>
    <div class="container_field">
        <input type="text" class="input" placeholder="Введите ИНН или наименование компании" :value="valueField"
            @input="emitData" />
        <div class="dropdown_modal" v-if="list.length > 0">
            <div class="field" v-for="(company, key) in list_company" :key="key"
                @click="selectCompany(company.value, company.data.inn, company.data.ogrn)">
                <div class="name">{{ company.value }}</div>
                <div class="sub_info" v-html="sub_info(company.data.inn, company.data.ogrn)"></div>
            </div>
        </div>
    </div>

</template>
<script>
import { getCompanyName } from "@/api/getInfoCompany";

export default {
    name: "innAndNameInput",
    props: {},
    data() {
        return {
            list: [],
            name: "",
            valueField: "",
        }
    },
    methods: {
        async selectCompany(name, inn, ogrn) {
            this.valueField = name;
            this.list = [];
            this.$emit('input', {
                name,
                inn,
                ogrn,
            })
        },

        async emitData(e) {
            const value = e.target.value;

            this.valueField = value;
            const data = await getCompanyName(value);
            console.log(data);
            this.list = data.suggestions;

        },
        findValueAndFormat(number) {

            const start_index = `${number}`.indexOf(`${this.valueField}`);
            const end_index = this.valueField.length;

            if (start_index >= 0 && end_index >= 0) {
                const start_chars = this.valueField;
                const end_chars = `${number}`.slice(end_index);
                return `<span style="color: #b36b24">${start_chars}</span>${end_chars}`;
            }

            return `${number}`;
        },
        sub_info(inn, ogrn) {
            const valid_inn = this.findValueAndFormat(inn);
            const valid_ogrn = this.findValueAndFormat(ogrn);

            return `ИНН ${valid_inn}, ОГРН ${valid_ogrn}`
        },
    },
    computed: {
        list_company() {
            return this.list.slice(0, 4);
        }
    }
}
</script>
<style scoped>
.container_field {
    position: relative;
    margin-bottom: 8px;
}

.field {
    padding: 10px 14px;
    cursor: pointer;
}

.field:hover {
    background: rgba(0, 0, 0, 0.02);
}

.sub_info {
    text-transform: uppercase;
    font-size: 13px;
    color: #706f6f;
}

.name {
    font-weight: bold;
    text-transform: uppercase;
    color: #424242;
}

.dropdown_modal {
    position: absolute;
    top: calc(100% + 2px);
    left: 0;
    width: 100%;
    background: #fff;
    z-index: 100;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
}

.input {
    width: 100%;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    padding: 16px 12px;
}

.input::-webkit-input-placeholder {
    /* WebKit browsers */
    color: #b9b9b9;
}

.input:-moz-placeholder {
    /* Mozilla Firefox 4 to 18 */
    color: #b9b9b9;
}

.input::-moz-placeholder {
    /* Mozilla Firefox 19+ */
    color: #b9b9b9;
}

.input:-ms-input-placeholder {
    /* Internet Explorer 10+ */
    color: #b9b9b9;
}
</style>