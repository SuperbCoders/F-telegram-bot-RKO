<template>
  <div>
    <v-dialog v-model="dialog" width="700">
      <v-card>
        <v-card-text class="pa-5">
          <div style="text-align: center">
            <v-icon large color="pink darken-1" style="font-size: 100px">
              mdi-check-circle-outline
            </v-icon>
          </div>
          <div style="font-size: 24px; font-weight: bold" class="black--text mt-4 text-center">
            Ваша заявка успешно отправлена!
          </div>

          <div class="mt-4 text-center" style="font-size: 12px">
            В ближайшее время с вами свяжутся
          </div>
        </v-card-text>
      </v-card>
    </v-dialog>
    <div></div>
    <div class="all_data_table">
      <div class="data_table-row-title d-flex">
        <div class="data_table_block">
          <p class="form_block_title">Вопрос</p>
        </div>
        <div class="data_table_block">
          <p class="form_block_title">Ответ</p>
        </div>
      </div>
      <hr />
      <div v-for="(item, index) in Object.entries(isResult)" :key="index" class="all_data_table-row mt-1">
        <div v-if="item[1]">
          <div class="d-flex data1_table_block mt-5">
            <div class="data_table_block" v-if="item[1]">
              <p class="form_block_title">
                {{ isTitle(item[0]) }}
              </p>
            </div>
            <div class="data_table_block" v-if="item[1]">
              <div v-if="isArray(item[1])" class="form_block_title d-block">
                <div v-if="isArray(item[1])"></div>
                <div v-for="(item, index) in item[1]" :key="index">
                  <div v-if="isObject(item) ">
                    <div v-for="(val, key) in item" :key="key">
                      <div>
                        {{ isTitle(key) }} =>
                        <p v-if="!isObject(val)">{{ val }}</p>
                      </div>
                      <div v-if="isObject(val)">
                        <div v-for="(elementObject, indexObject) in val" :key="indexObject">
                          - {{ elementObject }}
                        </div>
                      </div>
                    </div>
                  </div>
                  <p class="d-flex" v-else>- {{ item }}</p>
                </div>
              </div>
              <p class="text-left form_block_title" v-else-if="typeof item[1] == 'boolean'">
                <span v-if="item[1]">Да</span>
                <span v-else>Нет</span>
              </p>
              <p class="text-left form_block_title" v-else>
                {{ item[1] }}
              </p>
              <div v-if="typeof item[1] === 'object' && !Array.isArray(item)"></div>
            </div>
          </div>
          <hr />
        </div>
      </div>
    </div>
    <line-step :step="19" class="mt-10" />
    <v-btn elevation="2" class="card_content_button mt-10" large @click="sendData()">Отправить</v-btn>
  </div>
</template>
<script>
import LineStep from '../../components/line_step/line_step.vue';

export default {
    data() {
        return {
            dialog: false,
            formData: {},
        };
    },
    methods: {
        async sendData() {
            this.$store.commit("IsFormData");
            this.FormData = new FormData();
            this.FormData.append("test", 1);
            await fetch("https://rko-bot.spaaace.io/api/loan-application/create/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=utf-8",
                },
                body: JSON.stringify(this.isResult),
            });
            this.dialog = true;
        },
        isObject(element) {
            if (typeof element == "object") {
                return true;
            }
            else {
                return false;
            }
        },
        isArray(element) {
            if (Array.isArray(element)) {
                return true;
            }
            else {
                return false;
            }
        },
        isTypeObject(object) {
            if (Array.isArray(object)) {
                return "";
            }
            return "";
        },
        isTitle(element) {
            switch (element) {
                case "tariff":
                    return "Тариф";
                case "account_birth_place":
                    return "Место рождения";
                case "account_datebirth":
                    return "Дата рождения";
                case "account_onw_inn":
                    return "Инн";
                case "account_onw_role":
                    return "Роль";
                case "account_own_citizenship":
                    return "Гражданство";
                case "account_own_firstname":
                    return "Имя";
                case "account_own_lastname":
                    return "Фамилия";
                case "account_own_surname":
                    return "Отчество";
                case "account_own_mail":
                    return "Адрес фактического проживания";
                case "account_own_name":
                    return "Пол";
                case "account_own_phone":
                    return "Телефон";
                case "account_own_piece":
                    return "Доля владения";
                case "operation_nalition":
                    return "Количество операций по снятию наличности в месяц";
                case "account_own_registration":
                    return "Адрес регистрации";
                case "account_own_snils":
                    return "Снилс";
                case "account_operations":
                    return "Рассчетно касовое обслуживание";
                case "accownt_own_living":
                    return "Адрес проживания";
                case "assigned_publ_pers_registraion":
                    return "Адрес регистрации";
                case "assigned_publ_pers_relation":
                    return "Степень родства либо статус (супруг или супруга) по отношению кпубличному должностному лицу";
                case "beneficiaries":
                    return "Выгодоприобретатели";
                case "cash_source":
                    return "Источники происхождения денежных средств";
                case "collegiate_body":
                    return "Наименования наблюдательного совета";
                case "collegiate_person":
                    return "Наименование коллегиального исполнительног органа";
                case "company_group_name":
                    return "Наименование группы компаний";
                case "company_name":
                    return "Наименование группы компаний";
                case "salary_debt":
                    return "Задолжность по зп";
                case "state_employers":
                    return "Штатная численость сотрудников";
                case "sum_per_month":
                    return "Сумма по снятию за месяц";
                case "date_issue":
                    return "Дата выдачи";
                case "division_code":
                    return "Код подразделения";
                case "employers_volume":
                    return "Численность персонала";
                case "end_date":
                    return "Дата окончания действия";
                case "groupList":
                    return "Список групп";
                case "group_members":
                    return "Состав группы компаний";
                case "issued_by":
                    return "Кем выдан";
                case "legal_address":
                    return "Юридический адрес";
                case "mail_address":
                    return "Почтовый адрес";
                case "outside_contracts_volume":
                    return "Количество операций по безлимитным платежам в месяц";
                case "passport_serial":
                    return "Серия паспорта";
                case "physic_address":
                    return "Физический адрес";
                case "placeOfBirth":
                    return "Место рождения";
                case "licence_type":
                    return "Тип лицензии";
                case "licence_number":
                    return "Номер лицензии";
                case "licence_date_issue":
                    return "Дата выдачи лицензии";
                case "licenced_validity":
                    return "Срок действия";
                case "licence_issued_by":
                    return "Кем выдан";
                case "operation_volume":
                    return "Количество операций по безлимитным платежам в месяц";
                case "planned_operations":
                    return "Сведения о планируемых опреациях по счету";
                case "start_date":
                    return "Дата начала действия";
                case "supreme_management_body":
                    return "Тип";
                case "supervisotyBoardPersone_name":
                    return "Наименование коллегиального исполнительного органа";
                case "is_supervisoty":
                    return "Наличие коллегиального исполнительного органа";
                case "supreme_management_inn":
                    return "Инн";
                case "supreme_management_type":
                    return "Роль";
                case "validity":
                    return "Срок действия";
                case "contact_number":
                    return "Номер телефона";
                case "inn":
                    return "ИНН";
                case "addresses":
                    return "Адрес";
                case "supreme_management_person":
                    return "Тип Руководителя";
                case "collegiate_person_fio":
                    return "Члены коллегиального исполнительного органа";
                case "account_own_gender":
                    return "Пол";
                case "doc_number":
                    return "Номер документа удостоверяющего личность";
                case "doc_serial":
                    return "Серия документа удостоверяющего личность";
                case "doc_type":
                    return "Тип документа удостоверяющего личность";
                case "foreigner_doc_type":
                    return "Тип документа";
                case "foreigner_doc_serial":
                    return "Серия (если имеется)";
                case "foreigner_doc_issued":
                    return "Дата начала срока действия права пребывания(проживания)";
                case "foreigner_doc_validity":
                    return "Дата окончания срока действия права пребывания(проживания)";
                case "licenced_activity":
                    return "Перечень видов лицензируемой деятельности";
                // case 'licenced_validity': return 'Срок действия'
                // case 'licence_date_issue': return 'Дата выдачи лицензии'
                // case 'licence_issued_by': return 'Кем выдан'
                // case 'licence_number': return 'Номер лицензии'
                // case 'licence_type': return 'Сведения о лицензии'
                case "name":
                    return "Наименование";
                case "ogrn":
                    return "ОГРН";
                case "supervisory":
                    return "Наименования наблюдательного совета";
                case "is_collegiate_body":
                    return "Наименования наблюдательного совета";
                default:
                    return element;
                // case 'accownt_own_living': return 'Адрес проживания'
                // case 'tariff': return 'Тариф'
            }
        },
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
        this.$store.commit("IsFormData");
    },
    components: { LineStep }
};
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
  width: 100%;
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