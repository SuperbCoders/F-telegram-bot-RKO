<template>
  <div class="rate_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <h2 class="text-left rate_section_title mb-10 w-60">
      Тарифы на расчетно-кассовое обслуживание
    </h2>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Первый</h2>
        <p class="text-left mb-3 card_content_text">
          Подойдёт тем, кто неавно зарегистрировал ИП или ООО и только начинает вести бизнес
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            Нет бесплатных платежей
          </li>
          <li class="text-left mb-3">
            49 ₽ за платеж
          </li>
          <li class="text-left mb-3">
            100 000 ₽ бесплатно для снятия наличных и переводов на ФЛ/Card 2 Card Далее 349 ₽ за каждые 50 000 ₽
          </li>
          <li class="text-left mb-3">
            59 ₽ минимальная плата в день за использование овердрафта
          </li>
          <li class="text-left mb-3">
            50 000 ₽ максимальный кэшбэк по бизнес-карте
          </li>
          <li class="text-left mb-3">
            0 ₽ за SMS-уведомления
          </li>
          <li class="text-left mb-3">
            0 ₽ за подключение эквайринга и сервисов для бизнеса
          </li>
        </ul>
        <h2 class="text-left rate_content_price mb-3">0 ₽/мес</h2>
        <v-btn class="rate_card_content_button-activate pink darken-1" v-if="currentData.tariff === 'Первый'"
          @click="unsetTarif()" large>
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn class="rate_card_content_button" v-else @click="setTarif('Первый')" large>Выбрать</v-btn>
      </div>
    </v-card>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Второй</h2>
        <p class="text-left mb-3 card_content_text">
          Оптимальный тариф для тех, чей бизнес начал приносить первую прибыль
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            5 платежей бесплатно
          </li>
          <li class="text-left mb-3">
            29 ₽ за платеж сверх лимита
          </li>
          <li class="text-left mb-3">
            200 000 ₽ бесплатно для снятия наличных и переводов на ФЛ/Card 2 Card Далее 349 ₽ за каждые 50 000 ₽
          </li>
          <li class="text-left mb-3">
            59 ₽ минимальная плата в день за использование овердрафта
          </li>
          <li class="text-left mb-3">
            50 000 ₽ максимальный кэшбэк по бизнес-карте
          </li>
          <li class="text-left mb-3">
            0 ₽ за SMS-уведомления
          </li>
          <li class="text-left mb-3">
            0 ₽ за подключение эквайринга и сервисов для бизнеса
          </li>
        </ul>
        <h2 class="text-left rate_content_price mb-3">490 ₽/мес</h2>
        <v-btn class="rate_card_content_button-activate pink darken-1" v-if="currentData.tariff === 'Второй'"
          @click="unsetTarif()" large>
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn class="rate_card_content_button" v-else @click="setTarif('Второй')" large>Выбрать</v-btn>
      </div>
    </v-card>
    <v-card class="mb-10 rate_card rounded-xl shadow-light-100">
      <div class="card_content p-10 text-left m-11">
        <h2 class="text-left mb-3 card_content_title">Третий</h2>
        <p class="text-left mb-3 card_content_text">
          Для активно растущего бизнеса, который выходит на новые рынки
        </p>
        <ul class="mb-3 rate_section_list">
          <li class="text-left mb-3">
            50 платежей бесплатно
          </li>
          <li class="text-left mb-3">
            19 ₽ за платеж сверх лимита 300 000 ₽ бесплатно для снятия наличных и переводов на ФЛ и Card/Card Далее 349
            ₽ за каждые 50 000 ₽
          </li>
          <li class="text-left mb-3">
            59 ₽ минимальная плата в день за использование овердрафта
          </li>
          <li class="text-left mb-3">
            50 000 ₽ максимальный кэшбэк по бизнес-карте
          </li>
          <li class="text-left mb-3">
            0 ₽ за SMS-уведомления
          </li>
          <li class="text-left mb-3">
            0 ₽ за подключение эквайринга и сервисов для бизнеса
          </li>
        </ul>
        <h2 gray class="text-left rate_content_price mb-3">1 490 ₽/мес</h2>
        <v-btn class="rate_card_content_button-activate pink darken-1" v-if="currentData.tariff === 'Третий'"
          @click="unsetTarif()" large>
          <span class="white--text"> Выбрано </span>

          <v-icon large color="white" class="ml-2" style="font-size: 20px">
            mdi-check
          </v-icon>
        </v-btn>
        <v-btn class="rate_card_content_button" v-else @click="setTarif('Третий')" large>Выбрать</v-btn>
      </div>
    </v-card>

    <div class="form_block">
      <h2 class="text-left">
        Выберите дополнительные продукты к подключению
      </h2>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="СМС-оповещение"
        value="СМС-оповещение" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Интернет-эквайринг"
        value="Интернет-эквайринг" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Торговый-эквайринг"
        value="Торговый-эквайринг" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Комьюнити" value="Комьюнити"
        hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Бухгалтерия" value="Бухгалтерия"
        hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Юридическая поддержка"
        value="Юридическая поддержка" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.additional_products" class="checkboxs" label="Продвижение" value="Продвижение"
        hide-details>
      </v-checkbox>
    </div>

    <LineStep :step="13" />
    <v-btn block large @click="redirect()" class="mt-10 auth_form_bth" color="primary">
      <span v-if="currentData.tariff">Продолжить</span>
      <span v-else>Пропустить</span>
    </v-btn>
  </div>
</template>

<script>
import LineStep from "@/components/line_step/line_step.vue";
import { loadCurrentData } from '@/utils/loadStore'

export default {
  components: {
    LineStep,
  },
  data() {
    return {
      currentData: {
        tariff: null,
        additional_products: [],
      },
    };
  },
  mounted() {
    scroll(0, 0);
    loadCurrentData({
      currentData: this.currentData,
      step: 'step_13',
      vue: this,
    });
  },
  methods: {
    setTarif(tarif) {
      this.currentData.tariff = tarif;
    },
    unsetTarif() {
      this.currentData.tariff = null;
    },
    redirect() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_13',
        value: this.currentData
      })
      this.next();
    },
    next() {
      this.$router.push({ name: "step_14" });
    },
    back() {
      this.$router.push({ name: "step_12" });
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

.rate_section_list>li {
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