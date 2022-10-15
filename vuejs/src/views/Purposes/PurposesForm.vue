<template>
  <div class="purposes_block">
    <h4 class="form_block_label text-left">
      Сведения о целях установления деловых отношений с банком
    </h4>
    <div @click="valid = true" class="form_block">
      <v-checkbox label="Рассчетно-кассовое обслуживание" value="Рассчетно-кассовое обслуживание"
        v-model="currentData.informationGoals" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.informationGoals" label="Дистанцинное обслуживание" value="Дистанцинное обслуживание" hide-details></v-checkbox>
      <v-checkbox label="Внешнеэкономическое обслуживание" value="Внешнеэкономическое обслуживание" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.informationGoals" label="Интернет-экваринг" value="Интернет-экваринг" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.informationGoals" label="Кредитование" value="Кредитование" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.informationGoals" label="Торговый экваринг" value="Торговый экваринг" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.informationGoals" label="Переводы СБП (c2b)" color="red" value="red" hide-details></v-checkbox>
    </div>
    <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Количество операций по безлимитным платежам в месяц
      </p>
      <v-radio-group mandatory v-model="currentData.operationCol" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Сумма операций по снятию наличности в месяц
      </p>
      <v-radio-group mandatory v-model="currentData.amoutOfTransaction" column>
        <v-radio label="0 - 99 000 руб" value="0-99 000 руб"></v-radio>
        <v-radio label="100 000 - 1 000 000 руб" value="100 000 - 1 000 000 руб"></v-radio>
        <v-radio label="более 1 000 000 руб" value="более 1 000 000 руб"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-5">
      <p class="form_block_title">
        Количество операций по внешнеторговым контрактам в месяц
      </p>
      <v-radio-group v-model="currentData.operationOfContract" mandatory column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div @click="valid = true" class="form_block mt-5">
      <p class="form_block_title">Источники происхождения денежных средств</p>
      <v-checkbox v-model="currentData.sourceOfOrigin" label="Средства, полученные в рамках осуществляемой хозяйственой деятельности"
        value="Средства, полученные в рамках осуществляемой хозяйственой деятельности" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.sourceOfOrigin" label="Сообственные средства" value="Сооственные средства" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.sourceOfOrigin" label="Заменные средства (займы от третих лиц, учредителей и т.д)"
        value="Заменные средства (займы от третих лиц, учредителей и т.д)" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.sourceOfOrigin" label="Иные" value="Иные" hide-details></v-checkbox>
    </div>
    {{ currentData.sourceOfOrigin }}
    <p v-if="!valid && !isValidatesourceOfOrigin" class="error_message">Выберите поле</p>
    <div class="form_block mt-10">
      <p class="form_block_title">Штатная численость сотрудников</p>
      <v-radio-group mandatory v-model="currentData.numberOfStaff" column>
        <v-radio label="0 - 99 000 руб" value="0-99 000 руб"></v-radio>
        <v-radio label="100 000 - 1 000 000 руб" value="100 000 - 1 000 000 руб"></v-radio>
        <v-radio label="более 1 000 000 руб" value="более 1 000 000 руб"></v-radio>
      </v-radio-group>
    </div>
    <v-btn block large :disabled="!valid" @click="validate" class="mt-10 auth_form_bth" color="primary">Продолжить
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      currentData: {
        informationGoals: [],
        operationCol: null,
        amoutOfTransaction: null,
        operationOfContract: null,
        numberOfStaff: null,
        sourceOfOrigin: []
      }

    }
  },
  methods: {
    validate() {
      if (this.isValidation) {
      }
      else {
        this.valid = false
      }
    },
  },
  computed: {
    isValidateInformationGoals () {
      if (this.currentData.informationGoals.length < 1) {
        return false
      }
      return true
    },
    isValidatesourceOfOrigin () {
      if (this.currentData.sourceOfOrigin.length < 1) {
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
  }
};
</script>

<style>

</style>