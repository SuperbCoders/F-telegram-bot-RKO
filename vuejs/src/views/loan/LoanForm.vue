<template>
  <v-container
    v-if="isApplicationSuccessfullySubmitted"
    class="fill-height"
    fluid
  >
    <v-row align="center" justify="center">
      <v-col cols="12" md="8" lg="6" align="center" justify="center">
        <v-alert color="overline primary  " dark>
          Ваша заявка отправлена в банк на рассмотрение. Информация с
          результатами рассмотрения будет отправлена вам по телефону и
          электронной почте.
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
  <v-container v-else class="fill-height application-form" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12">
        <v-stepper v-model="currentFormStep" alt-labels class="elevation-0">
          <v-stepper-items align="center" justify="center">
            <v-stepper-content step="1">
              <v-row>
                <v-col cols="12">
                  <p class="title blue-grey--text">
                    Сумма кредита:
                    <span class="primary--text"
                      >{{
                        getFormattedCurrency(formData["loanAmount"])
                      }}
                      &#8381;</span
                    >
                  </p>
                  <v-slider
                    v-model="formData['loanAmount']"
                    :max="5000000"
                    :min="1000000"
                    step="500000"
                    track-color="light-grey"
                    tick-size="5"
                    ticks="always"
                    track-fill-color="primary"
                  ></v-slider>
                  <p class="title blue-grey--text">
                    Срок:
                    <span class="primary--text">
                      {{ formData["loanTerm"] }}
                      {{ getFormattedYearNoun(formData["loanTerm"]) }}
                    </span>
                  </p>
                  <v-slider
                    class="d-none d-sm-block"
                    v-model="formData['loanTerm']"
                    :tick-labels="loanTermTickLabels"
                    :max="7"
                    :min="2"
                    step="1"
                    ticks
                    track-color="light-grey"
                    tick-size="5"
                    track-fill-color="primary"
                  ></v-slider>
                  <v-slider
                    class="d-sm-none"
                    v-model="formData['loanTerm']"
                    :tick-labels="smallLoanTermTickLabels"
                    :max="7"
                    :min="2"
                    step="1"
                    ticks
                    track-color="light-grey"
                    tick-size="5"
                    track-fill-color="primary"
                  ></v-slider>
                  <p class="mt-5 title grey--text">Ежемесячный платеж</p>
                  <v-scroll-y-transition hide-on-leave>
                    <p :key="monthlyPayment" class="display-1 primary--text">
                      {{ getFormattedCurrency(monthlyPayment) }} &#8381;
                    </p>
                  </v-scroll-y-transition>
                  <p class="grey--text">
                    Сумма переплаты:
                    <span class="black--text"
                      >{{ getFormattedCurrency(interestAmount) }} &#8381;</span
                    >
                  </p>
                  <p class="grey--text">
                    Сумма кредита:
                    <span class="black--text"
                      >{{ getFormattedCurrency(totalLoanAmount) }} &#8381;</span
                    >
                  </p>
                  <p class="grey--text">
                    Процентная ставка:
                    <span class="black--text">{{ interestRate * 100 }}%</span>
                  </p>
                </v-col>
              </v-row>
            </v-stepper-content>
            <v-stepper-content step="2">
              <v-row>
                <v-col cols="12">
                  <v-select
                    v-model="formData['city']"
                    :items="availableCities"
                    outlined
                    label="Город"
                  ></v-select>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="formData['name']"
                    label="ФИО"
                    id="name"
                    name="name"
                    outlined
                    :error-messages="formErrors['name']"
                    :required="true"
                  ></v-text-field>
                  <v-checkbox
                    class="mt-n5"
                    :ripple="false"
                    v-model="hasOldName"
                    label="Меняли ли вы ФИО?"
                  ></v-checkbox>
                  <v-scroll-y-transition hide-on-leave>
                    <v-text-field
                      v-if="hasOldName"
                      v-model="formData['oldName']"
                      label="Данные о предыдущих ФИО"
                      id="oldName"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['oldName']"
                      :required="true"
                    ></v-text-field>
                  </v-scroll-y-transition>
                  <v-text-field
                    v-model="formData['phoneNumber']"
                    label="Мобильный телефон"
                    id="phoneNumber"
                    name="phoneNumber"
                    outlined
                    type="tel"
                    :error-messages="formErrors['phoneNumber']"
                    :required="true"
                  ></v-text-field>
                  <v-text-field
                    v-model="formData['email']"
                    label="Электронная почта"
                    id="email"
                    name="email"
                    type="email"
                    outlined
                    :error-messages="formErrors['email']"
                    :required="true"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-row>
                <v-col cols="12">
                  <p class="subtitle grey--text">Текущие данные паспорта</p>
                  <v-text-field
                    v-model="formData['passportSeries']"
                    label="Серия"
                    id="passportSeries"
                    name="passportSeries"
                    outlined
                    :error-messages="formErrors['passportSeries']"
                    :required="true"
                  ></v-text-field>
                  <v-text-field
                    v-model="formData['passportNumber']"
                    label="Номер"
                    id="passportNumber"
                    name="passportNumber"
                    outlined
                    :error-messages="formErrors['passportNumber']"
                    :required="true"
                  ></v-text-field>
                  <v-text-field
                    v-model="formData['passportCode']"
                    label="Код подразделения"
                    id="passportCode"
                    name="passportCode"
                    outlined
                    :error-messages="formErrors['passportCode']"
                    :required="true"
                  ></v-text-field>
                  <v-menu
                    v-model="passportIssueDateMenu"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="formData['passportIssueDate']"
                        label="Дата выдачи"
                        id="passportIssueDate"
                        name="passportIssueDate"
                        outlined
                        :error-messages="formErrors['passportIssueDate']"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="formData['passportIssueDate']"
                      @input="passportIssueDateMenu = false"
                    ></v-date-picker>
                  </v-menu>
                  <v-scroll-y-transition hide-on-leave>
                    <v-card
                      v-if="shouldAddOldPassportData"
                      class="mt-0 mb-5"
                      color="grey lighten-4"
                    >
                      <v-card-text align="left" justify="center">
                        <h4>Предыдущие данные паспорта</h4>
                        <p class="caption">
                          Обязательно к заполнению, если текущему паспорту менее
                          2-х лет
                        </p>
                        <v-text-field
                          v-model="formData['oldPassportSeries']"
                          label="Серия"
                          id="oldPassportSeries"
                          name="oldPassportSeries"
                          outlined
                          :error-messages="formErrors['oldPassportSeries']"
                          :required="true"
                        ></v-text-field>
                        <v-text-field
                          v-model="formData['oldPassportNumber']"
                          label="Номер"
                          id="oldPassportNumber"
                          name="oldPassportNumber"
                          outlined
                          :error-messages="formErrors['oldPassportNumber']"
                          :required="true"
                        ></v-text-field>
                        <v-text-field
                          v-model="formData['oldPassportCode']"
                          label="Код подразделения"
                          id="oldPassportCode"
                          name="oldPassportCode"
                          outlined
                          :error-messages="formErrors['oldPassportCode']"
                          :required="true"
                        ></v-text-field>
                      </v-card-text>
                    </v-card>
                  </v-scroll-y-transition>
                  <v-text-field
                    v-model="formData['passportIssuedBy']"
                    label="Кем выдан"
                    id="passportIssuedBy"
                    name="passportIssuedBy"
                    outlined
                    :error-messages="formErrors['passportIssuedBy']"
                    :required="true"
                  ></v-text-field>
                  <v-text-field
                    v-model="formData['passportPlaceOfBirth']"
                    label="Место рождения"
                    id="passportPlaceOfBirth"
                    name="passportPlaceOfBirth"
                    outlined
                    :error-messages="formErrors['passportPlaceOfBirth']"
                    :required="true"
                  ></v-text-field>
                  <v-menu
                    v-model="passportBirthDateMenu"
                    :close-on-content-click="false"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-text-field
                        v-model="formData['passportDateOfBirth']"
                        label="Дата рождения"
                        id="passportDateOfBirth"
                        name="passportDateOfBirth"
                        outlined
                        :error-messages="formErrors['passportDateOfBirth']"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker
                      v-model="formData['passportDateOfBirth']"
                      @input="passportBirthDateMenu = false"
                    ></v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="5">
              <v-row>
                <v-col cols="12">
                  <p class="subtitle grey--text">Фото страниц паспорта</p>
                  <v-file-input
                    v-model="passportPhotoOne"
                    :error-messages="formErrors['passportPhotoOne']"
                    label="Главная страница"
                    outlined
                    accept="image/*"
                  ></v-file-input>
                  <v-file-input
                    v-model="passportPhotoTwo"
                    :error-messages="formErrors['passportPhotoTwo']"
                    label="Страница с регистрацией"
                    outlined
                    accept="image/*"
                  ></v-file-input>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="6">
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="formData['registrationAddress']"
                    label="Адрес регистрации"
                    id="registrationAddress"
                    name="registrationAddress"
                    outlined
                    :error-messages="formErrors['registrationAddress']"
                    :required="true"
                  ></v-text-field>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="isRegistrationAddressSameAsCurrent"
                    label="Адрес регистрации совпадает с адресом проживания"
                  ></v-checkbox>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="formData['hasNoCurrentAddress']"
                    label="Адрес регистрации отсутствует"
                  ></v-checkbox>
                  <v-scroll-y-transition hide-on-leave>
                    <v-text-field
                      v-if="!isRegistrationAddressSameAsCurrent"
                      v-model="formData['currentAddress']"
                      label="Адрес проживания"
                      id="currentAddress"
                      name="currentAddress"
                      outlined
                      :error-messages="formErrors['currentAddress']"
                      :required="true"
                    ></v-text-field>
                  </v-scroll-y-transition>
                  <v-text-field
                    v-model="formData['currentApartmentsNumber']"
                    label="Номер квартиры"
                    id="currentApartmentsNumber"
                    name="currentApartmentsNumber"
                    outlined
                    :error-messages="formErrors['currentApartmentsNumber']"
                    :required="true"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="7">
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    v-model="formData['monthlyIncome']"
                    label="Размер ежемесячного совокупного дохода (руб.)"
                    id="monthlyIncome"
                    name="monthlyIncome"
                    outlined
                    :error-messages="formErrors['monthlyIncome']"
                    :required="true"
                  ></v-text-field>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="agreementCheckboxOne"
                    label="Я даю согласие на обработку персональных данных"
                  ></v-checkbox>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="agreementCheckboxTwo"
                    label="Я подтверждаю своё согласие на получение Банком информации о моей кредитной истории в бюро кредитных историй"
                  ></v-checkbox>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="agreementCheckboxThree"
                    label="Я уведомлен(а) об условиях предоставления и погашения кредита, а также подтверждаю присоединение к Правилам комплексного банковского обслуживания физических лиц в ПАО Банк ЗЕНИТ"
                  ></v-checkbox>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="agreementCheckboxFour"
                    label="Подтверждаю свое согласие на уступке прав (требований)"
                  ></v-checkbox>
                  <v-checkbox
                    class="mt-n2"
                    :ripple="false"
                    v-model="agreementCheckboxFive"
                    label="Подтверждаю свое согласие на взыскание задолженности по кредиту по исполнительной подписи нотариуса"
                  ></v-checkbox>
                </v-col>
              </v-row>
            </v-stepper-content>
          </v-stepper-items>
          <v-row>
            <v-col cols="12">
              <v-progress-linear
                :value="formProgress"
                color="primary"
                height="5"
              ></v-progress-linear>
            </v-col>
          </v-row>
          <v-row v-if="isOnFirstFormStep">
            <v-col cols="12">
              <v-btn block large color="primary" @click="goToNextStep"
                >Продолжить</v-btn
              >
            </v-col>
          </v-row>
          <v-row v-else-if="isOnLastFormStep">
            <v-col cols="6">
              <v-btn block large @click="goToPreviousStep">Назад</v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn
                color="primary"
                block
                large
                :disabled="!allowedToSubmitApplication"
                :loading="isWaitingForResponse"
                @click="submitLoanApplication"
              >
                Отправить
              </v-btn>
            </v-col>
          </v-row>
          <v-row v-else>
            <v-col cols="6">
              <v-btn block large @click="goToPreviousStep">Назад</v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn block large color="primary" @click="goToNextStep"
                >Продолжить</v-btn
              >
            </v-col>
          </v-row>
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import { DateTime } from 'luxon';

export default {
  name: 'LoanForm',

  data: () => ({
    isApplicationSuccessfullySubmitted: false,
    isWaitingForResponse: false,
    currentFormStep: 1,
    formSteps: [
      {
        stepName: "1",
        stepNumber: 1,
        stepFields: [
          "loanAmount",
          "loanTerm",
        ]
      },
      {
        stepName: "2",
        stepNumber: 2,
        stepFields: [
          "city",
        ]
      },
      {
        stepName: "3",
        stepNumber: 3,
        stepFields: [
          "name",
          "phoneNumber",
          "email",
        ]
      },
      {
        stepName: "4",
        stepNumber: 4,
        stepFields: [
          "passportSeries",
          "passportNumber",
          "passportCode",
          "passportIssueDate",
          "passportIssuedBy",
          "passportPlaceOfBirth",
          "passportDateOfBirth",
        ]
      },
      {
        stepName: "5",
        stepNumber: 5,
        stepFields: [
          "passportPhotoOne",
          "passportPhotoTwo",
        ]
      },
      {
        stepName: "6",
        stepNumber: 6,
        stepFields: [
          "registrationAddress",
          "currentAddress",
          "currentApartmentsNumber",
        ]
      },
      {
        stepName: "7",
        stepNumber: 7,
        stepFields: [
          "monthlyIncome",
        ]
      },
    ],
    hasOldName: false,
    agreementCheckboxOne: false,
    agreementCheckboxTwo: false,
    agreementCheckboxThree: false,
    agreementCheckboxFour: false,
    agreementCheckboxFive: false,
    availableCities: [
      "Москва",
      "Санкт-Петербург",
      "Альметьевск",
      "Азнакаево",
      "Анапа",
      "Арзамас",
      "Бавлы",
      "Балашиха",
      "Бугры",
      "Бугульма",
      "Горно-Алтайск",
      "Данков",
      "Джалиль",
      "Екатеринбург",
      "Елабуга",
      "Елец",
      "Заинск",
      "Ижевск",
      "Йошкар-Ола",
      "Казань",
      "Калининград",
      "Карабаш",
      "Кемерово",
      "Краснодар",
      "Лениногорск",
      "Липецк",
      "Мытищи",
      "Набережные Челны",
      "Нижнекамск",
      "Нижний Новгород",
      "Новосибирск",
      "Нурлат",
      "Одинцово",
      "Пермь",
      "Ростов-на-Дону",
      "Самара",
      "Саратов",
      "Саров",
      "Сочи",
      "Тольятти",
      "Тула",
      "Химки",
      "Чебоксары",
      "Челябинск",
      "Чистополь",
    ],
    passportPhotoOne: null,
    passportPhotoTwo: null,
    interestRate: 0.05,
    formErrors: {},
    hasErrors: false,
    formData: {},
    isRegistrationAddressSameAsCurrent: false,
    loanTermTickLabels: [
      '2 года',
      '3 года',
      '4 года',
      '5 лет',
      '6 лет',
      '7 лет',
    ],
    smallLoanTermTickLabels: [
      '2 года',
      '',
      '4 года',
      '',
      '6 лет',
      '',
    ],
    passportIssueDateMenu: false,
    passportBirthDateMenu: false,
    shouldDisplaySuccessMessage: false,
  }),

  mounted: function () {
    window.Telegram.WebApp.ready()
    window.Telegram.WebApp.expand()
  },

  computed: {
    currentDate: function () {
      return DateTime.now().setZone("Europe/Moscow").toISODate()
    },
    formProgress: function () {
      return (this.currentFormStep / this.formSteps.length) * 100
    },
    monthlyPayment: function () {
      let r = this.interestRate / 12
      let n = this.formData["loanTerm"] * 12 || 24
      let P = this.formData["loanAmount"] || 1000000
      let result = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
      return parseFloat(result).toFixed(2)
    },
    interestAmount: function () {
      let loanTerm = this.formData["loanTerm"] * 12 || 24
      let loanAmount = this.formData["loanAmount"] || 1000000
      let result = (this.monthlyPayment * loanTerm) - loanAmount
      return parseFloat(result).toFixed(2)
    },
    totalLoanAmount: function () {
      let loanAmount = this.formData["loanAmount"] || 1000000
      let result = parseFloat(loanAmount) + parseFloat(this.interestAmount)
      return result.toFixed(2)
    },
    allowedToContinueFromStepTwo: function () {
      let requiredFields = [
        this.formData["name"],
        this.formData["city"],
        this.formData["email"],
        this.formData["phoneNumber"],
      ]
      return requiredFields.every(Boolean)
    },
    allowedToSubmitApplication: function () {
      let requiredFields = [
        this.agreementCheckboxOne,
        this.agreementCheckboxTwo,
        this.agreementCheckboxThree,
        this.agreementCheckboxFour,
        this.agreementCheckboxFive,
      ]
      return requiredFields.every(Boolean)
    },
    shouldAddOldPassportData: function () {
      if (this.formData["passportIssueDate"]) {
        let passportIssueDate = DateTime.fromISO(this.formData["passportIssueDate"])
        let currentDate = DateTime.now().setZone("Europe/Moscow")
        let timeSincePassportWasIssued = currentDate.diff(passportIssueDate, ["months"])
        if (timeSincePassportWasIssued.months < 24) {
          return true
        }
      }
      return false
    },
    isOnFirstFormStep: function () {
      return this.currentFormStep === 1
    },
    isOnLastFormStep: function () {
      return this.currentFormStep === this.formSteps.length
    }
  },

  methods: {
    nextStep(n) {
      if (n === this.steps) {
        this.e1 = 1
      } else {
        this.e1 = n + 1
      }
    },
    getFormattedCurrency: function (number) {
      if (number) {
        return parseFloat(number).toLocaleString("ru-RU")
      }
    },
    getFormattedYearNoun: function (number) {
      const ORDER = [2, 0, 1, 1, 1, 2]
      const DECLENSIONS = ['год', 'года', 'лет']
      let declension = (
        (number % 100 > 4 && number % 100 < 20) ?
          2 :
          ORDER[(number % 10 < 5) ? number % 10 : 5]
      )
      return DECLENSIONS[declension]
    },
    getFormData: function () {
      let formData = new FormData()
      Object.keys(this.formData).forEach(key => formData.append(key, this.formData[key]))
      if (this.passportPhotoOne) {
        formData.append("passportPhotoOne", this.passportPhotoOne)
      }
      if (this.passportPhotoTwo) {
        formData.append("passportPhotoTwo", this.passportPhotoTwo)
      }
      if (window.Telegram &&
        window.Telegram.WebApp &&
        window.Telegram.WebApp.initDataUnsafe &&
        window.Telegram.WebApp.initDataUnsafe.user &&
        window.Telegram.WebApp.initDataUnsafe.user.id) {
        const userId = window.Telegram.WebApp.initDataUnsafe.user.id
        formData.append("telegramChatId", userId)
      }
      return formData
    },
    goToNextStep: function () {
      if (!this.isOnLastFormStep) {
        this.currentFormStep += 1
        window.scrollTo(0, 0)
      }
    },
    goToPreviousStep: function () {
      if (!this.isOnFirstFormStep) {
        this.currentFormStep -= 1
        window.scrollTo(0, 0)
      }
    },
    goToFirstFormError: function () {
      for (const fieldName of Object.keys(this.formErrors)) {
        for (let step of this.formSteps) {
          if (step.stepFields.includes(fieldName)) {
            this.currentFormStep = step.stepNumber
            return
          }
        }
      }
    },
    submitLoanApplication: function () {
      this.formErrors = {}
      this.hasErrors = false
      this.isWaitingForResponse = true
      const formData = this.getFormData()
      axios
        .post(
          `${process.env.VUE_APP_API_ROOT_URL}loan-application/create/`,
          formData,
        )
        .then(() => {
          this.isWaitingForResponse = false
          this.formData = {}
          this.isApplicationSuccessfullySubmitted = true
          window.Telegram.WebApp.close()
        })
        .catch(error => {
          this.formErrors = error.response.data
          this.hasErrors = true
          this.isWaitingForResponse = false
          this.goToFirstFormError()
        });
    },
  },
};
</script>

<style lang="scss" >
.application-form {
  .v-slider__track-container {
    height: 5px !important;
  }
  .v-slider__track {
    height: 5px !important;
  }
  .v-slider__tick {
    background-color: #10c8d2;
  }
}
</style>
