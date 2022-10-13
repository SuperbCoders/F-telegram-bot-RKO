<template>
  <div class="imformation_staff_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h2 class="text-left mb-10 font-bold w-50">
        Группа взаимосвязанных компаний
      </h2>
      <div class="form_block">
        <p class="text-left form_block_title">Название группы компаний</p>
        <v-text-field
          id="oldName"
          placeholder="Напишите назание"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата начала действия</p>
        <v-menu
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="xx.xx.xxxx"
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
          <v-date-picker v-model="dateStarting" @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата окончания действия</p>
        <v-menu
          v-model="passportIssueDateMenu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="xx.xx.xxxx"
              id="passportIssueDate"
              name="passportIssueDate"
              append-icon="mdi-calendar-blank"
              outlined
              readonly
              v-model="dateEnd"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="dateEnd" @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>
      </div>
    </v-form>
    <line-step :step='3' />
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
  data: () => ({
    valid: true,
    dateStarting: null,
    dateEnd: null,
    passportIssueDateMenu: null,
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$router.push("/sctructure-group");
      }
    },
  },
  components: {
    LineStep,
  }
};
</script>

<style>
.w-50 {
  width: 50%;
}
</style>