<template>
  <div class="individuals_form">
    <v-checkbox
      label="Руководитель"
      color="red"
      value="red"
      hide-details
    ></v-checkbox>
    <v-checkbox
      label="Учредитель"
      color="red"
      value="red"
      hide-details
    ></v-checkbox>
    <v-checkbox
      label="Бенефированый владелец"
      color="red"
      value="red"
      hide-details
    ></v-checkbox>
    <v-checkbox
      label="Подписант"
      color="red"
      value="red"
      hide-details
    ></v-checkbox>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="Напишите адрес"
        class="align-center border-none"
        outlined
        :rules="requiredRules"
        :required="true"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
    data: () => ({
    valid: true,
    dateStarting: null,
    dateEnd: null,
    passportIssueDateMenu: null,
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
};
</script>

<style>
</style>