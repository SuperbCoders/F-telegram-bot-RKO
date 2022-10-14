<template>
  <div class="planning_operation_section">
    <h3 class="form_block_label">Сведения о планируемых опреациях по счету</h3>
    <div class="form_block">
      <v-checkbox
        v-model="operationlist"
        label="Договор купли продажи (товарный)"
        value="Договор купли продажи (товарный)"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="operationlist"
        label="Агенсткий договор"
        value="Агенсткий договор"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="operationlist"
        label="Договор комиссии"
        value="Договор комиссии"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="operationlist"
        label="Договор купли продажи ценных бумаг"
        value="Договор купли продажи ценных бумаг"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="operationlist"
        label="Договор аренды"
        value="Договор аренды"
        hide-details
      ></v-checkbox>
    </div>
    <p class="error_message" v-if="!valid && operationlist.length < 1">
      Выберите пункт
    </p>
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
import line_step from '../../components/line_step/line_step.vue';

export default {
  data() {
    return {
      valid: true,
      operationlist: [],
    };
  },
  methods: {
    validate() {
      if (this.valid && this.operationlist.length < 1) {
        this.valid = false;
      } else {
        this.valid = true;
        this.$router.push("/beneficiaries");
      }
    },
  },
  components: {
    line_step
  }
};
</script>

<style>
</style>