<template>
  <div class="client_info_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Место рождения</p>
        <v-text-field
          id="oldName"
          placeholder="Введите адрес"
          class="align-center border-none"
          outlined
          v-model="currentData.account_birth_place"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата рождения</p>
        <v-menu
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          class="client_info_datapicker"
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="Дата"
              id="passportIssueDate"
              name="passportIssueDate"
              outlined
              append-icon="mdi-calendar-blank"
              readonly
              v-model="currentData.account_datebirth"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="currentData.account_datebirth"
            :min="isDate()"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Тип документа удостоверяющего личность
        </p>
        <v-select
          filled
          outlined
          :rules="requiredRules"
          v-model="currentData.doc_type"
          placeholder="Выберите тип"
          :items="type_document"
        ></v-select>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Серия документа удостоверяющего личность (при наличии)
        </p>
        <v-text-field
          id="oldName"
          placeholder="Введите серию документа"
          class="align-center border-none"
          v-mask="'## ##'"
          masked="true"
          v-model="currentData.doc_serial"
          outlined
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Номер документа удостоверяющего личность
        </p>
        <v-text-field
          id="oldName"
          placeholder="Введите номер документа"
          class="align-center border-none"
          v-mask="'## ## ##'"
          masked="true"
          outlined
          v-model="currentData.doc_number"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Кем выдан</p>
        <v-text-field
          id="oldName"
          placeholder="Наименование"
          class="align-center border-none"
          outlined
          v-model="currentData.issued_by"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Код подзразделения (при наличии)
        </p>
        <v-text-field
          id="oldName"
          placeholder="Введите имя"
          v-model="currentData.division_code"
          class="align-center border-none"
          v-mask="'###-###'"
          masked="true"
          outlined
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата выдачи</p>
        <v-menu
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="Дата"
              id="passportIssueDate"
              name="passportIssueDate"
              outlined
              append-icon="mdi-calendar-blank"
              readonly
              v-model="currentData.date_issue"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="currentData.date_issue"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Срок действия</p>
        <v-menu
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="Дата"
              id="passportIssueDate"
              name="passportIssueDate"
              outlined
              append-icon="mdi-calendar-blank"
              readonly
              v-model="currentData.validity"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="currentData.validity"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
    </v-form>
    <line-step :step='10' />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
import { mask } from "vue-the-mask";
export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listRole: [],
    currentData: {
      placeOfBirth: null,
      typeDocumnet: null,
    },
    dateStarting: null,
    dateEnd: null,
    test: [],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
    type_document: ["Паспорт"],
  }),
  methods: {
    validate() {
      // let isStatusFogeiner = this.$store.state.isForegin;
      this.$store.commit("IsFormData");
      const isStatusFogeiner =
        this.$store.state.result.assigned_publ_pers_relation;
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        if (isStatusFogeiner) {
          this.$router.push("/document-fogeiner");
        } else {
          this.$router.push("/information-staff");
        }
        this.$store.commit("addItemFormData", this.currentData);
      }
    },
    isDate() {
      const year = new Date();
      // const month = new Date().getMonth()
      // const day = new Date().getDate()
      return this.toJSONLocal(year)
      // console.log(this.toJSONLocal(year));
      // console.log(year, month, day)
    },
    toJSONLocal(date) {
      const local = new Date(date)
      local.setMinutes(date.getMinutes() - date.getTimezoneOffset());
      return local.toJSON().slice(0, 10);
    },
  },
  computed: {
    // test() {
    //   const year = new Date().getFullYear();
    //   console.log(year);
    //   return year;
    // },
  },
  components: {
    LineStep
  }
};
</script>

<style>
.client_info_datapicker {
  max-width: 100%;
}
</style>