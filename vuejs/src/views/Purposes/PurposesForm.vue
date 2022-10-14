<template>
  <div class="purposes_block">
    <h4 class="form_block_label text-left">
      Сведения о целях установления деловых отношений с банком
    </h4>
    <div class="form_block">
      <v-checkbox
        v-model="ex4"
        label="Рассчетно-кассовое обслуживание"
        value="Рассчетно-кассовое обслуживание"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Дистанцинное обслуживание"
        value="Дистанцинное обслуживание"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Внешнеэкономическое обслуживание"
        value="Внешнеэкономическое обслуживание"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Интернет-экваринг"
        value="Интернет-экваринг"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Кредитование"
        value="Кредитование"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Торговый экваринг"
        value="Торговый экваринг"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Переводы СБП (c2b)"
        color="red"
        value="red"
        hide-details
      ></v-checkbox>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Количество операций по безлимитным платежам в месяц
      </p>
      <v-radio-group mandatory v-model="column" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">
        Сумма операций по снятию наличности в месяц
      </p>
      <v-radio-group mandatory v-model="column" column>
        <v-radio label="0 - 99 000 руб" value="0-99 000 руб"></v-radio>
        <v-radio
          label="100 000 - 1 000 000 руб"
          value="100 000 - 1 000 000 руб"
        ></v-radio>
        <v-radio
          label="более 1 000 000 руб"
          value="более 1 000 000 руб"
        ></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-5">
      <p class="form_block_title">
        Количество операций по внешнеторговым контрактам в месяц
      </p>
      <v-radio-group mandatory v-model="column" column>
        <v-radio label="0-29" value="0-29"></v-radio>
        <v-radio label="30-100" value="30-100"></v-radio>
        <v-radio label="более 100" value="более 100"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block mt-5">
      <p class="form_block_title">Источники происхождения денежных средств</p>
      <v-checkbox
        v-model="ex4"
        label="Средства, полученные в рамках осуществляемой хозяйственой деятельности"
        value="Средства, полученные в рамках осуществляемой хозяйственой деятельности"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Сообственные средства"
        value="Сооственные средства"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Заменные средства (займы от третих лиц, учредителей и т.д)"
        value="Заменные средства (займы от третих лиц, учредителей и т.д)"
        hide-details
      ></v-checkbox>
      <v-checkbox
        v-model="ex4"
        label="Иные"
        value="Иные"
        hide-details
      ></v-checkbox>
    </div>
    <div class="form_block mt-10">
      <p class="form_block_title">Штатная численость сотрудников</p>
      <v-radio-group mandatory v-model="column" column>
        <v-radio label="0 - 99 000 руб" value="0-99 000 руб"></v-radio>
        <v-radio
          label="100 000 - 1 000 000 руб"
          value="100 000 - 1 000 000 руб"
        ></v-radio>
        <v-radio
          label="более 1 000 000 руб"
          value="более 1 000 000 руб"
        ></v-radio>
      </v-radio-group>
    </div>
    <v-btn
      block
      large
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>