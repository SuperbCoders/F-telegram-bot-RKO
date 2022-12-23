<template>
  <div class="purposes_block">
    <h2>Сведения о бизнесе</h2>
    <div>
      <h4 class="form_block_label text-left">
        Компания осуществляет деятельность, подлежащую лицензированию
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.subject_licensing" column>
          <v-radio label="Осуществляет" value="Осуществляет"></v-radio>
          <v-radio label="Не осуществляет" value="Не осуществляет"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>
    <div>
      <h4 class="form_block_label text-left">
        История, репутация, сектор рынка и конкуренция
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.history_reputation" column>
          <v-radio label="Положительная" value="Положительная"></v-radio>
          <v-radio label="Отрицательная" value="Отрицательная"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.num_transactions_month" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.num_transactions_week" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.num_transactions_quarter" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.num_transactions_age" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_transactions_month" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_transactions_week" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_transactions_quarter" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_transactions_age" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.monthly_cash_withdrawal" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.week_cash_withdrawal" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.quarter_cash_withdrawal" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.age_cash_withdrawal" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>



    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию наличности в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_mouth_cash_withdrawal" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_week_cash_withdrawal" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_quarter_cash_withdrawal" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_age_cash_withdrawal" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    
    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_trade_contracts_month" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>


    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_trade_contracts_week" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_trade_contracts_quarter" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_trade_contracts_age" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_sum_contracts_month" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в неделю
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_sum_contracts_week" column>
          <v-radio label="До 1 000 000" value="До 1 000 000"></v-radio>
          <v-radio label="До 10 000 000" value="До 10 000 000"></v-radio>
          <v-radio label="До 100 000 000" value="До 100 000 000"></v-radio>
          <v-radio label="Свыше 100 000 000" value="Свыше 100 000 000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в квартал
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_sum_contracts_quarter" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в год
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_sum_contracts_age" column>
          <v-radio label="От 10" value="От 10"></v-radio>
          <v-radio label="От 100" value="От 100"></v-radio>
          <v-radio label="От 1000" value="От 1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Источники поступления денежных средств
      </h4>
      <div @click="valid = true" class="form_block">
        <v-checkbox label="Финансирование учредителей/участников" value="Финансирование учредителей/участников"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Доходы от основного вида деятельности" value="Доходы от основного вида деятельности"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Доходы от дополнительных видов деятельности"
          value="Доходы от дополнительных видов деятельности" v-model="currentData.sources_cash_receipts"
          hide-details></v-checkbox>
        <v-checkbox label="Заемные (кредитные)/привлеченные денежные средства"
          value="Заемные (кредитные)/привлеченные денежные средства" v-model="currentData.sources_cash_receipts"
          hide-details></v-checkbox>
        <v-checkbox label="Государственное финансирование" value="Государственное финансирование"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Иное" value="Иное" v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Штатная численность сотрудников
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.headcount" column>
          <v-radio label="Единственным работником является единоличный исполнительный орган" value="Единственным работником является единоличный исполнительный орган"></v-radio>
          <v-radio label="2-5" value="2-5"></v-radio>
          <v-radio label="6-20" value="6-20"></v-radio>
          <v-radio label="Более 20" value="Более 20"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <line-step :step='7' class="mt-5" />
    <v-btn block large :disabled="!valid" @click="validate" class="mt-10 auth_form_bth" color="primary">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '@/components/line_step/line_step.vue';
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
          object: 'step_6',
          value: this.currentData
        })
        this.next();
      }
      else {
        this.valid = false
      }
    },
    next() {
      this.$router.push({ name: 'step_9' })
    },
  },
  computed: {
    isValidateInformationGoals() {
      if (this.currentData.account_operations.length < 1) {
        return false
      }
      return true
    },
    isValidatesourceOfOrigin() {
      if (this.currentData.cash_source.length < 1) {
        return false
      }
      return true
    },
    isValidation() {
      if (this.isValidateInformationGoals && this.isValidatesourceOfOrigin) {
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