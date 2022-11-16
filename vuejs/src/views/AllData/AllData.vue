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
          <v-btn block large class="mt-10 card_content_button" color="primary" @click="closeAll()">
            Завершить
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>
    <div>
      <h4 class="mb-6 text-center">Подтвердите введенные данные</h4>
    </div>
    <div class="all_data_table">
      <div class="d-flex">
        <div class="data_table_block">
          <p class="form_block_title  w-50">Вопрос</p>
        </div>
        <div class="data_table_block">
          <p class="form_block_title  w-50">Ответ</p>
        </div>
      </div>
      <div v-for="(step, step_index) in getFormData" :key="step_index">
        <hr class="mt-2 mb-2">
        <div v-if="step_index === 'step_2'">
          Структура органов управления
        </div>
        <div v-if="step_index === 'step_3'">
          Группа взаимосвязанных компаний
        </div>

        <div v-if="step_index === 'step_5'">
          Сведения о лицензии
        </div>
        <div v-if="step_index === 'step_6'">
          Сведения о персонале
        </div>
        <div v-if="step_index === 'step_7'">
          Сведения о планируемых операциях по счету
        </div>
        <div v-if="step_index === 'step_8'">
          Выгодоприобретатели
        </div>
        <div v-if="step_index === 'step_9'">
          Сведения о целях установления деловых отношений с банком
        </div>
        <div v-if="step_index === 'step_11'">
          Тарифы на расчетно-кассовое обслуживание
        </div>
        <div v-for="(objectAnswer, question) in step" :key="question" class="mt-2">
          <div v-if="objectAnswer.type === 'Object'">
            <div v-if="objectAnswer.body">
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ objectAnswer.body }}
              </div>
            </div>

          </div>
          <div v-else-if="objectAnswer.type === 'Array'">
            <div class="d-flex" v-if="objectAnswer.typeArray === 'Variable'">
              <div class="form_block_title w-50 pb-2 pt-2" v-if="objectAnswer.body.length > 0">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2" v-if="objectAnswer.body.length > 0">
                <div v-for="(subAnswer, subKey) in objectAnswer.body" :key="subKey">
                  - {{ subAnswer.body }}
                </div>
              </div>
            </div>

            <div class="" v-if="objectAnswer.typeArray === 'Object'">
              <div class="form_block_title pb-2 pt-2" v-if="objectAnswer.body.length > 0">
                {{ isTitle(question) }}
              </div>

              <div v-for="(arrayAnswer, arrayKey) in objectAnswer.body" :key="arrayKey">
                <div v-for="(subAnswer, subKey) in arrayAnswer.body" :key="subKey">
                  <div v-if="subAnswer" class="d-flex">
                    <div class="form_block_title w-50 pb-2 pt-2">
                      {{ isTitle(subKey) }}
                    </div>
                    <div class="form_block_title w-50 pb-2 pt-2">
                      <div v-if="isArray(subAnswer)">
                        <div v-for="(arr, key) in subAnswer" :key="key">
                          - {{ arr }}
                        </div>
                      </div>
                      <div v-else>
                        {{ subAnswer }}
                      </div>
                    </div>
                  </div>

                </div>

              </div>

            </div>

          </div>
          <div v-else-if="objectAnswer.type === 'Boolean'">
            <div class="d-flex">
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2">
                <div>
                  <span v-if="objectAnswer.body">Да</span>
                  <span v-else>Нет</span>
                </div>

              </div>
            </div>
          </div>
          <div v-else-if="objectAnswer.type === 'Variable'">
            <div class="d-flex">
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ objectAnswer.body }}
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
      this.$store.dispatch('addObjectFormData', {
        object: 'step_final',
        value: {
          is_finished: true,
        }
      });


      this.dialog = true;
    },
    deepClone(obj) {
      if (obj === null) return null;
      let clone = Object.assign({}, obj);

      Object.keys(clone).forEach(
        key =>
        (clone[key] =
          typeof obj[key] === "object" ? this.deepClone(obj[key]) : obj[key])
      );

      return Array.isArray(obj) && obj.length
        ? (clone.length = obj.length) && Array.from(clone)
        : Array.isArray(obj)
          ? Array.from(obj)
          : clone;
    },
    isObject(element) {
      if (typeof element == "object") {
        return true;
      } else {
        return false;
      }
    },
    isBoolean(element) {
      if (typeof element == "boolean") {
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
    closeAll() {
      window.Telegram.WebApp.close();
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
          return "Расчетно-кассовое обслуживание";
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
          return "Высший орган управления";
        case "supervisoty_board_persone_name":
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
          return "Адреса:";
        case "supreme_management_person":
          return "Тип руководителя";
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
        case "list_collegial_executive_body":
          return "Члены коллегиального исполнительного органа";
        case "list_supervisoty_board_persone":
          return "Члены наблюдательного совета";
        case "informationGoals":
          return "Юридические лица компании";
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
      let formData = this.deepClone(this.$store.state.formData);
      for (const stepName in formData) {
        let step = formData[stepName]
        for (let keyStep in step) {
          let valueStep = step[keyStep]
          if (this.isArray(valueStep)) {
            let isTypeArray = null;

            if (keyStep === 'list_collegial_executive_body' || keyStep === 'list_supervisoty_board_persone') {
              const arr_fio = valueStep.map((val) => {
                const account_own_lastname = val?.['page-1']?.account_own_lastname;
                const account_own_name = val?.['page-1']?.account_own_name;
                const account_own_surname = val?.['page-1']?.account_own_surname;
                return {
                  type: 'Variable',
                  body: `${account_own_lastname} ${account_own_name} ${account_own_surname}`,
                }
              })
              console.log('arr_fio', arr_fio);
              step[keyStep] = {
                type: 'Array',
                typeArray: 'Variable',
                body: arr_fio,
              }

              continue
            }

            for (let keySubStep in valueStep) {
              let valueSubStep = valueStep[keySubStep];
              if (this.isArray(valueSubStep)) {
                valueStep[keySubStep] = {
                  type: 'Array',
                  body: valueSubStep,
                }
                isTypeArray = "Array";
              } else if (this.isObject(valueSubStep)) {
                valueStep[keySubStep] = {
                  type: 'Object',
                  body: valueSubStep,
                }

                isTypeArray = "Object";
              } else if (this.isBoolean(valueSubStep)) {
                valueStep[keyStep] = {
                  type: 'Boolean',
                  body: valueSubStep,
                }
                isTypeArray = "Boolean";
              } else {
                valueStep[keySubStep] = {
                  type: 'Variable',
                  body: valueSubStep,
                }
                isTypeArray = "Variable";
              }
            }
            step[keyStep] = {
              type: 'Array',
              typeArray: isTypeArray,
              body: valueStep,
            }
          } else if (this.isObject(valueStep)) {
            step[keyStep] = {
              type: 'Object',
              body: valueStep,
            }
          } else if (this.isBoolean(valueStep)) {
            step[keyStep] = {
              type: 'Boolean',
              body: valueStep,
            }
          } else if (valueStep || valueStep === 0) {
            step[keyStep] = {
              type: 'Variable',
              body: valueStep,
            }
          } else {
            step[keyStep] = {
              type: 'Unknow',
              body: valueStep,
            }
          }
        }
      }

      return formData;
    }

  },
  mounted() {
  },
  components: { LineStep },
};
</script>
<style scoped>
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
  display: block !important;
  align-items: flex-start;
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