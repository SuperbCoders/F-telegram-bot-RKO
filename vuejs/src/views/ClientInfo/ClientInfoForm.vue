<template>
  <div class="client_info_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Место рождения</p>
        <AddressInput label="Введите адрес" v-model="currentData.account_birth_place" />
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Дата рождения</p>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="isActivePicker()"
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
              @click="currentData.account_datebirth = ''"
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
            :active-picker.sync="activePicker"
            :max="isDate()"
            min="1950-01-01"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Тип документа, удостоверяющего личность
        </p>
        <v-select
          filled
          outlined
          :rules="requiredRules"
          v-model="currentData.doc_type"
          placeholder="Выберите тип"
          :items="type_document"
          :required="true"
        ></v-select>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Серия документа удостоверяющего личность
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
          <span class="star">*</span>Номер документа удостоверяющего личность
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
        <p class="text-left form_block_title"><span class="star">*</span>Кем выдан</p>
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
          placeholder="Введите код"
          v-model="currentData.division_code"
          class="align-center border-none"
          v-mask="'###-###'"
          masked="true"
          outlined
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Дата выдачи</p>
        <v-menu
          :close-on-content-click="isActivePickerIssue()"
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
              @click="currentData.validity = ''"
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
            :active-picker.sync="activePickerIssue"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Срок действия</p>
        <v-menu
          :close-on-content-click="isActivePickerValidity()"
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
            :min="currentData.date_issue"
            @input="passportIssueDateMenu = false"
            :active-picker.sync="activePickerValidity"
          ></v-date-picker>
        </v-menu>
      </div>
    </v-form>
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
import { mask } from "vue-the-mask";
import AddressInput from '../../components/addressInput.vue';

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listRole: [],
    currentData: {
      placeOfBirth: null,
      typeDocumnet: null,
      account_datebirth: null,
      date_issue: '',
      validity: '',
    },
    account_datebirth: null,
    dateStarting: null,
    dateEnd: null,
    test: [],
    activePicker: null,
    activePickerIssue: null,
    activePickerValidity: null,
    date: null,
    menu: false,
    requiredRules: [(v) => !!v || "Это поле обязательно"],
    type_document: ["Паспорт"],
  }),
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    }
  },
  methods: {
    validate() {
      // let isStatusFogeiner = this.$store.state.isForegin;
      const isStatusFogeiner =
        this.$store.state?.supervisoryBoardPersone?.['page-3']?.assigned_publ_pers_relation;
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        if(this.$route.query?.type === 'SupervisoryBoard') {
          this.$store.commit("setSupervisoryBoardPersone", {key: "page-8", value: this.currentData});
        }else if(this.$route.query?.type === 'CollegialExecutive') {
          this.$store.commit("setCollegialExecutiveBody", {key: "page-8", value: this.currentData});
        }

        if (isStatusFogeiner === 'Да') {
          this.$router.push({path:"/document-fogeiner", query: this.$route.query});
        } else {
          this.$router.push({path:"/all-data-persone", query: this.$route.query});
        }
      }
    },
    // validityNull () {
    //   currentData.validity = ''
    // },
    isDate() {
      const year = new Date().getFullYear() - 18;
      return `${year}-12-31`;
    },
    isActivePicker () {
      if (this.currentData.account_datebirth !=='' && this.activePicker === 'DATE') {
        return true
      }
      return false
    },
    isActivePickerIssue () {
      if (this.currentData.date_issue !=='' && this.activePickerIssue === 'DATE') {
        return true
      }
      return false
    },
    isActivePickerValidity () {
      if (this.currentData.validity !=='' && this.activePickerValidity === 'DATE') {
        return true
      }
      return false
    },
    toJSONLocal(date) {
      const local = new Date(date);
      return local.toJSON().slice(0, 10);
    },
  },
  computed: {
  },
  components: {
    AddressInput
  },
};
</script>

<style>
.client_info_datapicker {
  max-width: 100%;
}
</style>