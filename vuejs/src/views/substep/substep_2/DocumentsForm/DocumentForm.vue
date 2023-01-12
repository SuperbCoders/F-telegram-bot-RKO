<template>
  <div class="document_form_block">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>

      <div class="form_block" v-if="is_eio">
        <p class="text-left form_block_title"><span class="star">*</span>Должность</p>

        <v-text-field id="oldName" placeholder="Должность" class="align-center border-none" outlined
          :rules="requiredRules" v-model="currentData.account_own_job_title" :required="true">

        </v-text-field>
      </div>

      <div class="form_block mt-5">
        <p class="text-left form_block_title"><span class="star">*</span>ИНН</p>

        <v-text-field id="oldName" v-model="currentData.account_onw_inn" v-mask="'### ### ### ###'" masked="true"
          placeholder="Введите ИНН" class="align-center border-none" outlined :rules="innRules">

        </v-text-field>
      </div>

      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Гражданство</p>
        <v-combobox outlined required class="mt-1 auth_form combobox" @keyup="inputCountry"
          v-model="currentData.account_own_citizenship" :items="itemsCountry">
        </v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Страна проживания</p>
        <v-combobox outlined required class="mt-1 auth_form combobox" @keyup="inputCountry2"
          v-model="currentData.account_country_residence" :items="itemsCountry2">
        </v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Телефон</p>

        <v-text-field id="oldName" placeholder="Телефон" v-mask="'+# (###) ### ## ##'" masked="true"
          class="align-center border-none" outlined :rules="requiredRules" v-model="currentData.account_own_phone"
          :required="true">

        </v-text-field>
      </div>

      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Эл. почта</p>

        <v-text-field id="oldName" type="email" placeholder="Эл. почта" class="align-center border-none" outlined
          :rules="emailRules" v-model="currentData.account_own_email" :required="true">

        </v-text-field>
      </div>

      <div class="form_block" v-if="is_auctioner">
        <p class="text-left form_block_title"><span class="star">*</span>Доля владения Акционер/учредитель</p>
        <v-text-field id="oldName" placeholder="Доля владения Акционер/учредитель" class="align-center border-none"
          outlined :rules="requiredRules" v-model="currentData.account_own_piece_auctioner" :required="true">
        </v-text-field>
      </div>
      <div class="form_block" v-if="is_beneficiary">
        <p class="text-left form_block_title"><span class="star">*</span>Доля владения Бенифициар</p>
        <v-text-field id="oldName" placeholder="Доля владения Бенифициар" class="align-center border-none" outlined
          :rules="requiredRules" v-model="currentData.account_own_piece_beneficiary" :required="true">
        </v-text-field>
      </div>
      <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import { mask } from "vue-the-mask";
import { getCountry } from '@/api/getCountry'
import { loadSubCurrentData } from '@/utils/loadStore'

export default {
  directives: { mask },
  data() {
    return {
      valid: true,
      currentData: {
        account_own_job_title: "",
        account_onw_inn: "",
        account_own_citizenship: "Россия",
        account_own_phone: "",
        account_own_piece_auctioner: "",
        account_own_piece_beneficiary: "",
        account_own_email: "",
        account_country_residence: "",
      },
      itemsCountry: [
        "Россия",
      ],
      itemsCountry2: [
        "Россия",
      ],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
      innRules: [
        (v) =>
          ((v && v.length >= 15) || !v || v.length == 0) || "ИНН не может содержать меньше 12 симоволов",
      ],
      emailRules: [(v) => /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.exec(v) !== null || "В это поле нужно написать Email"],
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("setPersone", { key: "substep_2", value: this.currentData, index: this.$route.params?.id });

        this.$router.push({ name: "substep_3", params: { id: this.$route.params.id } });
      }
    },
    back() {
      this.$router.push({ name: "substep_1", params: { id: this.$route.params.id } });
    },
    async inputCountry(event) {
      const countryes = await getCountry(event.target.value);

      this.itemsCountry = countryes?.suggestions?.map((val) => {
        return val.value;
      });
    },
    async inputCountry2(event) {
      const countryes = await getCountry(event.target.value);

      this.itemsCountry2 = countryes?.suggestions?.map((val) => {
        return val.value;
      });
    },
  },
  async mounted() {
    loadSubCurrentData({
      currentData: this.currentData,
      substep: "substep_2",
      vue: this,
      index: this.$route.params.id,
    })
  },
  computed: {
    is_auctioner() {
      const index = this.$route.params.id;
      return this.$store.state.formData.step_4.list_persone[index].substep_1.account_onw_role.indexOf("Акционер/учредитель") >= 0;
    },
    is_eio() {
      const index = this.$route.params.id;
      return this.$store.state.formData.step_4.list_persone[index].substep_1.account_onw_role.indexOf("ЕИО") >= 0;
    },
    is_beneficiary() {
      const index = this.$route.params.id;
      return this.$store.state.formData.step_4.list_persone[index].substep_1.account_onw_role.indexOf("Бенифициар") >= 0;
    }
  },
}
</script>

<style>
.combobox .v-input__icon {
  display: none !important;
}
.theme--light.v-list-item.v-list-item--highlighted::before {
  opacity: 0 !important;
}
</style>