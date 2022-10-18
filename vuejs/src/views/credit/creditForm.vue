<template>
  <div class="credit_section text-center">
    <p class="credit_section_title blue-grey--text">
      <span class="credit_section_title">Сумма кредите:</span>
      <span class="primary--text">
        {{ getFormattedCurrency(formData["loanAmount"]) }} &#8381;</span
      >
    </p>
    <v-slider
      :max="5000000"
      :min="1000000"
      v-model="formData['loanAmount']"
      step="500000"
      track-color="#F1BAD2"
      track-fill-color="primary"
    ></v-slider>
    <p class="credit_section_title">
      Срок:
      <span class="primary--text ">
        {{ formData["loanTerm"] }}
        {{ getFormattedYearNoun(formData["loanTerm"]) }}
      </span>
    </p>
    <v-slider
      class="d-none d-sm-block"
      :tick-labels="loanTermTickLabels"
      :max="6"
      :min="2"
      step="1"
      v-model="formData['loanTerm']"
      ticks
      track-color="#F1BAD2"
      track-fill-color="primary"
      tick-size="5"
    ></v-slider>
    <v-slider
      class="d-sm-none"
      v-model="formData['loanTerm']"
      :tick-labels="smallLoanTermTickLabels"
      :max="6"
      :min="2"
      track-color="#F1BAD2"
      track-fill-color="primary"
    ></v-slider>
    <p class="mt-5 pay_text grey--text">Ежемесячный платеж</p>
    <v-scroll-y-transition hide-on-leave>
      <p :key="monthlyPayment" class="display-1 primary--text">
        {{ getFormattedCurrency(monthlyPayment()) }} &#8381;
      </p>
    </v-scroll-y-transition>
    <p class="grey--text">
      Сумма переплаты:
      <span class="black--text"
        >
        {{ getFormattedCurrency(interestAmount()) }} &#8381;
      </span
      >
    </p>
    <p class="grey--text">
      Сумма кредита:
      <span class="black--text"
        >
        {{ getFormattedCurrency(totalLoanAmount()) }} &#8381;
        </span>
    </p>
    <p class="grey--text">
      Процентная ставка:
      <span class="black--text">{{ interestRate * 100 }}%</span>
    </p>
    <LineStep :step="5" />
    <v-btn block large class="mt-10 auth_form_bth" color="primary">
      <router-link
        class="auth_form_bth color-white text-decoration-none"
        to="/document"
      >
        Продолжить
      </router-link>
    </v-btn>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
export default {
  data() {
    return {
      formData: {
        loanAmount: 0
      },
      loanTermTickLabels: ["2 года", "3 года", "4 года", "5 лет", "6 лет"],
      smallLoanTermTickLabels: ["2 года", "", "4 года", "", "6 лет"],
      interestRate: 0.05,
    };
  },
  methods: {
    getFormattedCurrency: function (number) {
      if (number) {
        return parseFloat(number).toLocaleString("ru-RU");
      }
    },
    interestAmount: function () {
      let loanTerm = this.formData["loanTerm"] * 12 || 24;
      let loanAmount = this.formData["loanAmount"] || 1000000;
      let result = this.monthlyPayment() * loanTerm - loanAmount;
      return parseFloat(result).toFixed(2);
    },
    totalLoanAmount: function () {
      let loanAmount = this.formData["loanAmount"] || 1000000;
      let result = parseFloat(loanAmount) + parseFloat(this.interestAmount());
      return result.toFixed(2);
    },
    monthlyPayment: function () {
      let r = this.interestRate / 12;
      let n = this.formData["loanTerm"] * 12 || 24;
      let P = this.formData["loanAmount"] || 1000000;
      let result = (P * (r * (1 + r) ** n)) / ((1 + r) ** n - 1);
      return parseFloat(result).toFixed(2);
    },
    getFormattedYearNoun: function (number) {
      const ORDER = [2, 0, 1, 1, 1, 2];
      const DECLENSIONS = ["год", "года", "лет"];
      let declension =
        number % 100 > 4 && number % 100 < 20
          ? 2
          : ORDER[number % 10 < 5 ? number % 10 : 5];
      return DECLENSIONS[declension];
    },
  },
  components: {
    LineStep
  }
};
</script>

<style>
.v-slider__tick {
  position: relative;
}
.v-slider__tick::after {
  content: "";
  position: absolute;
  width: 200%;
  height: 200%;
  background: #fff;
  border: 3px solid #D41367;
  border-radius: 50%;
  transform: translate(-25%, -25%);
}
.v-slider__track-container {
  height: 4px !important;
}
.v-slider__thumb {
  width: 20px !important;
  height: 20px !important;
}
.v-slider__thumb::after {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  background: #ffffff;
  border: 4px solid #D41367;
  border-radius: 50%;
}
.v-slider__thumb::before {
  content: none !important;
}
.credit_section_title {
    color: black !important;
    font-family: Roboto;
}
.credit_section {
    font-family: Roboto;
}
.pay_text {
    font-size: 18px;
}
</style>