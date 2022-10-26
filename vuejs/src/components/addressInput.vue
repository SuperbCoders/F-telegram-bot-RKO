<template>
        <v-combobox :label="label" outlined required class="mt-1 combobox" 
            @keyup="getAddressFromName"
            @input="emitData"
            :value="value"
            :items="list_item"
            
            ></v-combobox>
</template>
<script>

import { getAddress } from '../api/GetAddress';

export default {
    props: {
        label: {
            type: String,
        },
        value: {
            type: String
        }

    },
    data() {
        return {
            list_item: [],
        }
    },
    methods: {
        async getAddressFromName(e) {
            const value = e.target.value;
            const data = await getAddress(value);
            this.list_item = data.suggestions.map((elem) => `${elem.value}`) || [];
        },
        emitData(e) {
            this.$emit('input', e)
        }
    }
}
</script>
<style scoped>

</style>