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
      <p class="text-left form_block_input">Задолженность по з/п</p>
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
    >
      Продолжить
    </v-btn>
    </div>
  </v-form>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
import { getLicense } from '../../api/getLicense';

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
    async validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: 'step_12',
          value: this.currentData
        })
        const data = await getLicense();
        console.log(data);
        
        const store = {};
        
        store.licence_type = data.view;
        store.licence_number = data.number;
        store.licence_issued_by = data.Issued_by;
        store.licence_date_issue = data.License_issue_date;
        store.licenced_validity = data.Validity;
        store.licenced_activity = data.List_types_licensed_activities;

        this.$store.dispatch('addObjectFormData', {
          object: 'step_13',
          value: store
        })
        this.$router.push("/planning");
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