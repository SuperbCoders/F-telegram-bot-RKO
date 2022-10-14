<template>
  <div class="status_kinship_block">
    <v-form ref="form" v-model="valid" lazy-validation>
    <div class="form_block">
      <p class="text-left form_block_label">
        Степень родства либо статус (супруг или супруга) по отношению к
        публичному должностному лицу
      </p>
      <v-select
          :items="relationDegree"
          label="Степень родства"
          filled
          :rules="requiredRules"
          required
          outlined
          placeholder="Выберите из списка"
        ></v-select>
      <div class="form_block">
        <p class="text-left form_block_title">Адрес регистрации</p>
        <v-text-field
          id="oldName"
          placeholder="Введите имя"
          class="align-center border-none"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Адресс регистрации</p>
        <v-text-field
          id="oldName"
          placeholder="Введите имя"
          class="align-center border-none"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
    </div>
    </v-form>
    <line-step :step='6' class="mt-5" />
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

export default {
  data: () => ({
    valid: true,
    listRole: [],
    dateStarting: null,
    dateEnd: null,
    test: [],
    relationDegree: [
      "Супруг",
      "Супруга"
    ],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$router.push("/address-form");
      }
    },
  },
  components: { LineStep },
};
</script>

<style>
</style>