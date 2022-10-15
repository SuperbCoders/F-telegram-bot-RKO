<template>
    <div>
        <div>
            <span>ИНН</span>
        </div>
        {{  test(List) }}
        <div class="all_data_table">
            <div class="all_data_table-row d-flex">
                <div class="data_table_block">
                    <p class="form_block_title ">
                        Ключ
                    </p>
                </div>
                <div class="data_table_block">
                    <p class="form_block_title">
                       Значение
                    </p>
                </div>
                <hr>
            </div>
            <div v-for="(item, index) in Object.entries(isResult)" :key="index" class="all_data_table-row d-flex">
                <div class="data_table_block">
                    <p class="form_block_title">
                        {{isTitle(item[0]) }}
                    </p>
                </div>
                <div class="data_table_block">
                    <p class="form_block_title">
                        {{ test(item[1]) }}
                    </p>
                </div>
                <hr>
            </div>
        </div>
        <v-btn elevation="2" class="card_content_button" large @click="sendData()">Отправить</v-btn>
    </div>
</template>
<script>
export default {
    data() {
        return {
            formData: {},
            List: ['fwwfawfa', 'gagawgwg', 'wgawagwaggwa']
        }
    },
    methods: {
        async sendData() {
            this.$store.commit('IsFormData')
            this.isResult = new FormData();
            await fetch("http://localhost:8000/loan-application/create/", {
                method: "POST",
                body: this.isResult,
            })

            this.$router.push("/already")
        },
        test (element) {
            if (Array.isArray(element)) {
                element.map((item) => {
                    console.log('элемент', item)
                    return item
                })
            } else {
                return element
            }
        },
        isTitle (element) {
            switch (element) {
                case 'tariff': return 'Тариф'
                case 'account_birth_place': return 'Место рождения'
                case 'account_onw_inn': return 'Инн'
                case 'account_onw_role': return 'Роль'
                case 'account_own_citizenship': return 'Гражданство'
                case 'account_own_firstname': return 'Имя'
                case 'account_own_lastname': return 'Фамилия'
                case 'account_own_surname': return 'Отчество'
                case 'account_own_mail': return 'Адрес фактического проживания'
                case 'account_own_name': return 'Пол'
                case 'account_own_phone': return 'Телефон'
                case 'account_own_piece': return 'Доля владения'
                case 'account_own_registration': return 'Адрес регистрации'
                case 'account_own_snils': return 'Снилс'
                case 'accownt_own_living': return 'Адрес проживания'
                // case 'tariff': return 'Тариф'
            }
        }
    },
    computed: {
        isResult() {
            return this.$store.state.result;
        }
    },
    mounted() {
        this.$store.commit('IsFormData')
    },
}
</script>
<style>
.card_content_button {
    width: 100%;
    box-shadow: 0 0 4px #00000030;
    background: #d41367 !important;
    border-radius: 6px;
    margin-top: 20px;
    font-family: Roboto;
    font-size: 14px !important;
    color: #fff !important;
    font-weight: 500;
    padding: 16px 30px !important;
    text-transform: none;
}

.all_data_table {
    width: 100%;
}

.data_table_block {
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.form_block_title {
    display: flex;
    align-items: center;
    justify-content: flex-start;
}
.all_data_table-row  {
}
</style>