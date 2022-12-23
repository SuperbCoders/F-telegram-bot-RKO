<template>
  <div class="status_kinship_block">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">

        <div class="form_block">
          <p class="text-left form_block_title">Адрес регистрации</p>
          <AddressInput label="Введите адрес" v-model="currentData.assigned_publ_pers_registraion" />
        </div>
      </div>
    </v-form>
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
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
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("setPersone", { key: "substep_3", value: this.currentData, index: this.$route.params?.id });

        this.$router.push({ name: "substep_4", params: {id: this.$route.params.id} });


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