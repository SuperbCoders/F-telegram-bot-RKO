<template>
  <div class="address_form_block">
    <v-form ref="form" v-model="valid" lazy-validation>
    <div class="form_block">
      <p class="text-left form_block_title">Адрес фактического проживания</p>
      <v-radio-group v-model="isAddress" mandatory>
        <v-radio label="Совпадает с адресом регистации" value="true"></v-radio>
        <v-radio label="Не совпадает с адресом регистации" value="false"></v-radio>
      </v-radio-group>
      <p class="form_block_title">
        Адрес фактического проживания
      </p>
      <v-text-field id="oldName" v-if="isAddress === 'false'" placeholder="Введите адрес" class="align-center border-none mt-5"
        :rules="requiredRules" outlined :required="true"></v-text-field>
    </div>
    </v-form>
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAddress: false,
      valid: false,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$router.push("/email-form");
      }
    },
  },
}
</script>

<style>

</style>