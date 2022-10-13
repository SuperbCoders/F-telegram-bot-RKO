<template>
  <div class="credit_section">
    <p class="credit_section_title blue-grey--text">
      <span>Сумма кредите:</span>
      <span class="primary--text"
        >
     {{ getFormattedCurrency(formData["loanAmount"]) }} &#8381;</span
      >
    </p>
    <v-slider
      :max="5000000"
      :min="1000000"
      v-model="formData['loanAmount']"
      step="500000"
      track-color="light-grey"
      tick-size="5"
      ticks="always"
      track-fill-color="primary"
    ></v-slider>
    <p class="title blue-grey--text">
      Срок:
      <span class="primary--text">
        {{ formData["loanTerm"] }}
        {{ getFormattedYearNoun(formData["loanTerm"]) }}
      </span>
    </p>
    <v-slider
      class="d-none d-sm-block"
      :tick-labels="loanTermTickLabels"
      :max="7"
      :min="2"
      step="1"
      v-model="formData['loanTerm']"
      ticks
      track-color="light-grey"
      tick-size="5"
      track-fill-color="primary"
    ></v-slider>
    <v-slider
      class="d-sm-none"
      :tick-labels="smallLoanTermTickLabels"
      :max="7"
      :min="2"
      step="1"
      ticks
      track-color="light-grey"
      tick-size="5"
      track-fill-color="primary"
    ></v-slider>
    <p class="mt-5 title grey--text">Ежемесячный платеж</p>
    <v-scroll-y-transition hide-on-leave>
      <p :key="monthlyPayment" class="display-1 primary--text">
        {{ getFormattedCurrency(monthlyPayment) }} &#8381;
      </p>
    </v-scroll-y-transition>
    <p class="grey--text">
      Сумма переплаты:
      <span class="black--text"
        >{{ getFormattedCurrency(interestAmount) }} &#8381;</span
      >
    </p>
    <p class="grey--text">
      Сумма кредита:
      <span class="black--text"
        >{{ getFormattedCurrency(totalLoanAmount) }} &#8381;</span
      >
    </p>
    <p class="grey--text">
      Процентная ставка:
      <span class="black--text">{{ interestRate * 100 }}%</span>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {},
      loanTermTickLabels: [
      "2 года",
      "3 года",
      "4 года",
      "5 лет",
      "6 лет",
    ],
    smallLoanTermTickLabels: ["2 года", "", "4 года", "", "6 лет"],
    };
  },
  methods: {
    getFormattedCurrency: function (number) {
      if (number) {
        return parseFloat(number).toLocaleString("ru-RU");
      }
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
};
</script>

<style>
</style>