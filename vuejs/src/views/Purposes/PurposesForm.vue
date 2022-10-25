<template>
  <div class="purposes_block">
    <h4 class="form_block_label text-left">
      Сведения о целях установления деловых отношений с банком
    </h4>
    <div @click="valid = true" class="form_block">
      <v-checkbox label="Рассчетно-кассовое обслуживание" value="Расчетно-кассовое обслуживание"
        v-model="currentData.account_operations" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.account_operations" label="Дистанционное обслуживание" value="Дистанционное обслуживание" hide-details></v-checkbox>
      <v-checkbox label="Внешнеэкономические операции" value="Внешнеэкономические операции" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.account_operations" label="Интернет-эквайринг" value="Интернет-эквайринг" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.account_operations" label="Кредитование" value="Кредитование" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.account_operations" label="Торговый эквайринг" value="Торговый эквайринг" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.account_operations" label="Переводы СБП (c2b)"  value="Переводы СБП (c2b)" hide-details></v-checkbox>
    </div>
    <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Количество операций по безналичным платежам в месяц
      </p>
      <v-radio-group v-model="currentData.operation_volume" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Сумма операций по безналичным платежам в месяц
      </p>
      <v-radio-group v-model="currentData.operation_sum" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Количество операций по снятию наличности в месяц
      </p>
      <v-radio-group v-model="currentData.operation_nalition" column>
        <v-radio label="0-29 000 руб" value="0-29 000 руб"></v-radio>
        <v-radio label="100 000-1 000 000 руб" value="100 000-1 000 000 руб"></v-radio>
        <v-radio label="более 1 000 000 руб" value="более 1 000 000 руб"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Сумма операций по снятию наличности в месяц
      </p>
      <v-radio-group v-model="currentData.sum_per_month" column>
        <v-radio label="0 - 99 000 руб" value="0-99 000 руб"></v-radio>
        <v-radio label="100 000 - 1 000 000 руб" value="100 000 - 1 000 000 руб"></v-radio>
        <v-radio label="более 1 000 000 руб" value="более 1 000 000 руб"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-5">
      <p class="form_block_title">
        Количество операций по внешнеторговым контрактам в месяц
      </p>
      <v-radio-group v-model="currentData.outside_contracts_volume" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div @click="valid = true" class="form_block mt-5">
      <p class="form_block_title">Источники происхождения денежных средств</p>
      <v-checkbox v-model="currentData.cash_source" label="Средства, полученные в рамках осуществляемой хозяйственной деятельности"
        value="Средства, полученные в рамках осуществляемой хозяйственой деятельности" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.cash_source" label="Собственные средства" value="Сооственные средства" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.cash_source" label="Заемные средства (займы от третьих лиц, учредителей и т.д)"
        value="Заменные средства (займы от третьих лиц, учредителей и т.д)" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.cash_source" label="Иные" value="Иные" hide-details></v-checkbox>
    </div>
    <p v-if="!valid && !isValidatesourceOfOrigin" class="error_message">Выберите поле</p>
    <div class="form_block mt-10">
      <p class="form_block_title">Штатная численность сотрудников</p>
      <v-radio-group v-model="currentData.state_employers" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <line-step :step='7' class="mt-5"/>
    <v-btn block large :disabled="!valid" @click="validate" class="mt-10 auth_form_bth" color="primary">Продолжить
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
        account_operations: [],
        operation_volume: null,
        sum_per_month: null,
        outside_contracts_volume: null,
        state_employers: null,
        cash_source: []
      }

    }
  },
  methods: {
    validate() {
      if (this.isValidation) {
        this.$store.dispatch('addObjectFormData', {
          object: 'step_16',
          value: this.currentData
        })
        this.$router.push('/approvals')
      }
      else {
        this.valid = false
      }
    },
  },
  computed: {
    isValidateInformationGoals () {
      if (this.currentData.account_operations.length < 1) {
        return false
      }
      return true
    },
    isValidatesourceOfOrigin () {
      if (this.currentData.cash_source.length < 1) {
        return false
      }
      return true
    },
    isValidation () {
      if (this.isValidateInformationGoals && this.isValidatesourceOfOrigin ) {
        return true
      }
      return false
    }
  },
  components: {
    LineStep
  }
};
</script>

<style>
.purposes_block .v-label {
  color: #323E48 !important;
}
</style>