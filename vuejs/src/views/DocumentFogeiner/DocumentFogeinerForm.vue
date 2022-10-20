<template>
  <div class="document_fogeiner_block">
    <h4>
      ДАННЫЕ ДОКУМЕНТА, ПОТВЕРЖДАЮЩЕГО ПРАВО ИНОСТРАННОГО ГРАЖДАНИНА ИЛИ ЛИЦА
      БЕЗ ГРАЖДНСТВА НА ПРЕБЫВАНИЯ(ПРОЖИВАНИЯ) В РФ
    </h4>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block mt-5">
        <p class="text-left form_block_title">Тип документа</p>
        <v-combobox
          filled
          outlined
          :items="docType"
          :rules="requiredRules"
          v-model="currentData.foreigner_doc_type"
          placeholder="Выберите тип"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Серия (если имеется)</p>
        <v-text-field
          id="oldName"
          v-mask="'## ##'"
          masked="true"
          placeholder="Введите серию документа"
          class="align-center border-none"
          outlined
          v-model="currentData.foreigner_doc_serial"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Номер документа удостоверяющего личность
        </p>
        <v-text-field
          id="oldName"
          v-mask="'### ###'"
          masked="true"
          placeholder="Введите номер документа"
          class="align-center border-none"
          outlined
          v-model="currentData.foreigner_doc_number"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Дата начала срока действия права пребывания(проживания)
        </p>
        <v-menu
          :close-on-content-click="true"
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
              @click="currentData.foreigner_doc_validity = ''"
              v-model="currentData.foreigner_doc_issued"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            :min="currentData.foreigner_doc_number"
            v-model="currentData.foreigner_doc_issued"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">
          Дата окончания срока действия пребывания (проживания)
        </p>
        <v-menu
          :close-on-content-click="true"
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
              v-model="currentData.foreigner_doc_validity"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            :min="currentData.foreigner_doc_issued"
            v-model="currentData.foreigner_doc_validity"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
    </v-form>
    <LineStep :step="11" class="mt-5" />
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
import LineStep from "../../components/line_step/line_step.vue";

export default {
  data: () => ({
    valid: true,
    listRole: [],
    dateStarting: null,
    dateEnd: null,
    docType: ["Паспорт"],
    currentData: {
      foreigner_doc_type: "",
      foreigner_doc_serial: "",
      foreigner_doc_number: "",
      foreigner_doc_issued: "",
      foreigner_doc_validity: "",
    },
    test: [],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$router.push("/information-staff");
      }
    },
    foreigner_doc_validity_null() {
      this.foreigner_doc_validity = "";
    },
  },
  components: {
    LineStep,
  },
};
</script>

<style>
</style>