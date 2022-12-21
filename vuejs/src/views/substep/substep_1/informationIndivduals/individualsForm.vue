<template>
  <div class="individuals_form">
    <v-form ref="form" v-model="valid" lazy-validation>
      <p class="text-left form_block_title"><span class="star">*</span>Роль лица</p>
      <div class="checkboxs">
        <v-checkbox label="Руководитель" v-model="currentData.account_onw_role" value="Руководитель" hide-details>
        </v-checkbox>
        <v-checkbox v-model="currentData.account_onw_role" label="Учредитель" value="Учредитель" hide-details>
        </v-checkbox>
        <v-checkbox v-model="currentData.account_onw_role" label="Бенефициарный владелец" value="Бенефициарный владелец"
          hide-details>
        </v-checkbox>
        <v-checkbox v-model="currentData.account_onw_role" label="Подписант" value="Подписант" hide-details>
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
        <p class="text-left form_block_title">Отчество (при наличии)</p>
        <v-text-field id="oldName" v-model="currentData.account_own_surname" placeholder="Введите Отчество"
          class="align-center border-none" outlined></v-text-field>
      </div>
      <v-radio-group v-model="currentData.account_own_gender" mandatory class="checkboxs">
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
        this.$store.commit("setPersone", { key: "substep_1", value: this.currentData });

        this.$router.push({ name: "substep_2" });
      }
    },
  },
  mounted() {
    this.$store.commit("setPersone", { key: "substep_0", value: {} });

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