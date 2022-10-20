<template>
  <div class="intelligence_section">
    <v-form ref="form" v-model="valid" lazy-validation>
    <h2 class="text-left mb-10">Сведения о персонале</h2>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Численность персонала</p>
      <v-text-field
        id="oldName"
        v-model="currentData.employers_volume"
        placeholder="Напишите значение"
        class="align-center border-none"
        name="oldName"
        type="number"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_input">Задолжность по з/п</p>
      <v-text-field
        id="oldName"
        v-model="currentData.salary_debt"
        placeholder="Укажите сумму"
        class="align-center border-none"
        name="oldName"
        type="number"
        :rules="requiredRules"
        append-icon="mdi-currency-rub"
        outlined
        :required="true"
      ></v-text-field>
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
  </v-form>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
export default {
  data() {
    return {
      valid: true,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
      test: false,
      currentData: {
        employers_volume: null,
        salary_debt: null
      }
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: 'step_12',
          value: this.currentData
        })
        this.$router.push('/license-info')
      }
    },
  },
  components: {
    LineStep
  }
}
</script>

<style>
.form_block_input {
  font-family: face;
  color: #8E909B;
  font-size: 13px;
}
.form_block_title {
  font-size: 13px;
  font-family: face;
  color: #8E909B;
}
</style>