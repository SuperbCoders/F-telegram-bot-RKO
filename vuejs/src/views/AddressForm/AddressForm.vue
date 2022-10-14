<template>
  <div class="address_form_block">
    <div class="form_block">
      <p class="text-left form_block_title">Адрес фактического проживания</p>
      <v-radio-group v-model="isAddress" mandatory>
        <v-radio label="Совпадает с адресом регистации" value="true"></v-radio>
        <v-radio label="Не совпадает с адресом регистации" value="false"></v-radio>
      </v-radio-group>
      <p class="form_block_title">
        Адрес фактического проживания
      </p>
      <v-text-field id="oldName" v-if="isAddress" placeholder="Введите адрес" class="align-center border-none mt-5"
        outlined :required="true"></v-text-field>
    </div>
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAddress: false
    }
  }
}
</script>

<style>

</style>