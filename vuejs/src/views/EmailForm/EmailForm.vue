<template>
  <div class="email_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Почтовый адрес</p>
        <v-radio-group v-model="isAddress" mandatory>
          <v-radio
            label="Совпадает с адресом регистации"
            value="Совпадает с адресом регистации"
          ></v-radio>
          <v-radio
            label="Совпадает с адресом проживания"
            value="Совпадает с адресом проживания"
          ></v-radio>
          <v-radio
            label="Не совпадает с адресом регистации и адресом проживания"
            value="Не совпадает с адресом регистации и адресом проживания"
          ></v-radio>
        </v-radio-group>
        <div v-if="isAddress === 'Не совпадает с адресом регистации и адресом проживания'">
          <p class="form_block_title">Адрес фактического проживания</p>
          <v-text-field
            id="oldName"
            placeholder="Введите адрес"
            v-model="address"
            class="align-center border-none mt-5"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
      </div>
    </v-form>
    <line-step :step='8' class="mt-5" />
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
import LineStep from '../../components/line_step/line_step.vue';
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
        this.$store.commit('IsFormData')
        if (this.isAddress === 'Совпадает с адресом регистации') {
          this.currentData.account_own_mail = this.$store.state.result.account_own_registration
        } else if (this.isAddress === 'Совпадает с адресом проживания') {
          this.currentData.account_own_mail = this.$store.state.result.accownt_own_living
        } else if (this.isAddress === 'Не совпадает с адресом регистации и адресом проживания') {
          this.currentData.account_own_mail = this.address
        }
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/document");
      }
    },
  },
  components: {
    LineStep,
  },
  computed: {
    isTest () {
      return this.$store.state.account_own_registration
    }
  }
};
</script>

<style>
</style>