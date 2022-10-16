<template>
  <div class="license_information_form">
    <v-form ref="form" v-model="valid" lazy-validation>
    <h2 class="form_block_label">Сведения о лицензии</h2>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Вид</p>
      <v-text-field
        id="oldName"
        placeholder="xxxxxx"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
        outlined
        v-model="currentData.licence_type"
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">Номер</p>
      <v-text-field
        id="oldName"
        placeholder="xxxxxx"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
        outlined
        v-model="currentData.licence_number"
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">Кем выдан</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        v-model="currentData.licence_issued_by"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">Дата выдачи лицензии</p>
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
            v-model="currentData.licence_date_issue"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="currentData.licence_date_issue"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div>
    <!-- <div class="form_block">
      <p class="text-left form_block_title">
        Срок дей
      </p>
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
            v-model="dateStarting"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStarting"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div> -->
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
            v-model="currentData.licenced_validity"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="currentData.licenced_validity"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">
        Перечень видов лицензируемой деятельности
      </p>
      <v-text-field
        id="oldName"
        placeholder="xxxxxx"
        class="align-center border-none"
        name="oldName"
        v-model="currentData.licenced_activity"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    </v-form>
    <line-step :step='12' />
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
import LineStep from '../../components/line_step/line_step.vue';
export default {
  data() {
    return {
      isAddress: false,
      valid: true,
      show1: false,
      currentData: {

      },
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/planning");
      }
    },
  },
  components: {
    LineStep,
  }
};
</script>

<style>
</style>