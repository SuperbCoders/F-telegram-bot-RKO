<template>
  <div class="address_form_block">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Адрес фактического проживания</p>
        <v-radio-group v-model="data" mandatory>
          <v-radio label="Совпадает с адресом регистации" value="Да"></v-radio>
          <v-radio label="Не совпадает с адресом регистации" value="Нет"></v-radio>
        </v-radio-group>
        <div v-if="data === 'Нет'">
          <p class="form_block_title">
            Адрес фактического проживания
          </p>
          <v-combobox label="Введите адрес" outlined v-model="currentData.accownt_own_living" :rules="requiredRules"
            required class="mt-1 auth_form combobox mt-5" @keyup="getAddressFromName" :items="listAddres"></v-combobox>
        </div>
      </div>
    </v-form>
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import { getAddress } from '../../api/GetAddress';

export default {
  data() {
    return {
      valid: false,
      data: 'Да',
      isAdress: null,
      currentData: {
        accownt_own_living: null
      },
      listAddres: [],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        if (this.data === 'Нет') {
          this.currentData.accownt_own_living = this.isAdress
        } else {
          this.currentData.accownt_own_living = 'Совпадает'
        }

        if (this.$route.query?.type === 'SupervisoryBoard') {
          this.$store.commit("setSupervisoryBoardPersone", { key: "page-5", value: this.currentData });
        } else if (this.$route.query?.type === 'CollegialExecutive') {
          this.$store.commit("setCollegialExecutiveBody", { key: "page-5", value: this.currentData });
        }
        this.$router.push({ path: "/email-form", query: this.$route.query });
      }
    },
    async getAddressFromName(e) {
      const value = e.target.value;
      const data = await getAddress(value);
      this.listAddres = data.suggestions.map((elem) => `${elem.value}, ${elem.data?.address?.unrestricted_value}`);
    },
  },
  computed: {
    isFormdata() {
      return this.$store.state.formData.account_own_registration
    }
  }
}
</script>

<style>

</style>