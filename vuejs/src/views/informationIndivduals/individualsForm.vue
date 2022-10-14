<template>
  <div class="individuals_form">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">

      </div>
      <p class="text-left form_block_title">Роль лица</p>
      <v-checkbox label="Руководитель" v-model="currentData.listRole" value="Руководитель" hide-details>
      </v-checkbox>
      <v-checkbox label="Учредитель" value="red" hide-details></v-checkbox>
      <v-checkbox v-model="currentData.listRole" label="Бенефированый владелец" value="Бенефированый владелец" hide-details>
      </v-checkbox>
      <v-checkbox v-model="currentData.listRole" label="Подписант" value="red" hide-details></v-checkbox>
      <p v-if="!valid && currentData.listRole.length < 1" class="error_message">Выберите пункт</p>
      <div class="form_block mt-5">
        <p class="text-left form_block_title">Фамилия</p>
        <v-text-field id="oldName" v-model="currentData.surname" placeholder="Введите фамилию" class="align-center border-none" outlined
          :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Имя</p>
        <v-text-field id="oldName" v-model="currentData.lastname" placeholder="Введите имя" class="align-center border-none" outlined
          :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Отчество (при наличии)</p>
        <v-text-field id="oldName" v-model="currentData.patronymic" placeholder="Напишите адрес" class="align-center border-none" outlined
         :required="true"></v-text-field>
      </div>
      <v-radio-group v-model="currentData.gender" mandatory>
        <v-radio  label="Мужской" value="Мужской"></v-radio>
        <v-radio  label="Женский" value="Женский">
        </v-radio>
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
      listRole: [],
      surname: null,
      gender: null,
      lastname: null,
      patronymic: null,
    },
    dateStarting: null,
    dateEnd: null,
    test: [],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/documents-forms");
      }
    },
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
</style>