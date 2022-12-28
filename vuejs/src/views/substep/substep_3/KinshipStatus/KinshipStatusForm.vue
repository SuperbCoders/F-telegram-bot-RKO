<template>
  <div class="status_kinship_block">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">

        <div class="form_block">
          <p class="text-left form_block_title">Адрес регистрации</p>
          <AddressInput label="Введите адрес" :index="5" v-model="currentData.assigned_publ_pers_registraion" />
        </div>
      </div>
    </v-form>
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import AddressInput from '@/components/addressInput.vue';
import { loadSubCurrentData } from '@/utils/loadStore'

export default {
  data: () => ({
    valid: true,
    currentData: {
      assigned_publ_pers_registraion: "",
    },
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  mounted() {
    loadSubCurrentData({
      currentData: this.currentData,
      substep: "substep_3",
      vue: this,
      index: this.$route.params.id
    })
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("setPersone", { key: "substep_3", value: this.currentData, index: this.$route.params?.id });
        this.$router.push({ name: "substep_4", params: { id: this.$route.params.id } });
      }
    },
    back() {
      this.$router.push({ name: "substep_2", params: { id: this.$route.params.id } });
    },
  },
  components: {
    AddressInput,
  }
};
</script>

<style>

</style>