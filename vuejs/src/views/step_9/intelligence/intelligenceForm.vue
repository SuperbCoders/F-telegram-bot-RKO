<template>
  <div class="intelligence_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>
      <h2 class="text-left mb-10">Сведения о персонале</h2>
      <div class="form_block mt-5">
        <p class="text-left form_block_title"><span class="star">*</span>Численность персонала</p>
        <v-text-field id="oldName" v-model="currentData.employers_volume" placeholder="Напишите значение"
          class="align-center border-none" name="oldName" type="number" :rules="requiredRules" outlined
          :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_input"><span class="star">*</span>Задолженность по з/п</p>
        <v-text-field id="oldName" v-model="currentData.salary_debt" placeholder="Укажите сумму"
          class="align-center border-none" name="oldName" type="number" :rules="requiredRules"
          append-icon="mdi-currency-rub" outlined :required="true"></v-text-field>
        <line-step :step='number_step' />
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
          Продолжить
        </v-btn>
      </div>
    </v-form>
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
      requiredRules: [(v) => v !== "" || "Это поле обязательно"],
      test: false,
      currentData: {
        employers_volume: "",
        salary_debt: 0
      }
    }
  },
  methods: {
    async validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: `step_${this.number_step}`,
          value: this.currentData
        })
        this.next();
      }
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
    },
    onClose() {
      this.$refs.employers_volume.blur()
      this.$refs.salary_debt.blur()
    },
  },
  mounted() {
    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });
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