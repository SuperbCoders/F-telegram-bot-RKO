<template>
  <div class="rate_section">
    <h2 class="text-left rate_section_title mb-10 w-60">
      Тарифы на расчетно-кассовое обслуживание
    </h2>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Тариф 1</h2>
        <p class="text-left mb-3 card_content_text">
          Для начинающих предпринимателей
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
        </ul>
        <h2 class="text-left rate_content_price mb-3">490 руб/мес</h2>
        <v-btn
          class="rate_card_content_button-activate pink darken-1"
          v-if="currentData.tariff === 'Тариф 1'"
          @click="unsetTarif()"
          large
        >
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn
          class="rate_card_content_button"
          v-else
          @click="setTarif('Тариф 1')"
          large
          >Выбрать</v-btn
        >
      </div>
    </v-card>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Тариф 2</h2>
        <p class="text-left mb-3 card_content_text">
          Для начинающих предпринимателей 
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
        </ul>
        <h2 class="text-left rate_content_price mb-3">490 руб/мес</h2>
        <v-btn
          class="rate_card_content_button-activate pink darken-1"
          v-if="currentData.tariff === 'Тариф 2'"
          @click="unsetTarif()"
          large
        >
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn
          class="rate_card_content_button"
          v-else
          @click="setTarif('Тариф 2')"
          large
          >Выбрать</v-btn
        >
      </div>
    </v-card>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Тариф 3</h2>
        <p class="text-left mb-3 card_content_text">
          Для начинающих предпринимателей
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
          <li class="text-left mb-3">
            До 400 000 ₽ себе на счет для ИП бесплатно
          </li>
        </ul>
        <h2 gray class="text-left rate_content_price mb-3">490 руб/мес</h2>
        <v-btn
          class="rate_card_content_button-activate pink darken-1"
          v-if="currentData.tariff === 'Тариф 3'"
          @click="unsetTarif()"
          large
        >
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn
          class="rate_card_content_button"
          v-else
          @click="setTarif('Тариф 3')"
          large
          >Выбрать</v-btn
        >
      </div>
    </v-card>
    <LineStep :step="9" />
    <v-btn
      block
      large
      :disabled="!currentData.tariff"
      @click="redirect()"
      class="mt-10 auth_form_bth"
      color="primary"
    >
      Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "../../components/line_step/line_step.vue";
export default {
  components: {
    LineStep,
  },
  data() {
    return {
      currentData: {
        tariff: null,
      },
    };
  },
  mounted(){
    scroll(0, 0);
  },
  methods: {
    setTarif(tarif) {
      this.currentData.tariff = tarif;
      // const data = this.$store.state.formData
    },
    unsetTarif() {
      this.currentData.tariff = null;
    },
    redirect() {
      this.$store.dispatch('addObjectFormData', {
          object: 'step_11',
          value: this.currentData
        })
      this.$router.push("/all-data");
    },
  },
};
</script>

<style>
.card_content {
  padding: 20px;
  font-family: Roboto;
}

.rate_section_title {
  width: 80%;
  font-family: Geometria;
  color: #0c0c0d;
}

.rate_card {
  box-shadow: 0 0 10px 2px rgba(0, 0, 0, 0.11) !important;
}

.rate_card_content_button {
  width: 150px !important;
  cursor: pointer;
  box-shadow: 0 0 4px #00000030;
  background: #f3f4f4 !important;
  border-radius: 6px;
  text-transform: none !important;
  margin-top: 20px;
  font-family: Roboto;
  font-size: 14px !important;
  color: #5b656d !important;
  font-weight: 500;
  padding: 16px 30px !important;
  text-transform: none;
}
.rate_card_content_button-activate {
  width: 150px !important;
  cursor: pointer;
  box-shadow: 0 0 4px #00000010;
  border-radius: 6px;
  text-transform: none !important;
  margin-top: 20px;
  font-family: Roboto;
  font-size: 14px !important;
  font-weight: 400;
  padding: 16px 30px !important;
  text-transform: none;
}

.rate_section_list > li {
  font-size: 14px;
  color: #757f86 !important;
}

.rate_content_price {
  font-weight: 400;
  color: #323e48;
}

.card_content_text {
  font-size: 12px;
  font-weight: 400;
  color: #323e48;
}

.card_content_title {
  letter-spacing: 0.6px;
  line-height: 28px;
  color: #323e48;
}
</style>