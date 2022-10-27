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
    <div>
      <h4 class="mb-6 text-center">Подтвердите введенные данные</h4>
    </div>
    <div class="all_data_table">
      <div class="data_table-row-title d-flex">
        <div class="data_table_block">
          <p class="form_block_title">Вопрос</p>
        </div>
        <div class="data_table_block">
          <p class="form_block_title">Ответ</p>
        </div>
      </div>
      <div v-for="(step, step_index) in getFormData" :key="step_index">
        <hr class="mt-2 mb-2">
        <div v-for="(item, index) in step" :key="index" class="mt-1">
          <div v-if="item || item === 0">
            <div v-if="isArray(item)">
              <p class="d-flex title-table form_block_title" v-if="item.length > 0">
                {{ isTitle(index) }}
              </p>
              <div v-for="(sub_item, sub_index) in item" :key="sub_index">
                <div v-if="isObject(sub_item)">
                  <div v-for="(val, key) in sub_item" :key="key">
                    <div class="d-flex" v-if="val">
                      <div class="form_block_title w-50 pt-2 pb-2">
                        {{ isTitle(key) }}
                      </div>
                      <div class="w-50 pt-2 pb-2">
                        <div v-if="!isObject(val)" class="form_block_title">{{ val }}</div>
                      </div>
                      
                    </div>
                    <div class="block_right">
                      <div v-if="isObject(val)">
                        <div v-for="(elementObject, indexObject) in val" :key="indexObject" class="form_block_title">
                          - {{ elementObject }}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div v-else class="block_right">
                  <div class="form_block_title">- {{ sub_item }}</div>
                </div>
              </div>
            </div>
            <div class="d-flex" v-else-if="typeof item == 'boolean'">
              <p class="form_block_title w-50">
                {{ isTitle(index) }}
              </p>
              <div class="form_block_title w-50">
                <div>
                  <span v-if="item">Да</span>
                  <span v-else>Нет</span>
                </div>
                
              </div>
              
            </div>
            <div class="d-flex" v-else>
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ isTitle(index) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ item }}
              </div>

            </div>
          </div>

        </div>


      </div>
    </div>
    <line-step :step="10" class="mt-10" />
    <v-btn elevation="2" class="card_content_button mt-10" large @click="sendData()">Отправить</v-btn>
  </div>
</template>
<script>
import LineStep from "../../components/line_step/line_step.vue";

export default {
  data() {
    return {
      dialog: false,
      formData: {},
    };
  },
  methods: {
    async sendData() {
      // this.$store.commit("IsFormData");
      this.FormData = new FormData();
      const formData = this.getFormData
      let fullData = {};
      for(const step in formData) {
        const obj = formData[step];
        fullData = Object.assign(fullData, obj);
      }
      await fetch("https://rko-bot.spaaace.io/api/loan-application/create/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify(fullData),
      });
      this.dialog = true;
    },
    isObject(element) {
      if (typeof element == "object") {
        return true;
      } else {
        return false;
      }
    },
    isArray(element) {
      if (Array.isArray(element)) {
        return true;
      } else {
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
          return "ИНН";
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
          return "СНИЛС";
        case "account_operations":
          return "Рассчетно касовое обслуживание";
        case "accownt_own_living":
          return "Адрес проживания";
        case "assigned_publ_pers_registraion":
          return "Адрес регистрации";
        case "assigned_publ_pers_relation":
          return "Степень родства либо статус (супруг или супруга) по отношению к публичному должностному лицу";
        case "beneficiaries":
          return "Выгодоприобретатели";
        case "cash_source":
          return "Источники происхождения денежных средств";
        case "collegiate_body":
          return "Наименование наблюдательного совета";
        case "collegiate_person":
          return "Наименование коллегиального исполнительног органа";
        case "company_group_name":
          return "Наименование группы компаний";
        case "company_name":
          return "Наименование группы компаний";
        case "salary_debt":
          return "Задолженность по зп";
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
          return "ИНН";
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
        case "typeAdress":
          return "Тип Адреса";
        case "basis":
          return "Основание";
        case "address":
          return "Адрес";
        case "name":
          return "Наименование";
        case "ogrn":
          return "ОГРН";
        case "supervisory":
          return "Наименование наблюдательного совета";
        case "is_collegiate_body":
          return "Наличие наблюдательного совета";
        case "operation_sum":
          return "Сумма операций по безналичным платежам в месяц";
        case "listCollegialExecutiveBody":
          return "Члены коллегиального исполнительного органа";
        case "listSupervisotyBoardPersone":
          return "Члены наблюдательного совета";
        default:
          return element;
      }
    },
    isFormData(index) {
      return !!this.$store.state.formData['step_' + index]
    },
    getStepFromFormData(index) {
      return this.$store.state.formData?.['step_' + index]
    },
  },
  computed: {
    getFormData() {
      let formData = Object.assign({}, this.$store.state.formData)


      return formData;
    }

    // isValueString (value) {
    //   if (value[1] !== '' && null) {
    //     return true
    //   }
    // }
  },
  mounted() {
  },
  components: { LineStep },
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
  padding-right: 15px;
  box-sizing: border-box;
}

.w-50 {
  width: 50%;
}
.title-table {
  font-size: 14px !important;
  padding-top: 4px;
}
.block_right {
  display: flex;
  justify-content: flex-end;
}

.block_right>* {
  width: 50%;
}

.all_data_table-row {}
</style>