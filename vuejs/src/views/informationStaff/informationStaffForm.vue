<template>
  <div class="imformation_staff_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h3 class="text-left mb-10 font-bold w-50">
        Группа взаимосвязанных компаний
      </h3>
      <v-btn block large class="mb-10" color="primary auth_form_bth" @click="skip()">Пропустить
      </v-btn>
      <div class="form_block">
        <p class="text-left form_block_title">Название группы компаний</p>
        <v-text-field id="oldName" placeholder="Напишите назание" class="align-center border-none" name="oldName"
          v-model="currentData.company_group_name" outlined :rules="requiredRules" :required="true"></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата начала действия</p>
        <v-menu :close-on-content-click="isActiveStartDate()" transition="scale-transition" offset-y min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field placeholder="xx.xx.xxxx" id="passportIssueDate" name="passportIssueDate" outlined
              append-icon="mdi-calendar-blank" readonly @click="currentData.end_date = ''"
              v-model="currentData.start_date" :rules="requiredRules" :required="true" v-bind="attrs" v-on="on">
            </v-text-field>
          </template>
          <v-date-picker v-model="currentData.start_date" :active-picker.sync="activePickerStartDate"
            @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block mb-5">
        <p class="text-left form_block_title">Дата окончания действия</p>

        <v-menu :close-on-content-click="isActiveEndDate()" transition="scale-transition" offset-y min-width="auto">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field placeholder="xx.xx.xxxx" id="passportIssueDate" name="passportIssueDate"
              append-icon="mdi-calendar-blank" outlined readonly v-model="currentData.end_date" :rules="requiredRules"
              :required="true" v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="currentData.end_date" :min="currentData.start_date"
            :active-picker.sync="activePickerEndDate" @input="passportIssueDateMenu = false"></v-date-picker>
        </v-menu>

      </div>
      <h3 class="text-left structure_group_label mb-10">
        Состав группы компаний
      </h3>
      <div v-for="(itemForm, index) in currentData.group_members" :key="index" class="form_input_block">
        <div class="form_block">
          <p class="text-left form_block_title">Наименование компании или ИНН</p>
          <InnAndNameInput :value="itemForm.name" @input="(e) => {
            itemForm.name = e;
            inputName(itemForm);
          }
          " />
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ОГРН</p>
          <v-text-field id="oldName" placeholder="Напишите ОГРН" class="align-center border-none" name="oldName"
            v-mask="'### ### ### ### ###'" masked="true" v-model="itemForm.ogrn" outlined :rules="requiredRules"
            :required="true"></v-text-field>
        </div>
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a @click="deleteGroupList" class="form_block_delete_link text-decoration-none" href="#">
          <img src="../../assets/trash.svg" alt="">
          <span class="pl-2">Удалить</span>
        </a>
        <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="addGroupList()">
          <span class="pr-2">Добавить</span>
          <img src="../../assets/plus-circle.svg" alt="">
        </v-btn>
      </div>
    </v-form>
    <line-step :step="3" />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "../../components/line_step/line_step.vue";
import { mask } from "vue-the-mask";
import InnAndNameInput from '../../components/innAndNameInput.vue';
import { getCompanyInn } from '../../api/getInfoCompany';

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listCompany: [],
    currentData: {
      company_group_name: null,
      start_date: null,
      end_date: null,
      group_members: [
        {
          name: null,
          inn: null,
          ogrn: null,
        },
      ],

    },
    activePickerEndDate: null,
    activePickerStartDate: null,
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
    ],
    passportIssueDateMenu: null,
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: 'step_4',
          value: this.currentData
        })
        this.$router.push("/intelligence");
      }
    },
    async inputName(itemForm) {
      const name = itemForm.name;
      if (name.match(/^\d+/)) {
        const data = await getCompanyInn(name);
        if (data.suggestions.length > 0) {
          const ogrn = data.suggestions[0]?.data?.ogrn;
          itemForm.ogrn = ogrn;
        }
      } else {
        const data = await getCompanyInn(name.split(',')[0]);
        if (data.suggestions.length > 0) {
          const ogrn = data.suggestions[0]?.data?.ogrn;
          itemForm.ogrn = ogrn;
        }
      }


    },
    skip() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_4',
        value: this.currentData
      })
      this.$router.push("/intelligence");
    },
    addGroupList() {
      const defaultGroupItem = {
        name: null,
        inn: null,
        ogrn: null,
      };
      this.currentData.group_members.push(defaultGroupItem);
    },
    deleteGroupList() {
      if (this.currentData.group_members.length > 1) {
        this.currentData.group_members.pop();
      }
    },
    isActiveEndDate() {
      if (this.currentData.end_date !== '' && this.activePickerEndDate === 'DATE') {
        return true
      }
      return false
    },
    isActiveStartDate() {
      if (this.currentData.start_date !== '' && this.activePickerStartDate === 'DATE') {
        return true
      }
      return false
    },
  },
  components: {
    LineStep,
    InnAndNameInput,
  },
};
</script>

<style>
.w-50 {
  width: 50%;
}

.combobox .v-label {
  color: #323E48;
}

.combobox .v-icon {
  display: none;
}
</style>