<template>
  <div class="client_info_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Место рождения</p>
        <v-text-field placeholder="Введите адрес" outlined v-model="currentData.account_birth_place"
          :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Дата рождения</p>
        <v-text-field placeholder="Дата рождения" outlined v-model="currentData.account_datebirth"
          :rules="requiredRules" :required="true" v-mask="'##.##.####'"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Тип документа, удостоверяющего личность
        </p>
        <v-select filled outlined :rules="requiredRules" v-model="currentData.doc_type" placeholder="Выберите тип"
          :items="type_document" item-value="key" item-text="value" item-label="value" :required="true"></v-select>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Серия документа удостоверяющего личность
        </p>
        <v-text-field id="oldName" placeholder="Введите серию документа" class="align-center border-none"
          v-mask="'## ##'" masked="true" v-model="currentData.doc_serial" outlined :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Номер документа удостоверяющего личность
        </p>
        <v-text-field id="oldName" placeholder="Введите номер документа" class="align-center border-none"
          v-mask="'## ## ##'" masked="true" outlined v-model="currentData.doc_number" :rules="requiredRules"
          :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Кем выдан</p>
        <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" outlined
          v-model="currentData.issued_by" :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          <span class="star">*</span>Код подразделения
        </p>
        <v-text-field id="oldName" placeholder="Введите код" v-model="currentData.division_code"
          class="align-center border-none" v-mask="'###-###'" masked="true" outlined :rules="requiredRules"
          :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Дата выдачи</p>
        <v-text-field placeholder="Дата рождения" outlined v-model="currentData.date_issue" :rules="requiredRules"
          :required="true" v-mask="'##.##.####'"></v-text-field>
      </div>
    </v-form>
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import { mask } from "vue-the-mask";
import { loadSubCurrentData } from '@/utils/loadStore'

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listRole: [],
    currentData: {
      account_birth_place: "",
      account_datebirth: "",
      doc_type: "",
      doc_serial: "",
      doc_number: "",
      issued_by: "",
      division_code: "",
      date_issue: "",
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
    type_document: [
      {
        key: 21,
        value: "Паспорт гражданина Российской Федерации"
      },
      {
        key: 22,
        value: "Дипломатический паспорт, служебный паспорт, удостоверяющие личность гражданина РФ за пределами РФ"
      },
      {
        key: 26,
        value: "Временное удостоверение личности гражданина РФ, выдаваемое на период оформления паспорта гражданина РФ"
      },
      {
        key: 27,
        value: "Свидетельство о рождении гражданина РФ (для граждан РФ в возрасте до 14 лет)"
      },
      {
        key: 28,
        value: "Иные документы, признаваемые документами, удостоверяющими личность гражданина РФ в соответствии с законодательством РФ",
      },
    ],
  }),
  watch: {
    menu(val) {
      val && setTimeout(() => (this.activePicker = "YEAR"));
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("setPersone", { key: "substep_5", value: this.currentData, index: this.$route.params?.id });

        this.$router.push({ name: "substep_6", params: { id: this.$route.params.id } });
      }
    },
    back() {
      this.$router.push({ name: "substep_4", params: { id: this.$route.params.id } });
    },
    // validityNull () {
    //   currentData.validity = ''
    // },
    isDate() {
      const year = new Date().getFullYear() - 18;
      return `${year}-12-31`;
    },
    isActivePicker() {
      if (this.currentData.account_datebirth !== '' && this.activePicker === 'DATE') {
        return true
      }
      return false
    },
    isActivePickerIssue() {
      if (this.currentData.date_issue !== '' && this.activePickerIssue === 'DATE') {
        return true
      }
      return false
    },
    isActivePickerValidity() {
      if (this.currentData.validity !== '' && this.activePickerValidity === 'DATE') {
        return true
      }
      return false
    },
    toJSONLocal(date) {
      const local = new Date(date);
      return local.toJSON().slice(0, 10);
    },
  },
  mounted() {
    loadSubCurrentData({
      currentData: this.currentData,
      substep: "substep_5",
      vue: this,
      index: this.$route.params.id
    })
  },
  computed: {
  },
  components: {
  },
};
</script>

<style>
.client_info_datapicker {
  max-width: 100%;
}
</style>