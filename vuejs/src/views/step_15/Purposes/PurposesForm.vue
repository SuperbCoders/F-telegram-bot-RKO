<template>
  <div class="purposes_block">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>

    <h2>Сведения о бизнесе</h2>
    <div>
      <h4 class="form_block_label text-left">
        Компания осуществляет деятельность, подлежащую лицензированию
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.subject_licensing" column>
          <v-radio label="Осуществляет" value="from-10"></v-radio>
          <v-radio label="Не осуществляет" value="from-100"></v-radio>
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
          <v-radio label="Положительная" value="from-10"></v-radio>
          <v-radio label="Отрицательная" value="from-100"></v-radio>
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
          <v-radio label="От 10" value="from-10"></v-radio>
          <v-radio label="От 100" value="from-100"></v-radio>
          <v-radio label="От 1000" value="from-1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в неделю
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.num_transactions_week" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в квартал
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.num_transactions_quarter" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общее количество операций в год
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.num_transactions_age" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_transactions_month" column>
          <v-radio label="До 1 000 000" value="to-1-mln"></v-radio>
          <v-radio label="До 10 000 000" value="to-10-mln"></v-radio>
          <v-radio label="До 100 000 000" value="to-100-mln"></v-radio>
          <v-radio label="Свыше 100 000 000" value="more-100-mln"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в неделю
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.sum_transactions_week" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в квартал
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.sum_transactions_quarter" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Общая сумма операций в год
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.sum_transactions_age" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.monthly_cash_withdrawal" column>
          <v-radio label="От 10" value="from-10"></v-radio>
          <v-radio label="От 100" value="from-100"></v-radio>
          <v-radio label="От 1000" value="from-1000"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в неделю
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.week_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в квартал
      </h4>
      <div class="form_block">
        <v-text-field type="number" outlined v-model="currentData.quarter_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по снятию наличности в год
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.age_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию наличности в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.sum_mouth_cash_withdrawal" column>
          <v-radio label="До 100 000" value="from-0-to-99"></v-radio>
          <v-radio label="До 500 000" value="from-10-to-100"></v-radio>
          <v-radio label="Свыше 500 000" value="more-100"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в неделю
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.sum_week_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в квартал
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.sum_quarter_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по снятию денежных средств в наличной форме в год
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.sum_age_cash_withdrawal" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>


    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_trade_contracts_month" column>
          <v-radio label="От 10" value="from-0-to-29"></v-radio>
          <v-radio label="От 100" value="from-30-to-100"></v-radio>
          <v-radio label="От 1000" value="more-100"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>


    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в неделю
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_trade_contracts_week" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в квартал
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_trade_contracts_quarter"
          class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Количество операций по внешнеторговым контрактам в год
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_trade_contracts_age" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в месяц
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.foreign_sum_contracts_month" column>
          <v-radio label="До 1 000 000" value="to-1-mln"></v-radio>
          <v-radio label="До 10 000 000" value="to-10-mln"></v-radio>
          <v-radio label="До 100 000 000" value="to-100-mln"></v-radio>
          <v-radio label="Свыше 100 000 000" value="more-100-mln"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в неделю
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_sum_contracts_week" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в квартал
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_sum_contracts_quarter" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Сумма операций по внешнеторговым контрактам в год
      </h4>
      <div class="form_block mt-2">
        <v-text-field type="number" outlined v-model="currentData.foreign_sum_contracts_age" class="mt-1 auth_form">
        </v-text-field>
      </div>
    </div>

    <div>
      <h4 class="form_block_label text-left">
        Источники поступления денежных средств
      </h4>
      <div @click="valid = true" class="form_block">
        <v-checkbox label="Финансирование учредителей/участников" value="founderFunding"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Доходы от основного вида деятельности" value="incomeFromMainActivity"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Доходы от дополнительных видов деятельности" value="incomeFromAdditionalActivity"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Заемные (кредитные)/привлеченные денежные средства" value="borrowed"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Государственное финансирование" value="governmentFunding"
          v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
        <v-checkbox label="Иное" value="other" v-model="currentData.sources_cash_receipts" hide-details></v-checkbox>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div class="mt-4">
      <h4 class="form_block_label text-left">
        Штатная численность сотрудников
      </h4>
      <div @click="valid = true" class="form_block">
        <v-text-field type="number" outlined v-model="currentData.headcount" class="mt-1 auth_form">
        </v-text-field>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div class="">
      <h4 class="form_block_label text-left">
        Имеются постоянные или предполагаемые плательщики по операциям с денежными средствами на счете
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.hasConstantPayers" column>
          <v-radio label="Да" value="Да"></v-radio>
          <v-radio label="Нет" value="Нет"></v-radio>
        </v-radio-group>

      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div class="mt-4" v-if="currentData.hasConstantPayers == 'Да'">
      <h4 class="form_block_label text-left">
        Наименование и ИНН организации
      </h4>
      <div @click="valid = true" class="form_block">
        <v-text-field type="text" outlined v-model="currentData.hasConstantPayersDetails" class="mt-1 auth_form">
        </v-text-field>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div class="mt-4">
      <h4 class="form_block_label text-left">
        Имеются постоянные или предполагаемые получатели по операциям с денежными средствами на счете
      </h4>
      <div @click="valid = true" class="form_block">
        <v-radio-group v-model="currentData.hasConstantRecipient" column>
          <v-radio label="Да" value="Да"></v-radio>
          <v-radio label="Нет" value="Нет"></v-radio>
        </v-radio-group>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <div class="mt-4" v-if="currentData.hasConstantRecipient == 'Да'">
      <h4 class="form_block_label text-left">
        Наименование и ИНН организации
      </h4>
      <div @click="valid = true" class="form_block">
        <v-text-field type="text" outlined v-model="currentData.hasConstantRecipientDetails" class="mt-1 auth_form">
        </v-text-field>
      </div>
      <p v-if="!valid && !isValidateInformationGoals" class="error_message">Выберите поле</p>
    </div>

    <line-step :step='number_step' class="mt-5" />
    <v-btn block large :disabled="!valid" @click="validate" class="mt-10 auth_form_bth" color="primary">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '@/components/line_step/line_step.vue';
import { loadCurrentData } from '@/utils/loadStore'

export default {
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      valid: true,
      currentData: {
        subject_licensing: "",
        history_reputation: "",
        num_transactions_month: "",
        num_transactions_week: "",
        num_transactions_quarter: "",
        num_transactions_age: "",
        sum_transactions_month: "",
        sum_transactions_week: "",
        sum_transactions_quarter: "",
        sum_transactions_age: "",
        monthly_cash_withdrawal: "",
        week_cash_withdrawal: "",
        quarter_cash_withdrawal: "",
        age_cash_withdrawal: "",
        sum_mouth_cash_withdrawal: "",
        sum_week_cash_withdrawal: "",
        sum_quarter_cash_withdrawal: "",
        sum_age_cash_withdrawal: "",
        foreign_trade_contracts_month: "",
        foreign_trade_contracts_week: "",
        foreign_trade_contracts_quarter: "",
        foreign_trade_contracts_age: "",
        foreign_sum_contracts_month: "",
        foreign_sum_contracts_week: "",
        foreign_sum_contracts_quarter: "",
        foreign_sum_contracts_age: "",
        sources_cash_receipts: [],
        headcount: "",
        hasConstantPayers: "",
        hasConstantPayersDetails: "",
        hasConstantRecipient: "",
        hasConstantRecipientDetails: "",
      }

    }
  },
  methods: {
    validate() {
      this.$store.dispatch('addObjectFormData', {
        object: `step_${this.number_step}`,
        value: this.currentData
      })
      this.next();
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
    },
  },
  mounted() {
    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });
  },
  computed: {
    isValidateInformationGoals() {
      if (this.currentData.account_operations.length < 1) {
        return false
      }
      return true
    },
    isValidatesourceOfOrigin() {
      if (this.currentData.sources_cash_receipts.length < 1) {
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