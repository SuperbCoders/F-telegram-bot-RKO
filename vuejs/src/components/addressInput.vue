<template>
    <div class="container_field">
        <input type="text" class="input" @focus="focusInput" :placeholder="label"
            @input="emitData" :value="value">
        <div class="dropdown_modal" v-if="is_modal && list_address.length > 0">
            <div class="field" v-for="(address, key) in list_address" :key="key" @click="selectAddress(address)">
                <div class="name">{{ address }}</div>
            </div>
        </div>
    </div>
</template>
<script>

import { getAddress } from '@/api/getAddress';

export default {
    props: {
        index: {
            type: Number,
            default: 0,
        },
        value: {
            type: String,
            default: "",
        },
        label: {
            type: String,
        }
    },
    data() {
        return {
            list_address: [],
            address_field: "",
            is_modal: false,
        }
    },
    methods: {
        async getAddressFromName(val) {
            const data = await getAddress(val);
            this.list_address = data.suggestions.map((elem) => {
                return `${elem.value}`
            }) || [];
        },
        selectAddress(address) {
            this.getAddressFromName(address);
            this.is_modal = false;
            this.$emit('input', address)
        },
        emitData(e) {
            const val = e.target.value;
            console.log(123);
            this.getAddressFromName(val);
            this.$emit('input', val)
        },
        focusInput() {
            this.is_modal = true;
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
    max-height: 200px;
    overflow: auto;
}

.input {
    width: 100%;
    border: 1px solid #d6d6d6;
    border-radius: 8px;
    padding: 16px 12px;
    outline: none;
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