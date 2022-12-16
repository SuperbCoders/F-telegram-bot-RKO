<template>
  <div class="status_kinship_block">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_label">
          Степень родства либо статус (супруг или супруга) по отношению к
          публичному должностному лицу
        </p>
        <p class="text-left form_block_title">Степень родства</p>
        <v-combobox
          :items="relationDegree"
          v-model="currentData.assigned_publ_pers_relation"
          :rules="requiredRules"
          required
          outlined
          placeholder="Степень родства"
        ></v-combobox>
        <div class="form_block">
          <p class="text-left form_block_title">Адрес регистрации</p>
          <AddressInput label="Введите адрес" v-model="currentData.assigned_publ_pers_registraion" />
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">Адрес регистрации</p>
          <AddressInput label="Введите адрес" v-model="currentData.account_own_registration" />
        </div>
      </div>
    </v-form>
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import AddressInput from '@/components/addressInput.vue';

export default {
  data: () => ({
    valid: true,
    currentData: {
      assigned_publ_pers_relation: null,
      assigned_publ_pers_registraion: null,
      account_own_registration: null,
    },
    relationDegree: ["Супруг", "Супруга"],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {

        this.$store.commit('updateAssigned_publ_pers_registraion', this.currentData.assigned_publ_pers_registraion)

        if(this.$route.query?.type === 'SupervisoryBoard') {
          this.$store.commit("setSupervisoryBoardPersone", {key: "page-4", value: this.currentData});
        }else if(this.$route.query?.type === 'CollegialExecutive') {
          this.$store.commit("setCollegialExecutiveBody", {key: "page-4", value: this.currentData});
        }
        
        this.$router.push({name:"substep_5", query: this.$route.query});


      }
    },
  },
  components: {
    AddressInput,
  }
};
</script>

<style>
</style>