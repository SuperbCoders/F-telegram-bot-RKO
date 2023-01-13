<template>
  <div>
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">
      Назад
    </v-btn>
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
    <v-dialog v-model="dialogAgreement" width="700">
      <v-card>
        <v-card-text class="pa-5">

          <h3>Согласие на обработку персональных данных</h3>
          <p>Настоящим Заявитель предоставляет КБ «Ренессанс Кредит» (ООО) (ОГРН 1027739586291, 115114, г. Москва,
            Кожевническая улица, д.14) (далее – Банк) согласие на обработку (совершение любых действий с использованием
            средств автоматизации или без, включая сбор, запись, систематизацию, накопление, хранение, уточнение,
            извлечение, использование, передачу, обезличивание, блокировку, удаление, уничтожение) Банком, Партнерами
            Банка и иными лицами, с которыми Банк заключит договоры на оказание услуг для исполнения обязательств Банка
            перед Клиентом в рамках Договоров на предоставление Услуги, путем осуществления контактов с помощью средств
            связи, всех своих персональных данных и/или своего фото- и/или видео изображения, и/или аудиозапись своего
            голоса в целях проверки достоверности
            предоставленных им сведений, комплексной оценки своего финансового состояния, а также в целях продвижения
            услуг Банка и Партнеров Банка на рынке. Согласие действует в течение сроков хранения документов и сведений,
            содержащих персональные данные, установленных законодательством Российской Федерации, и может быть отозвано
            путем предоставления письменного заявления в Банк.</p>


          <div v-if="is_OOO" class="mt-4">
            <h3>Согласие на использование ПЭП</h3>
            <p>Настоящим Заявитель в соответствии со ст. 428 Гражданского кодекса Российской Федерации присоединяется к
              Соглашению об использовании простой электронной подписи физического лица (далее – Соглашение ПЭП ФЛ),
              подтверждает, что ознакомлен с Соглашением ПЭП ФЛ, опубликованным на Сайте Банка, выражает свое согласие с
              ним и обязуется его выполнять.</p>
          </div>

          <div>
            <h3>Согласие для Бюро кредитных историй</h3>
            <p>Настоящим Клиент, а также Заявитель, выражают свое согласие на получение Банком в отношении Клиента и
              Заявителя кредитных отчетов из любых бюро кредитных историй с целью проверки сведений, предоставленных
              Клиентом при заключении и исполнении Договора кредитования счета и Заявителем при заключении и исполнении
              Договора поручительства, оценки финансового состояния Клиента и Заявителя, а также формирования Банком для
              Клиента и Заявителя предложений по кредитным продуктам.
              Заявитель, являющийся пользователем номера мобильного телефона, указанного в настоящем Комплексном
              заявлении, выражает согласие ПАО “Вымпел-Коммуникации» (ОГРН 1027700166636) (далее – Оператор) на
              обработку сведений о себе, как об абоненте, в том числе: о номере мобильного телефона, абонентском
              оборудовании (далее-Оборудование), о международном идентификаторе sim-карты, об изменениях номера
              мобильного телефона на sim-карте/номера Оборудования/номера абонентского договора, об оформлении номера
              мобильного телефона на иное лицо, о расторжении договора в отношении номера мобильного
              телефона/перенесения номера мобильного телефона в сеть другого Оператора, приостановки/возобновлении
              предоставления услуг на номере мобильного телефона, иные данные о номере мобильного телефона, об оказанных
              Оператором услугах связи (сведений об оплате услуг связи, идентификаторах, местонахождении Оборудования
              при оказании услуг связи) и передачу результата обработки Банку для проверки предоставленных Заявителем
              данных, а также для других законных целей. Согласие дано на срок до его отзыва.</p>
          </div>

          <div v-if="is_OOO" class="mt-4">
            <h3>Подтверждение присоединения к условиям поручительства</h3>
            <p>Настоящим Заявитель в обеспечение исполнения Клиентом всех обязательств по Договору кредитования счета в
              соответствии со ст. 428 Гражданского кодекса Российской Федерации присоединяется к Условиям
              поручительства,
              опубликованным на Сайте Банка, и подтверждает, что ознакомился с Договором кредитования счета и Договором
              поручительства в полном объеме, полностью и всецело понимает их содержание, принимает их условия и
              обязуется
              их выполнять.
              Заявитель соглашается на получение Банком кредитных отчетов о Заявителе из любых бюро кредитных историй с
              целью проверки сведений, предоставленных Заявителем при заключении и исполнении Договора поручительства,
              оценки финансового состояния Заявителя, а также формирования Банком для Заявителя предложений по кредитным
              продуктам.
              Заявитель, являющийся пользователем номера мобильного телефона, указанного в настоящем Комплексном
              заявлении, дает согласие ПАО «Вымпел-Коммуникации» (ОГРН 1027700166636) (далее – Оператор) на обработку
              сведений о себе, как об абоненте, в том числе: о номере мобильного телефона, абонентском оборудовании
              (далее-Оборудование), о международном идентификаторе sim-карты, об изменениях номера мобильного телефона
              на
              sim-карте/номера Оборудования/номера абонентского договора, об оформлении номера мобильного телефона на
              иное
              лицо, о расторжении договора в отношении номера мобильного телефона/перенесения номера мобильного телефона
              в
              сеть другого Оператора, приостановки/возобновлении
              предоставления услуг на номере мобильного телефона, иные данные о номере мобильного телефона, об оказанных
              Оператором услугах связи (сведений об оплате услуг связи, идентификаторах, местонахождении Оборудования
              при
              оказании услуг связи) и передачу результата обработки Банку для проверки предоставленных мной данных, а
              также для других законных целей. Согласие дано на срок до его отзыва.</p>
          </div>

          <h3 class="mt-4">Согласие на обработку сведений об абоненте</h3>
          <p>
            Заявитель, являющийся пользователем номера мобильного телефона, указанного в настоящей Анкете, выражает
            согласие ПАО «Вымпел-Коммуникации» (ОГРН 1027700166636) (далее – Оператор) на обработку сведений о себе, как
            об абоненте, в том числе: о номере мобильного телефона, абонентском оборудовании (далее-Оборудование), о
            международном идентификаторе sim- карты, об изменениях номера мобильного телефона на sim-карте/ номера
            Оборудования/ номера абонентского договора, об оформлении номера мобильного телефона на иное лицо, о
            расторжении договора в отношении номера мобильного телефона/ перенесения номера мобильного телефона в сеть
            другого Оператора, приостановки/ возобновлении предоставления услуг на номере мобильного телефона, иные
            данные о номере мобильного телефона, об оказанных Оператором услугах связи (сведений об оплате услуг связи,
            идентификаторах, местонахождении Оборудования при оказании услуг связи) и передачу результата обработки
            Банку для проверки предоставленных Заявителем данных, а также для других законных целей. Согласие дано на
            срок до его отзыва.
          </p>
          <v-btn block large class="mt-10 card_content_button" color="primary" @click="dialogAgreement = false">
            Закрыть
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>
    <div>
      <h4 class="mb-6 text-center" style="text-align: left">Подтвердите введенные данные</h4>
    </div>
    <div class="all_data_table">
      <div class="d-flex">
        <div class="data_table_block">
          <p class="form_block_title  w-50" style="text-align: left">Вопрос</p>
        </div>
        <div class="data_table_block">
          <p class="form_block_title  w-50" style="text-align: left">Ответ</p>
        </div>
      </div>
      <div v-for="(step, step_index) in getFormData" :key="step_index">

        <div v-for="(objectAnswer, question) in step" :key="question" class="mt-2">
          <div v-if="objectAnswer.type === 'Object'">
            <div v-if="objectAnswer.body">
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2">
                {{ translateValue(objectAnswer.body) }}
              </div>
            </div>
          </div>
          <div v-else-if="objectAnswer.type === 'Array'">
            <div class="d-flex" v-if="objectAnswer.typeArray === 'Variable'">
              <div class="form_block_title w-50 pb-2 pt-2" v-if="objectAnswer.body.length > 0">
                {{ isTitle(question) }}
              </div>
              <div class="form_block_title w-50 pb-2 pt-2" style="flex-direction: column; gap: 15px;" v-if="objectAnswer.body.length > 0">
                <div v-for="(subAnswer, subKey) in objectAnswer.body" :key="subKey">
                  - {{ translateValue(subAnswer.body) }}
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
                        {{ translateValue(subAnswer) }}
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
                {{ translateValue(objectAnswer.body) }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <line-step :step="number_step" class="mt-10" />
    <p @click="dialogAgreement = true" class="mt-8 text-center" style="cursor: pointer;">
      Нажимая на кнопку «Отправить», вы соглашаетесь с
      условиями подачи заявки и обработки персональных данных</p>
    <v-btn elevation="2" class="card_content_button mt-1" large @click="sendData()">Отправить</v-btn>
  </div>
</template>
<script>
import LineStep from "@/components/line_step/line_step.vue"
import { translateMixin } from '@/mixin/translate'
export default {
  mixins: [translateMixin],
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      dialog: false,
      dialogAgreement: false,
      formData: {},
    };
  },
  methods: {
    async sendData() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_11',
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

    isFormData(index) {
      return !!this.$store.state.formData['step_' + index]
    },
    getStepFromFormData(index) {
      return this.$store.state.formData?.['step_' + index]
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
    },
  },
  computed: {
    getFormData() {
      let formData = this.deepClone(this.$store.state.formData);
      for (const stepName in formData) {
        let step = formData[stepName]
        for (let keyStep in step) {
          // SKIP
          const list_skip = [
            'opf',
            'document_certifying_identity_executive_file',
            'document_certifying_identity_executive',

            'document_confirming_real_activity_file',
            'document_licenses_file',

            'document_confirming_real_activity',
            'document_licenses',

            'document_certifying_identity_ceo_file',
            'document_certifying_identity_ceo',
          ];
          if (list_skip.indexOf(keyStep) >= 0) {
            continue
          }

          let valueStep = step[keyStep]
          if (this.isArray(valueStep)) {
            let isTypeArray = null;

            if (keyStep === 'list_persone') {
              const arr_fio = valueStep.map((val) => {
                const account_own_lastname = val?.['substep_1']?.account_own_lastname;
                const account_own_name = val?.['substep_1']?.account_own_name;
                const account_own_surname = val?.['substep_1']?.account_own_surname;
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
    },
    is_OOO() {
      return this.$store.state.formData.step_1?.opf?.short === 'ООО';
    },

  },
  mounted() {

  },
  components: { LineStep },
};
</script>
<style scoped>

</style>