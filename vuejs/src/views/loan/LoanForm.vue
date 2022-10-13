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
  <v-container v-else class="fill-height p-0 application-form" fluid>
    <attach-button class="d-none" text="Прикрепить файл" />
    <v-row align="center" justify="center">
      <v-col cols="12">
        <v-stepper v-model="currentFormStep" alt-labels class="elevation-0">
          <v-stepper-items align="center" justify="center">
            <v-stepper-content step="1">
              <v-row>
                <v-col cols="12">
                  <h1 class="display-1 text-left mb-10">Адрес</h1>
                  <div class="form_block mt-5">
                    <p class="text-left">ИНН</p>
                    <v-text-field
                      v-model="formData['inn']"
                      id="oldName"
                      placeholder="ООО Ромашка"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['inn']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Имя Компании</p>
                    <v-text-field
                      v-model="formData['company_name']"
                      id="oldName"
                      placeholder="ООО Ромашка"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['company_name']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Контактный телефон</p>
                    <v-text-field
                      v-model="formData['contact_number']"
                      id="oldName"
                      placeholder="ООО Ромашка"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['contact_number']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <default-input />
                  <div class="form_block mt-5">
                    <p class="text-left">Тип</p>
                    <v-combobox
                      filled
                      outlined
                      placeholder="Тип"
                      :items="availableCities"
                    ></v-combobox>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Основания</p>
                    <v-text-field
                      v-model="formData['basis']"
                      id="oldName"
                      placeholder="ООО Ромашка"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['basis']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_group">
                    <p class="text-left mb-5">Юридический адрес совпадает с физическим?</p>
                    <v-btn-toggle
                      active-class
                      color="pink darken-1"
                      class="d-flex align-start"
                      v-model="toggle_exclusive"
                    >
                      <v-btn class="d-flex align-center">
                        <p class="pl-5 pr-5 mb-0">Да</p>
                      </v-btn>

                      <v-btn>
                        <p class="pl-5 pr-5 mb-0">Нет</p>
                      </v-btn>
                    </v-btn-toggle>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">физический адрес</p>
                    <v-text-field
                      v-model="formData['physical_address']"
                      id="oldName"
                      placeholder="Физический адрес"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['physical_address']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_group">
                    <p class="text-left mb-5">почтовый адрес совпадает с юридическим?</p>
                    <v-btn-toggle
                      active-class
                      color="pink darken-1"
                      class="d-flex align-start"
                      v-model="toggle_exclusive"
                    >
                      <v-btn class="d-flex align-center">
                        <p class="pl-5 pr-5 mb-0">Да</p>
                      </v-btn>

                      <v-btn>
                        <p class="pl-5 pr-5 mb-0">Нет</p>
                      </v-btn>
                    </v-btn-toggle>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Почтовый адрес</p>
                    <v-text-field
                      v-model="formData['mail_address']"
                      id="oldName"
                      placeholder="Адрес"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['mail_address']"
                      :required="true"
                    ></v-text-field>
                  </div>
                </v-col>
              </v-row>
            </v-stepper-content>
            <v-stepper-content step="2">
              <v-row>
                <v-col cols="12">
                  <h2 class="text-left mb-10">Структура органов управления</h2>
                  <div class="form_block mt-5">
                    <p class="text-left">Высший орган управления</p>
                    <v-combobox
                      filled
                      outlined
                      placeholder="Выберите из списка"
                      :items="availableCities"
                      v-model="formData['supreme_management_body']"
                    ></v-combobox>
                  </div>
                  <default-input />
                  <div class="form_block mt-5">
                    <p class="text-left">Руководитель</p>
                    <v-text-field
                      v-model="formData['mail_address']"
                      id="oldName"
                      placeholder="ФИО Руководителя"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['supervisor']"
                      :required="true"
                      />
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">ИНН руководителя</p>
                    <v-text-field
                      v-model="formData['oldName']"
                      id="oldName"
                      placeholder="Введите ИНН "
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['supervisor_inn']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_group">
                    <p class="text-left mb-5">Наличие наблюдательного совета</p>
                    <v-btn-toggle
                      active-class
                      color="pink darken-1"
                      class="d-flex align-start"
                      v-model="toggle_exclusive"
                    >
                      <v-btn class="d-flex align-center">
                        <p class="pl-5 pr-5 mb-0">Да</p>
                      </v-btn>

                      <v-btn>
                        <p class="pl-5 pr-5 mb-0">Нет</p>
                      </v-btn>
                    </v-btn-toggle>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Наименования наблюдательного совета</p>
                    <v-text-field
                      v-model="formData['supervisory']"
                      id="oldName"
                      append-icon="mdi-map-marker"
                      placeholder="Адрес"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['supervisory']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_group">
                    <p class="text-left mb-5">
                      Наличие коллегиального исполнительног органа
                    </p>
                    <v-btn-toggle
                      active-class
                      color="pink darken-1"
                      class="d-flex align-start"
                      v-model="toggle_exclusive"
                    >
                      <v-btn class="d-flex align-center">
                        <p class="pl-5 pr-5 mb-0">Да</p>
                      </v-btn>

                      <v-btn>
                        <p class="pl-5 pr-5 mb-0">Нет</p>
                      </v-btn>
                    </v-btn-toggle>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">
                      Наименование коллегиального исполнительног органа
                    </p>
                    <v-text-field
                      v-model="formData['collegiate_body']"
                      id="oldName"
                      placeholder="Наименование"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['collegiate_body']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">
                      Члены коллегиального исполнительного органа
                    </p>
                    <v-text-field
                      v-model="formData['collegiate_person']"
                      id="oldName"
                      placeholder="Укажите ФИЗ"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['collegiate_person']"
                      :required="true"
                    ></v-text-field>
                  </div>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-row>
                <v-col cols="12">
                  <h2 class="text-left mb-10">Сведения о персонале</h2>
                  <div class="form_block mt-5">
                    <p class="text-left">Численность персонала</p>
                    <v-text-field
                      v-model="formData['employers_volume']"
                      id="oldName"
                      placeholder="Введите численность персонала"
                      class="align-center border-none"
                      name="oldName"
                      append-icon="mdi-currency-rub"
                      outlined
                      :error-messages="formErrors['employers_volume']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Задолженность по зарплате</p>
                    <v-text-field
                      v-model="formData['salary_debt']"
                      id="oldName"
                      placeholder="Введите задолженность по зарплате"
                      class="align-center border-none"
                      name="oldName"
                      append-icon="mdi-currency-rub"
                      outlined
                      :error-messages="formErrors['salary_debt']"
                      :required="true"
                    ></v-text-field>
                  </div>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="4">
              <v-row>
                <v-col cols="12">
                  <h2 class="text-left mb-10">
                    Группа взаимосвязанных компаний
                  </h2>
                  <div class="form_block mt-5">
                    <p class="text-left">Название группы компаний</p>
                    <v-text-field
                      v-model="formData['company_group_name']"
                      id="oldName"
                      placeholder="Наименование"
                      class="align-center border-none"
                      name="oldName"
                      outlined
                      :error-messages="formErrors['company_group_name']"
                      :required="true"
                    ></v-text-field>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Дата начала действия</p>
                    <v-menu
                      v-model="formData['stop_date']"
                      :close-on-content-click="false"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="formData['start_date']"
                          label="Дата выдачи"
                          id="passportIssueDate"
                          name="passportIssueDate"
                          append-icon="mdi-calendar-blank"
                          outlined
                          :error-messages="formErrors['passportIssueDate']"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="formData['start_date']"
                        @input="passportIssueDateMenu = false"
                      ></v-date-picker>
                    </v-menu>
                  </div>
                  <div class="form_block mt-5">
                    <p class="text-left">Дата окончания действия</p>
                    <v-menu
                      v-model="formData['stop_date']"
                      :close-on-content-click="false"
                      transition="scale-transition"
                      offset-y
                      min-width="auto"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          v-model="formData['stop_date']"
                          label="Дата выдачи"
                          id="passportIssueDate"
                          name="passportIssueDate"
                          append-icon="mdi-calendar-blank"
                          outlined
                          :error-messages="formErrors['stop_date']"
                          readonly
                          v-bind="attrs"
                          v-on="on"
                        ></v-text-field>
                      </template>
                      <v-date-picker
                        v-model="formData['stop_date']"
                        @input="passportIssueDateMenu = false"
                      ></v-date-picker>
                    </v-menu>
                  </div>
                </v-col>
              </v-row>
            </v-stepper-content>

            <v-stepper-content step="5">
              <v-row>
                <v-col cols="12">
                  <h2 class="text-left mb-10">Документы</h2>
                  <p class="subtitle text-left">
                    Сведения о лицензии на право осуществления деятельности
                  </p>
                  <v-file-input
                    v-model="document"
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
                  <h2 class="text-left mb-10">
                    Тарифы на расчетно-кассовое обслуживание
                  </h2>
                  <v-card elevation="2" class="mb-3">
                    <div class="card_content p-10 text-left m-11">
                      <h1 class="text-left mb-3">Простой</h1>
                      <p class="text-left mb-3">
                        Для начинающих предприниматель
                      </p>
                      <ul class="mb-3">
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                      </ul>
                      <h2 class="text-left mb-3">490 руб/мес</h2>
                      <v-btn elevation="2" large>Выбрать</v-btn>
                    </div>
                  </v-card>
                  <v-card elevation="2" class="mb-5">
                    <div class="card_content p-10 text-left m-11 ,b-">
                      <h1 class="text-left mb-3">Простой</h1>
                      <p class="text-left mb-3">
                        Для начинающих предприниматель
                      </p>
                      <ul class="mb-3">
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                      </ul>
                      <h2 class="text-left mb-3">490 руб/мес</h2>
                      <v-btn elevation="2" large>Выбрать</v-btn>
                    </div>
                  </v-card>
                  <v-card elevation="2" class="mb-3">
                    <div class="card_content p-10 text-left m-11 mb-5">
                      <h1 class="text-left mb-3">Простой</h1>
                      <p class="text-left mb-3">
                        Для начинающих предприниматель
                      </p>
                      <ul class="mb-3">
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                        <li class="text-left mb-3">
                          До 400 000 ₽ себе на счет для ИП бесплатно
                        </li>
                      </ul>
                      <h2 class="text-left mb-3">490 руб/мес</h2>
                      <v-btn elevation="2" large>Выбрать</v-btn>
                    </div>
                  </v-card>
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
import { DateTime } from "luxon";
import AttachButton from "../../components/button/attachButton.vue";
export default {
  name: "LoanForm",
  data: () => ({
    isApplicationSuccessfullySubmitted: false,
    isWaitingForResponse: false,
    currentFormStep: 1,
    formSteps: [
      {
        stepName: "1",
        stepNumber: 1,
        stepFields: ["loanAmount", "loanTerm"],
      },
      {
        stepName: "2",
        stepNumber: 2,
        stepFields: ["city"],
      },
      {
        stepName: "3",
        stepNumber: 3,
        stepFields: ["name", "phoneNumber", "email"],
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
        ],
      },
      {
        stepName: "5",
        stepNumber: 5,
        stepFields: ["passportPhotoOne", "passportPhotoTwo"],
      },
      {
        stepName: "6",
        stepNumber: 6,
        stepFields: [
          "registrationAddress",
          "currentAddress",
          "currentApartmentsNumber",
        ],
      },
      {
        stepName: "7",
        stepNumber: 7,
        stepFields: ["monthlyIncome"],
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
      "2 года",
      "3 года",
      "4 года",
      "5 лет",
      "6 лет",
      "7 лет",
    ],
    smallLoanTermTickLabels: ["2 года", "", "4 года", "", "6 лет", ""],
    passportIssueDateMenu: false,
    passportBirthDateMenu: false,
    shouldDisplaySuccessMessage: false,
  }),
  mounted: function () {
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
  },
  computed: {
    currentDate: function () {
      return DateTime.now().setZone("Europe/Moscow").toISODate();
    },
    formProgress: function () {
      return (this.currentFormStep / this.formSteps.length) * 100;
    },
    monthlyPayment: function () {
      let r = this.interestRate / 12;
      let n = this.formData["loanTerm"] * 12 || 24;
      let P = this.formData["loanAmount"] || 1000000;
      let result = (P * (r * (1 + r) ** n)) / ((1 + r) ** n - 1);
      return parseFloat(result).toFixed(2);
    },
    interestAmount: function () {
      let loanTerm = this.formData["loanTerm"] * 12 || 24;
      let loanAmount = this.formData["loanAmount"] || 1000000;
      let result = this.monthlyPayment * loanTerm - loanAmount;
      return parseFloat(result).toFixed(2);
    },
    totalLoanAmount: function () {
      let loanAmount = this.formData["loanAmount"] || 1000000;
      let result = parseFloat(loanAmount) + parseFloat(this.interestAmount);
      return result.toFixed(2);
    },
    allowedToContinueFromStepTwo: function () {
      let requiredFields = [
        this.formData["name"],
        this.formData["city"],
        this.formData["email"],
        this.formData["phoneNumber"],
      ];
      return requiredFields.every(Boolean);
    },
    allowedToSubmitApplication: function () {
      let requiredFields = [
        this.agreementCheckboxOne,
        this.agreementCheckboxTwo,
        this.agreementCheckboxThree,
        this.agreementCheckboxFour,
        this.agreementCheckboxFive,
      ];
      return requiredFields.every(Boolean);
    },
    shouldAddOldPassportData: function () {
      if (this.formData["passportIssueDate"]) {
        let passportIssueDate = DateTime.fromISO(
          this.formData["passportIssueDate"]
        );
        let currentDate = DateTime.now().setZone("Europe/Moscow");
        let timeSincePassportWasIssued = currentDate.diff(passportIssueDate, [
          "months",
        ]);
        if (timeSincePassportWasIssued.months < 24) {
          return true;
        }
      }
      return false;
    },
    isOnFirstFormStep: function () {
      return this.currentFormStep === 1;
    },
    isOnLastFormStep: function () {
      return this.currentFormStep === this.formSteps.length;
    },
  },
  methods: {
    nextStep(n) {
      if (n === this.steps) {
        this.e1 = 1;
      } else {
        this.e1 = n + 1;
      }
    },
    getFormattedCurrency: function (number) {
      if (number) {
        return parseFloat(number).toLocaleString("ru-RU");
      }
    },
    getFormattedYearNoun: function (number) {
      const ORDER = [2, 0, 1, 1, 1, 2];
      const DECLENSIONS = ["год", "года", "лет"];
      let declension =
        number % 100 > 4 && number % 100 < 20
          ? 2
          : ORDER[number % 10 < 5 ? number % 10 : 5];
      return DECLENSIONS[declension];
    },
    getFormData: function () {
      let formData = new FormData();
      Object.keys(this.formData).forEach((key) =>
        formData.append(key, this.formData[key])
      );
      if (this.passportPhotoOne) {
        formData.append("passportPhotoOne", this.passportPhotoOne);
      }
      if (this.passportPhotoTwo) {
        formData.append("passportPhotoTwo", this.passportPhotoTwo);
      }
      if (
        window.Telegram &&
        window.Telegram.WebApp &&
        window.Telegram.WebApp.initDataUnsafe &&
        window.Telegram.WebApp.initDataUnsafe.user &&
        window.Telegram.WebApp.initDataUnsafe.user.id
      ) {
        const userId = window.Telegram.WebApp.initDataUnsafe.user.id;
        formData.append("telegramChatId", userId);
      }
      return formData;
    },
    goToNextStep: function () {
      if (!this.isOnLastFormStep) {
        this.currentFormStep += 1;
        window.scrollTo(0, 0);
      }
    },
    goToPreviousStep: function () {
      if (!this.isOnFirstFormStep) {
        this.currentFormStep -= 1;
        window.scrollTo(0, 0);
      }
    },
    goToFirstFormError: function () {
      for (const fieldName of Object.keys(this.formErrors)) {
        for (let step of this.formSteps) {
          if (step.stepFields.includes(fieldName)) {
            this.currentFormStep = step.stepNumber;
            return;
          }
        }
      }
    },
    submitLoanApplication: function () {
      this.formErrors = {};
      this.hasErrors = false;
      this.isWaitingForResponse = true;
      const formData = this.getFormData();
      axios
        .post(
          `http://localhost:8000/loan-application/create/`,
          formData,
        )
        .then(() => {
          this.isWaitingForResponse = false;
          this.formData = {};
          this.isApplicationSuccessfullySubmitted = true;
          window.Telegram.WebApp.close();
        })
        .catch((error) => {
          this.formErrors = error.response.data;
          this.hasErrors = true;
          this.isWaitingForResponse = false;
          this.goToFirstFormError();
        });
    },
  },
  components: { AttachButton },
};
</script>

<style lang="scss" >
.autn_form {
  height: 50px !important;
}
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
.card_content {
  padding: 20px;
}
</style>
