<template>
  <div class="planning_operation_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <h3 class="form_block_label">Виды договоров (контрактов), расчеты по которым юридическое лицо собирается
      осуществлять через банк</h3>
    <div class="form_block">
      <v-checkbox v-model="currentData.planned_operations" label="Договор возмездного оказания услуг"
        value="Договор возмездного оказания услуг" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор поставки" value="Договор поставки"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор подряда" value="Договор подряда"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор комиссии" value="Договор комиссии"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор купли-продажи" value="Договор купли-продажи"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор аренды движимого имущества"
        value="Договор аренды движимого имущества" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор аренды недвижимого имущества"
        value="Договор аренды недвижимого имущества" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор лизинга" value="Договор лизинга"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Договор факторинга" value="Договор факторинга"
        hide-details></v-checkbox>
      <v-checkbox v-model="currentData.planned_operations" label="Иное (укажите)" value="Иное (укажите)"
        hide-details></v-checkbox>

      <v-text-field id="other" v-if="currentData.planned_operations.indexOf('Иное (укажите)') >= 0"
        v-model="currentData.other" placeholder="Иное" class="align-center border-none mt-5" outlined>
      </v-text-field>

    </div>
    <p class="error_message" v-if="!valid && operationlist.length < 1">
      Выберите пункт
    </p>
    <line-step :step='10' class="mt-5" />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '@/components/line_step/line_step.vue';
import { loadCurrentData } from '@/utils/loadStore'

export default {
  data() {
    return {
      valid: true,
      currentData: {
        planned_operations: [],
        other: "",
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
          object: 'step_10',
          value: this.currentData
        })
        this.next();
      }
    },
    next() {
      this.$router.push({ name: "step_11" });
    },
    back() {
      this.$router.push({ name: "step_9" });
    },
  },
  mounted(){
    loadCurrentData({
      currentData: this.currentData,
      step: 'step_10',
      vue: this,
    });
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