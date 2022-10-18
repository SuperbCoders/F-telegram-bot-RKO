<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold form_block_label">
      Структура органов управления
    </h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Выберите из списка</p>
        <v-combobox
          v-model="currentData.supreme_management_body"
          filled
          :rules="requiredRules"
          required
          :items="isLeaderList"
          outlined
          placeholder="Выберите из списка"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Руководитель</p>
        <v-combobox
          filled
          v-model="currentData.supreme_management_person"
          :items="isLeaderType"
          outlined
          :rules="requiredRules"
          placeholder="Тип"
        ></v-combobox>
      </div>
      <div v-if="isManagementCompany" class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <v-text-field
          id="oldName"
          v-model="currentData.supreme_management_inn"
          placeholder="Введите ИНН или название компании"
          class="align-center border-none"
          name="oldName"
          outlined
          type="number"
          :rules="innRules"
        ></v-text-field>
      </div>
      <div class="form_group mb-10">
        <p class="text-left form_block_label mt-5">
          Наличие наблюдательного совета
        </p>
        <RadioGroup
          @isStatus="(status) => (isTest1 = status)"
          name="Existence of a supervisory board"
        />
      </div>
      <div v-if="isTest1" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименования наблюдательного совета
        </p>
        <v-text-field
            id="oldName"
            placeholder="Наименования"
            class="align-center border-none"
            name="oldName"
            v-model="currentData.supervisory.account_company_name"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        <div
          v-for="(item, index) in currentData.supervisory"
          :key="index"
          class="form_block"
        >
          <p class="text-left form_block_title">Роль лица</p>
          <v-checkbox
            label="Руководитель"
            v-model="item.account_onw_role"
            value="Руководитель"
            hide-details
          >
          </v-checkbox>
          <v-checkbox
            label="Учредитель"
            value="Учредитель"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="item.account_onw_role"
            label="Бенефированый владелец"
            value="Бенефированый владелец"
            hide-details
          >
          </v-checkbox>
          <v-checkbox
            v-model="item.account_onw_role"
            label="Подписант"
            value="Подписант"
            hide-details
          ></v-checkbox>
          <!-- <p
            v-if="!valid && item.supervisory.account_onw_role.length < 1"
            class="error_message"
          >
            Выберите пункт
          </p> -->
          <div class="form_block mt-5">
            <p class="text-left form_block_title">Фамилия</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_lastname"
              placeholder="Введите фамилию"
              class="align-center border-none"
              outlined
              :rules="requiredRules"
              :required="true"
            >
            </v-text-field>
          </div>
          <div class="form_block">
            <p class="text-left form_block_title">Имя</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_name"
              placeholder="Введите имя"
              class="align-center border-none"
              outlined
              :rules="requiredRules"
              :required="true"
            ></v-text-field>
          </div>
          <div class="form_block">
            <p class="text-left form_block_title">Отчество (при наличии)</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_surname"
              placeholder="Введите отчество"
              class="align-center border-none"
              outlined
              :required="true"
            ></v-text-field>
          </div>
          <v-radio-group v-model="currentData.account_own_gender" mandatory>
            <v-radio label="Мужской" value="Мужской"></v-radio>
            <v-radio label="Женский" value="Женский"> </v-radio>
          </v-radio-group>
        </div>
        <div class="form_block d-flex align-center justify-center">
          <a
            @click="deleteObjectList(currentData.supervisory)"
            class="form_block_delete_link text-decoration-none"
            href="#form_block"
          >
            Отменить
          </a>
          <v-btn
            @click="addObjectList(currentData.supervisory)"
            class="
              text-center
              d-flex
              align-center
              justify-center
              ml-10
              add_form
            "
          >
            <span class="pr-3">Добавить</span>
            <v-icon>mdi-plus-circle-outline</v-icon>
          </v-btn>
        </div>
      </div>
      <div class="form_group mt-5">
        <p class="text-left form_block_label mb-2">
          Наличие коллегиального исполнительного органа
        </p>
        <RadioGroup
          @isStatus="(status) => (isTest2 = status)"
          name="The presence of a collegial executive body"
        />
      </div>
      <div v-if="isTest2" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименование коллегиального исполнительного органа
        </p>
        <v-text-field
          id="oldName"
          placeholder="Наименование"
          class="align-center border-none"
          name="oldName"
          outlined
          v-model="currentData.collegiate_body.company_name"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
        <div
          v-for="(item, index) in currentData.collegiate_body"
          :key="index"
          class="form_block"
        >
          <p class="text-left form_block_title">Роль лица</p>
          <v-checkbox
            label="Руководитель"
            v-model="item.account_onw_role"
            value="Руководитель"
            hide-details
          >
          </v-checkbox>
          <v-checkbox
            label="Учредитель"
            value="Учредитель"
            hide-details
          ></v-checkbox>
          <v-checkbox
            v-model="item.account_onw_role"
            label="Бенефированый владелец"
            value="Бенефированый владелец"
            hide-details
          >
          </v-checkbox>
          <v-checkbox
            v-model="item.account_onw_role"
            label="Подписант"
            value="Подписант"
            hide-details
          ></v-checkbox>
          <p
            v-if="!valid && item.account_onw_role.length < 1"
            class="error_message"
          >
            Выберите пункт
          </p>
          <div class="form_block mt-5">
            <p class="text-left form_block_title">Фамилия</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_lastname"
              placeholder="Введите фамилию"
              class="align-center border-none"
              outlined
              :rules="requiredRules"
              :required="true"
            >
            </v-text-field>
          </div>
          <div class="form_block">
            <p class="text-left form_block_title">Имя</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_name"
              placeholder="Введите имя"
              class="align-center border-none"
              outlined
              :rules="requiredRules"
              :required="true"
            ></v-text-field>
          </div>
          <div class="form_block">
            <p class="text-left form_block_title">Отчество (при наличии)</p>
            <v-text-field
              id="oldName"
              v-model="item.account_own_surname"
              placeholder="Введите отчество"
              class="align-center border-none"
              outlined
              :required="true"
            ></v-text-field>
          </div>
          <v-radio-group v-model="item.account_own_gender" mandatory>
            <v-radio label="Мужской" value="Мужской"></v-radio>
            <v-radio label="Женский" value="Женский"> </v-radio>
          </v-radio-group>
        </div>
        <div class="form_block d-flex align-center justify-center">
          <a
            @click="deleteObjectList(currentData.collegiate_body)"
            class="form_block_delete_link text-decoration-none"
            href="#form_block"
          >
            Отменить
          </a>
          <v-btn
            @click="addObjectList(currentData.collegiate_body)"
            class="
              text-center
              d-flex
              align-center
              justify-center
              ml-10
              add_form
            "
          >
            <span class="pr-3">Добавить</span>
            <v-icon>mdi-plus-circle-outline</v-icon>
          </v-btn>
        </div>
      </div>
      <div class="form_block mt-10">
        <p class="text-left form_block_title">
          Члены коллегиального исполнительного органа
        </p>
        <v-text-field
          id="oldName"
          placeholder="Укажите Физ лицо"
          v-model="currentData.collegiate_person_fio"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
    </v-form>
    <line-step :step="2" />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить</v-btn
    >
  </div>
</template>
<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";
import LineStep from "../../components/line_step/line_step.vue";

export default {
  data: () => ({
    valid: true,
    currentData: {
      supreme_management_body: null,
      supreme_management_type: null,
      supreme_management_inn: null,
      collegiate_body: [
        {
          account_company_name: "",
          account_onw_role: [],
          account_own_lastname: null,
          account_own_gender: null,
          account_own_name: null,
          account_own_surname: null,
        },
      ],
      collegiate_person: null,
      collegiate_person_fio: null,
      supervisory: [
        {
          account_company_name: "",
          account_onw_role: [],
          account_own_lastname: null,
          account_own_gender: null,
          account_own_name: null,
          account_own_surname: null,
        },
      ],
    },
    isTest1: true,
    isTest2: true,
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
      (v) =>
        (v && v.length <= 12) || "ИНН не может содержать больше 12 симоволов",
    ],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.commit("addItemFormData", this.currentData);
        this.$router.push("/documents-forms");
      }
    },
    addObjectList(object) {
      const result = {
        account_onw_role: [],
        account_own_lastname: null,
        account_own_gender: null,
        account_own_name: null,
        account_own_surname: null,
      };
      object.push(result);
    },
    deleteObjectList(object) {
      if (object.length > 1) {
        object.pop();
      }
      // object.pop()
    },
  },
  computed: {
    isLeaderList() {
      return this.$store.getters.isList;
    },
    isLeaderType() {
      return this.$store.getters.isLeaderTypeTitle;
    },
    isManagementCompany() {
      return (
        this.currentData.supreme_management_person === "Управляющая компания"
      );
    },
  },
  components: {
    RadioGroup,
    LineStep,
  },
};
</script>

<style>
.structure_form_title {
  font-family: Geometria;
}
.form_block {
  font-family: Roboto;
  font-size: 14px;
}
.form_block_title {
  font-size: 12px;
  width: 200px;
}
.form_block_label {
  font-family: Roboto;
  color: black;
}
.auth_form_bth {
  border-radius: 10px;
  color: white !important;
  text-transform: capitalize;
  font-size: 14px;
}
</style>