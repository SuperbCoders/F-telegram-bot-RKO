<template>
  <div class="individuals_form">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <v-form ref="form" v-model="valid" lazy-validation>
      <p class="text-left form_block_title"><span class="star">*</span>Роль лица</p>
      <div class="checkboxs">
        <v-checkbox v-model="currentData.account_onw_role" label="Акционер/учредитель" value="Акционер/учредитель"
          hide-details>
        </v-checkbox>
        <v-checkbox v-model="currentData.account_onw_role" label="ЕИО" value="ЕИО" hide-details>
        </v-checkbox>
        <v-checkbox v-model="currentData.account_onw_role" label="Бенифициар" value="Бенифициар" hide-details>
        </v-checkbox>
      </div>

      <p v-if="!valid && currentData.account_onw_role.length < 1" class="error_message">
        Выберите пункт
      </p>
      <div class="form_block mt-5">
        <p class="text-left form_block_title"><span class="star">*</span>Фамилия</p>
        <v-text-field id="oldName" v-model="currentData.account_own_lastname" placeholder="Введите Фамилию"
          class="align-center border-none" outlined :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Имя</p>
        <v-text-field id="oldName" v-model="currentData.account_own_name" placeholder="Введите Имя"
          class="align-center border-none" outlined :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Отчество</p>
        <v-text-field id="oldName" v-model="currentData.account_own_surname" placeholder="Введите Отчество"
          class="align-center border-none" outlined :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <v-radio-group v-model="currentData.account_own_gender" mandatory :required="true" class="checkboxs">
        <p class="text-left form_block_title"><span class="star">*</span>Пол</p>
        <v-radio label="Мужской" value="Мужской"></v-radio>
        <v-radio label="Женский" value="Женский"> </v-radio>
      </v-radio-group>
    </v-form>

    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import { loadSubCurrentData } from '@/utils/loadStore'

export default {
  data: () => ({
    valid: true,
    listRole: [],
    currentData: {
      account_onw_role: [],
      account_own_lastname: null,
      account_own_gender: null,
      account_own_name: null,
      account_own_surname: null,
    },
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("setPersone", { key: "substep_1", value: this.currentData, index: this.$route.params?.id });

        this.$router.push({
          name: "substep_2", params: {
            id: this.$route.params.id
          }
        });
      }
    },
    back() {
      this.$router.push({ name: "step_4" });
    },
  },
  mounted() {
    this.$store.commit("setPersone", { key: "substep_0", value: {}, index: this.$route.params?.id });
    loadSubCurrentData({
      currentData: this.currentData,
      substep: "substep_1",
      vue: this,
      index: this.$route.params.id
    })
  },
  components: {
  },
};
</script>

<style scoped>
.error_message {
  color: red;
  font-family: Roboto;
  margin-left: 10px;
  margin-top: 10px;
  font-size: 12px !important;
}

.checkboxs label {
  color: #323E48 !important;
}
</style>