<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold">Структура органов управления</h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Выберите из списка</p>
        <v-combobox
          v-model="currentData.supreme_management_body"
          filled
          :rules="requiredRules"
          required
          :items="isLeaderList"
          outlined
          placeholder="Выберите из списка"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Руководитель</p>
        <v-combobox 
          filled 
          v-model="currentData.supreme_management_type" 
          :items="isLeaderType" outlined 
          :rules="requiredRules" 
          placeholder="Тип"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <v-text-field
          id="oldName"
          v-model="currentData.supreme_management_inn"
          placeholder="Введите ИНН или название компании"
          class="align-center border-none"
          name="oldName"
          outlined
          type="number"
          :rules="innRules"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left mb-2 form_block_label">
          Наличие наблюдательного совета
        </p>
        <RadioGroup @isStatus="(status) => (isTest1 = status)" name="Existence of a supervisory board" />
      </div>
      <div v-if="isTest1" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименования наблюдательного совета
        </p>
        <v-text-field
          id="oldName"
          placeholder="Наименования"
          class="align-center border-none"
          name="oldName"
          v-model="currentData.collegiate_body"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left form_block_label mb-2 mt-5">

          Наличие коллегиального исполнительного органа
        </p>
        <RadioGroup @isStatus="(status) => isTest2 = status" name="The presence of a collegial executive body" />
      </div>
      <div v-if="isTest2" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименование коллегиального исполнительног органа
        </p>
        <v-text-field
          id="oldName"
          placeholder="Наименование"
          class="align-center border-none"
          name="oldName"
          outlined
          v-model="currentData.collegiate_person"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block mt-5">
        <p class="text-left form_block_title">
          Члены коллегиального исполнительного органа
        </p>
        <v-text-field
          id="oldName"
          placeholder="Укажите Физ лицо"
          v-model="currentData.collegiate_person_fio"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
    </v-form>
    <line-step :step='2' />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить</v-btn
    >
  </div>
</template>
<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";
import LineStep from '../../components/line_step/line_step.vue';

export default {
  data: () => ({
    valid: true,
    currentData: {
      supreme_management_body: null,
      supreme_management_type: null,
      supreme_management_inn: null,
      collegiate_body: null,
      collegiate_person: null,
      collegiate_person_fio: null,
    },
    isTest1: true,
    isTest2: true,
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
      (v) =>
        (v && v.length <= 12) || "ИНН не может содержать больше 12 симоволов",
    ],
    requiredRules: [(v) => !!v || "Это поле обязательно"]
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/individual-info");
      }
    },
  },
  computed: {
    isLeaderList () {
      return this.$store.getters.isList
    },
    isLeaderType () {
      return this.$store.getters.isLeaderType
    }
  },
  components: {
    RadioGroup,
    LineStep
  },
};
</script>

<style>
.form_block {
  font-family: Roboto;
  font-size: 14px;
}
.form_block_title {
  font-size: 12px;
  width: 200px;
}
.form_block_label {
  font-family: Roboto;
  color: black;
}
.auth_form_bth {
  border-radius: 10px;
  color: white !important;
  text-transform: capitalize;
  font-size: 14px;
}
</style>