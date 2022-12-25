<template>
  <div class="address_form_block">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Адрес фактического проживания</p>
        <v-radio-group v-model="currentData.is_accownt_own_living" mandatory class="checkboxs">
          <v-radio label="Совпадает с адресом регистрации" value="Да"></v-radio>
          <v-radio label="Не совпадает с адресом регистрации" value="Нет"></v-radio>
        </v-radio-group>
        <div v-if="currentData.is_accownt_own_living === 'Нет'">
          <p class="form_block_title">
            <span class="star">*</span>
            Адрес фактического проживания
          </p>
          <AddressInput label="Введите адрес" v-model="currentData.accownt_own_living" />
        </div>
      </div>
    </v-form>
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import AddressInput from '@/components/addressInput.vue';
import { loadSubCurrentData } from '@/utils/loadStore'

export default {
  data() {
    return {
      valid: false,
      data: 'Да',
      isAdress: null,
      currentData: {
        is_accownt_own_living: 'Да',
        accownt_own_living: null
      },
      listAddres: [],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    }
  },
  mounted() {
    loadSubCurrentData({
      currentData: this.currentData,
      substep: "substep_4",
      vue: this,
      index: this.$route.params.id
    })
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        // TODO нужно заменить на сами адреса
        if (this.data === 'Нет') {
          this.currentData.accownt_own_living = this.isAdress
        } else {
          const indexPage = this.$route.params.id;
          const address = this.$store.state.formData.step_4.list_persone[indexPage].substep_3.assigned_publ_pers_registraion;
          this.currentData.accownt_own_living = address  // Тут должен быть адрес
        }
        this.$store.commit("setPersone", { key: "substep_4", value: this.currentData, index: this.$route.params?.id });

        this.$router.push({ name: "substep_5", params: { id: this.$route.params.id } });
      }
    },
    back() {
      this.$router.push({ name: "substep_3", params: { id: this.$route.params.id } });
    },
  },
  computed: {
    isFormdata() {
      return this.$store.state.formData.account_own_registration
    }
  },
  components: {
    AddressInput,
  }
}
</script>

<style>

</style>