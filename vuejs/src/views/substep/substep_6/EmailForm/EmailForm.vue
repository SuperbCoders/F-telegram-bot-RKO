<template>
  <div class="email_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Почтовый адрес</p>
        <v-radio-group v-model="isAddress" mandatory class="checkboxs">
          <v-radio label="Совпадает с адресом регистрации" value="Совпадает с адресом регистрации"></v-radio>
          <v-radio label="Совпадает с адресом проживания" value="Совпадает с адресом проживания"></v-radio>
          <v-radio label="Не совпадает с адресом регистрации и адресом проживания"
            value="Не совпадает с адресом регистрации и адресом проживания"></v-radio>
        </v-radio-group>
        <div v-if="isAddress === 'Не совпадает с адресом регистрации и адресом проживания'">
          <p class="form_block_title">
            <span class="star">*</span>
            Адрес фактического проживания
          </p>
          <AddressInput label="Введите адрес" v-model="currentData.account_own_mail" />
        </div>
      </div>
    </v-form>
    <v-btn block large class="mt-3 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import AddressInput from '@/components/addressInput.vue';

export default {
  data() {
    return {
      isAddress: false,
      address: '',
      currentData: {
        account_own_mail: null
      },
      valid: false,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        if (this.isAddress === 'Совпадает с адресом регистрации') {
          this.currentData.account_own_mail = "Совпадает с адресом регистрации"
        } else if (this.isAddress === 'Совпадает с адресом проживания') {
          this.currentData.account_own_mail = "Совпадает с адресом проживания"
        } else if (this.isAddress === 'Не совпадает с адресом регистрации и адресом проживания') {
          this.currentData.account_own_mail = this.address
        }

        this.$store.commit("setPersone", { key: "substep_6", value: this.currentData });
        

        this.$router.push({ name: "substep_7", query: this.$route.query });
      }
    },
  },
  components: {
    AddressInput,
  },
  computed: {
    isTest() {
      return this.$store.state.account_own_registration
    }
  }
};
</script>

<style>

</style>