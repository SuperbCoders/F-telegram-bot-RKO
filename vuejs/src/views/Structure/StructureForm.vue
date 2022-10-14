<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold">Структура органов управления</h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title">Выберите из списка</p>
        <v-combobox
          v-model="currentData.leaderList"
          filled
          :rules="requiredRules"
          required
          :items="isLeaderList"
          outlined
          placeholder="Выберите из списка"
        ></v-combobox>
      </div>
      <default-input />
      <div class="form_block">
        <p class="text-left form_block_title">Руководитель</p>
        <v-combobox filled v-model="currentData.DirectorList" :items="isLeaderType" outlined :rules="requiredRules" placeholder="Тип"></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <v-text-field
          id="oldName"
          v-model="currentData.inn"
          placeholder="Введите ИНН или название компании"
          class="align-center border-none"
          name="oldName"
          outlined
          type="number"
          :rules="innRules"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left mb-5 form_block_label">
          Наличие наблюдательного совета
        </p>
        <RadioGroup @isStatus="(status) => isTest1 = status" name="Existence of a supervisory board" />
      </div>
      <div v-if="isTest1" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименования наблюдательного совета
        </p>
        <v-text-field
          id="oldName"
          placeholder="Наименования"
          v-model="currentData.supervisoryBoard"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left form_block_label mb-5">
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
          v-model="currentData.collegialBody"
          class="align-center border-none"
          name="oldName"
          outlined
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
          v-model="currentData.individual"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
    </v-form>
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

export default {
  data: () => ({
    valid: true,
    currentData: {
      leaderList: null,
      DirectorList: null,
      inn: null,
      supervisoryBoard: true,
      collegialBody: true,
      individual: null,
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