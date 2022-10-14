<template>
  <div class="imformation_staff_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h3 class="text-left mb-10 font-bold w-50">
        Группа взаимосвязанных компаний
      </h3>
      <div class="form_block">
        <p class="text-left form_block_title">Название группы компаний</p>
        <v-text-field id="oldName" placeholder="Напишите назание" class="align-center border-none" name="oldName"
          outlined :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата начала действия</p>
        <v-menu :close-on-content-click="false" transition="scale-transition" offset-y min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field placeholder="xx.xx.xxxx" id="passportIssueDate" name="passportIssueDate" outlined
              append-icon="mdi-calendar-blank" readonly v-model="currentData.dateStarting" :rules="requiredRules" :required="true"
              v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="currentData.dateStarting" @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block mb-5">
        <p class="text-left form_block_title">Дата окончания действия</p>
        <v-menu :close-on-content-click="false" transition="scale-transition" offset-y
          min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field placeholder="xx.xx.xxxx" id="passportIssueDate" name="passportIssueDate"
              append-icon="mdi-calendar-blank" outlined readonly v-model="currentData.dateEnd" :rules="requiredRules"
              :required="true" v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="currentData.dateEnd" @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>
      </div>
      <h3 class="text-left structure_group_label mb-10">Состав группы компаний</h3>
      <div v-for="(itemForm, index) in currentData.groupList" :key="index" class="form_input_block">
        <div class="form_block">
          <p class="text-left form_block_title">Название компании</p>
          <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" v-model="itemForm.name"
            name="oldName" outlined :rules="requiredRules" :required="true"></v-text-field>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ИНН</p>
          <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" name="oldName"
            type="number" v-model="itemForm.inn" outlined :rules="innRules" :required="true"></v-text-field>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ОГРН</p>
          <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" name="oldName"
            v-model="itemForm.ogrn" outlined :rules="requiredRules" :required="true"></v-text-field>
        </div>
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a @click="deleteGroupList" class="form_block_delete_link text-decoration-none" href="#">
          <v-icon>mdi-trash-can-outline</v-icon>
          Удалить
        </a>
        <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="addGroupList()">
          <span class="pr-3">Добавить</span>
          <v-icon>mdi-plus-circle-outline</v-icon>
        </v-btn>
      </div>
    </v-form>
    <line-step :step='10' />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
export default {
  data: () => ({
    valid: true,
    currentData: {
      dataStarting: null,
      dataEnd: null,
      groupList: [
        {
          name: null,
          inn: null,
          ogrn: null,
        },
      ]
    },
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) => (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
      (v) => (v && v.length <= 12) || "ИНН не может содержать больше 12 симоволов",
    ],
    passportIssueDateMenu: null,
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/intelligence");
      }
    },
    addGroupList() {
      const defaultGroupItem = {
        name: null,
        inn: null,
        ogrn: null,
      }
      this.currentData.groupList.push(defaultGroupItem);
    },
    deleteGroupList() {
      if (this.currentData.groupList.length > 1) {
        this.currentData.groupList.pop();
      }
    },
  },
  components: {
    LineStep,
  }
};
</script>

<style>
.w-50 {
  width: 50%;
}
</style>