<template>
    <div>
        <div>
        </div>
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
                    <div v-if="test(item[1])" class="form_block_title d-block">
                        <!-- <div v-if="test(item[1])"></div> -->
                        <div v-for="(item, index) in item[1]" :key="index">
                            <p class="d-flex">{{ index + 1}}) {{ item }}</p>
                        </div>
                    </div>
                    <p class="text-left form_block_title" v-else>
                        {{ item[1] }}
                    </p>
                    {{ typeof item[1] === 'object' && Array.isArray(item[1])}}
                    <div v-if="typeof item[1] === 'object' && !Array.isArray(item)">
                        <h1>wa'gjgaeiw</h1>
                    </div>
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
            this.FormData = new FormData();
            this.FormData.append("test", 1);

            await fetch("http://localhost:8000/loan-application/create/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify(this.isResult),
            })

            this.$router.push("/already")
        },
        test(element) {
            if (Array.isArray(element)) {
                return true
            } else if (element !== '' || null) {
                return false
            }
        },
        isTypeObject(object) {
            if (Array.isArray(object)) {
                return ''
            }
            return ''
        },
        isTitle(element) {
            switch (element) {
                case 'tariff': return 'Тариф'
                case 'account_birth_place': return 'Место рождения'
                case 'account_datebirth': return 'Дата рождения'
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
                case 'account_operations': return 'Рассчетно касовое обслуживание'
                case 'accownt_own_living': return 'Адрес проживания'
                case 'assigned_publ_pers_registraion': return 'Адрес регистрации'
                case 'assigned_publ_pers_relation': return 'Степень родства либо статус (супруг или супруга) по отношению кпубличному должностному лицу'
                case 'beneficiaries': return 'Выгодоприобретатели'
                case 'cash_source': return 'Источники происхождения денежных средств'
                case 'collegiate_body': return 'Наименования наблюдательного совета'
                case 'collegiate_person': return 'Наименование коллегиального исполнительног органа'
                case 'company_group_name': return 'Наименование группы компаний'
                case 'company_name': return 'Наименование группы компаний'
                case 'salary_debt': return 'Задолжность по зп'
                case 'state_employers': return 'Штатная численость сотрудников'
                case 'sum_per_month': return 'Сумма по снятию за месяц'
                case 'date_issue': return 'Дата выдачи'
                case 'division_code': return 'Код подразделения'
                case 'employers_volume': return 'Численность персонала'
                case 'end_date': return 'Дата окончания действия'
                case 'groupList': return 'Список групп'
                case 'group_members': return 'Состав группы компаний'
                case 'issued_by': return 'Кем выдан'
                case 'legal_address': return 'Юридический адрес'
                case 'mail_address': return 'Количество операций по безлимитным платежам в месяц'
                case 'outside_contracts_volume': return 'Количество операций по безлимитным платежам в месяц'
                case 'passport_number': return 'Номер паспорта'
                case 'passport_serial': return 'Серия паспорта'
                case 'physic_address': return 'Физический адрес'
                case 'placeOfBirth': return 'Место рождения'
                case 'operation_volume': return 'Количество операций по безлимитным платежам в месяц'
                case 'planned_operations': return 'Сведения о планируемых опреациях по счету'
                case 'start_date': return 'Дата начала действия'
                case 'supreme_management_body': return 'Тип'
                case 'supreme_management_inn': return 'Инн'
                case 'supreme_management_type': return 'Роль'
                case 'typeDocumnet': return 'Тип документа'
                case 'validity': return 'Срок действия'
                // case 'accownt_own_living': return 'Адрес проживания'
                // case 'tariff': return 'Тариф'
            }
        }
    },
    computed: {
        isResult() {
            return this.$store.state.result;
        },
        // isValueString (value) {
        //   if (value[1] !== '' && null) {
        //     return true
        //   }
        // }
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
    align-items: flex-start;
    justify-content: center;
}

.form_block_title {
    display: flex;
    align-items: center;
    justify-content: flex-start;
}

.all_data_table-row {}
</style>