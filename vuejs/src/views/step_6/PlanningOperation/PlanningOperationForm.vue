<template>
  <div class="planning_operation_section">
    <h3 class="form_block_label">Сведения о планируемых операциях по счету</h3>
    <div class="form_block">
      <v-checkbox
        v-model="currentData.planned_operations"
        label="Договор купли-продажи (товарный)"
        value="Договор купли-продажи (товарный)"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="currentData.planned_operations"
        label="Агентский договор"
        value="Агентский договор"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="currentData.planned_operations"
        label="Договор комиссии"
        value="Договор комиссии"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="currentData.planned_operations"
        label="Договор купли-продажи ценных бумаг"
        value="Договор купли-продажи ценных бумаг"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="currentData.planned_operations"
        label="Договор аренды"
        value="Договор аренды"
        hide-details
      ></v-checkbox>
    </div>
    <p class="error_message" v-if="!valid && operationlist.length < 1">
      Выберите пункт
    </p>
    <line-step :step='5' class="mt-5"/>
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
  data() {
    return {
      valid: true,
      currentData: {
        planned_operations: []
      },
    };
  },
  methods: {
    validate() {
      if (this.valid && this.currentData.planned_operations.length < 1) {
        this.valid = false;
      } else {
        this.valid = true;
        this.$store.dispatch('addObjectFormData', {
          object: 'step_7',
          value: this.currentData
        })
        this.$router.push("/beneficiaries");
      }
    },
  },
  components: {
    LineStep
  }
};
</script>

<style>
.planning_operation_section .v-label {
  color: #000 !important;
}
</style>