<template>
    <div>
        <div class="all_data_table">
            <div v-for="(item, index) in isResult" :key="index" class="">
                <div v-for="(val, name) in item" :key="name" class="all_data_table-row d-flex">
                    <div class="data_table_block" v-if="val">
                        <p class="form_block_title">
                            {{isTitle(name) }}
                        </p>
                    </div>

                    <div class="data_table_block" v-if="val">
                        <div v-if="name === 'first_passport_page'" class="form_block_title d-block"> 
                            {{ val[0].name }}
                        </div>
                        <div v-else-if="isArray(val)" class="form_block_title d-block">
                            <div v-for="(val2, name2) in val" :key="name2">
                                <div v-if="isObject(val2)">
                                    <div v-for="(val3, key) in item" :key="key">
                                        <div v-if="val3">
                                            {{ isTitle(key) }} => {{ val3 }}
                                        </div>
                                    </div>
                                </div>
                                <p class="d-flex" v-else>- {{ val2 }}</p>

                            </div>
                        </div>
                        <p class="text-left form_block_title" v-else>
                            {{ val }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <v-btn elevation="2" class="card_content_button" large @click="del()">Удалить</v-btn>
        <v-btn elevation="2" class="card_content_button" large @click="add()">Добавить</v-btn>
        <v-btn elevation="2" class="card_content_button" large @click="next()">Продолжить</v-btn>
    </div>
</template>
<script>
export default {
    data() {
        return {
            formData: {},
        }
    },
    methods: {
        isObject(element){
            if (typeof element == 'object') {
                return true
            } else {
                return false
            }
        },
        isArray(element) {
            if (Array.isArray(element)) {
                return true
            } else {
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
                case 'operation_nalition': return 'Количество операций по снятию наличности в месяц'
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
                case 'mail_address': return 'Почтовый адрес'
                case 'outside_contracts_volume': return 'Количество операций по безлимитным платежам в месяц'
                case 'passport_serial': return 'Серия паспорта'
                case 'physic_address': return 'Физический адрес'
                case 'placeOfBirth': return 'Место рождения'
                case 'licence_type': return 'Тип лицензии'
                case 'licence_number': return 'Номер лицензии'
                case 'licence_date_issue': return 'Дата выдачи лицензии'
                case 'licenced_validity': return 'Срок действия'
                case 'licence_issued_by': return 'Кем выдан'
                case 'operation_volume': return 'Количество операций по безлимитным платежам в месяц'
                case 'planned_operations': return 'Сведения о планируемых опреациях по счету'
                case 'start_date': return 'Дата начала действия'
                case 'supreme_management_body': return 'Тип'
                case 'supreme_management_inn': return 'Инн'
                case 'supreme_management_type': return 'Роль'
                case 'validity': return 'Срок действия'
                case 'contact_number': return 'Номер телефона'
                case 'inn': return 'ИНН'
                case 'addresses': return 'Адресс'
                case 'supreme_management_person': return 'Тип Руководителя'
                case 'collegiate_person_fio': return 'Члены коллегиального исполнительного органа'
                case 'account_own_gender': return 'Пол'
                case 'doc_number': return 'Номер документа удостоверяющего личность'
                case 'doc_serial': return 'Серия документа удостоверяющего личность'
                case 'doc_type': return 'Тип документа удостоверяющего личность'
                case 'licenced_activity': return 'Перечень видов лицензируемой деятельности'
                case 'name': return 'Наименование'
                case 'ogrn': return 'ОГРН'
                case 'supervisory': return 'Наименования наблюдательного совета'
                case 'first_passport_page': return 'Паспорт'
                default: return element
            }
        },
        del(){
            this.$router.push("/sctructure")
        },
        add(){
            this.$store.commit('setListSupervisoryBoardPersone')
            this.$router.push("/individual-info")
        },
        next(){
            this.$store.commit('setListSupervisoryBoardPersone')
            this.$router.push("/sctructure")
        }
    },
    computed: {
        isResult() {
            return this.$store.state.supervisoryBoardPersone;
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