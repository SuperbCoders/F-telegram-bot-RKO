<template>
  <div class="document_form_block">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block mt-5">
        <p class="text-left form_block_title">ИНН</p>

        <v-text-field id="oldName" 
          v-model="currentData.account_onw_inn"
          v-mask="'### ### ### ###'"
          masked="true"
          placeholder="Введите ИНН" class="align-center border-none" outlined
          :rules="innRules" :required="true">

        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">СНИЛС (при наличии)</p>
        <v-text-field id="oldName" 
        v-mask="'### ### ### ##'"
        masked="true"
        v-model="currentData.account_own_snils" placeholder="СНИЛС" class="align-center border-none" outlined

         :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Гражданство</p>

        <v-text-field id="oldName" placeholder="Гражданство" class="align-center border-none" outlined
          :rules="requiredRules" v-model="currentData.account_own_citizenship" :required="true">

        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Телефон</p>

        <v-text-field id="oldName" placeholder="Телефон" v-mask="'+# (###) ### ## ##'"
          masked="true" class="align-center border-none" outlined
          :rules="requiredRules" v-model="currentData.account_own_phone" :required="true">

        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Доля владения</p>
        <v-text-field id="oldName" placeholder="Доля владения" class="align-center border-none" outlined
          :rules="requiredRules" v-model="currentData.account_own_piece" :required="true">
        </v-text-field>
      </div>
      <line-step :step='4' />
      <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
import { mask } from "vue-the-mask";
export default {
  directives: { mask },
  data() {
    return {
      valid: true,
      currentData: {
        account_onw_inn: null,
        account_own_snils: null,
        account_own_citizenship: null,
        account_own_phone: null,
        account_own_piece: null
      },
      requiredRules: [(v) => !!v || "Это поле обязательно"],
      innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
      (v) =>
        (v && v.length <= 12) || "ИНН не может содержать больше 12 симоволов",
    ],
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/foreign-person");
      }
    },
  },
  components: {
    LineStep
  },
}
</script>

<style>

</style>