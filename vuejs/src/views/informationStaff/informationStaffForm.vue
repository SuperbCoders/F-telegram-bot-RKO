<template>
  <div class="imformation_staff_section">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h3 class="text-left mb-10 font-bold w-50">
        Группа взаимосвязанных компаний
      </h3>
      <div class="form_block">
        <p class="text-left form_block_title">Название группы компаний</p>
        <v-text-field
          id="oldName"
          placeholder="Напишите назание"
          class="align-center border-none"
          name="oldName"
          v-model="currentData.company_group_name"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Дата начала действия</p>
        <v-menu
          :close-on-content-click="true"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="xx.xx.xxxx"
              id="passportIssueDate"
              name="passportIssueDate"
              outlined
              append-icon="mdi-calendar-blank"
              readonly
              @click="currentData.end_date = ''"
              v-model="currentData.start_date"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="currentData.start_date"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
      <div class="form_block mb-5">
        <p class="text-left form_block_title">Дата окончания действия</p>
        <v-menu
          :close-on-content-click="true"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              placeholder="xx.xx.xxxx"
              id="passportIssueDate"
              name="passportIssueDate"
              append-icon="mdi-calendar-blank"
              outlined
              readonly
              v-model="currentData.end_date"
              :rules="requiredRules"
              :required="true"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="currentData.end_date"
            :min="currentData.start_date"
            @input="passportIssueDateMenu = false"
          ></v-date-picker>
        </v-menu>
      </div>
      <h3 class="text-left structure_group_label mb-10">
        Состав группы компаний
      </h3>
      <div
        v-for="(itemForm, index) in currentData.group_members"
        :key="index"
        class="form_input_block"
      >
        <div class="form_block">
          <p class="text-left form_block_title">Название компании</p>
          <v-combobox
            label="Напишите название"
            outlined
            v-model="itemForm.name"
            :rules="requiredRules"
            required
            class="align-center border-none combobox"
            @keyup="getListCompanyFromName"
            @input="getCompanyFromName(itemForm)"
            :items="listCompany"
          ></v-combobox>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ИНН</p>
          <v-text-field
            id="oldName"
            placeholder="Напишите ИНН"
            class="align-center border-none"
            name="oldName"
            v-model="itemForm.inn"
            v-mask="'### ### ### ###'"
            masked="true"
            @input="getCompanyFromInn(itemForm)"
            outlined
            :rules="innRules"
            :required="true"
          ></v-text-field>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ОГРН</p>
          <v-text-field
            id="oldName"
            placeholder="Напишите ОГРН"
            class="align-center border-none"
            name="oldName"
            v-mask="'### ### ### ### ###'"
            masked="true"
            v-model="itemForm.ogrn"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a
          @click="deleteGroupList"
          class="form_block_delete_link text-decoration-none"
          href="#"
        >
          <v-icon>mdi-trash-can-outline</v-icon>
          Удалить
        </a>
        <v-btn
          class="text-center d-flex align-center justify-center ml-10 add_form"
          @click="addGroupList()"
        >
          <span class="pr-3">Добавить</span>
          <v-icon>mdi-plus-circle-outline</v-icon>
        </v-btn>
      </div>
    </v-form>
    <line-step :step="11" />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "../../components/line_step/line_step.vue";
import { mask } from "vue-the-mask";
import { getCompanyInn, getCompanyName } from "../../api/getInfoCompany";

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
          object: 'step_11',
          value: this.currentData
        })
        this.$router.push("/intelligence");
      }
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
    async getListCompanyFromName(e) {
      const value = e.target.value;
      const data = await getCompanyName(value);
      this.listCompany = data.suggestions.map((elem) => `${elem.value} ${elem.data?.address?.unrestricted_value}`);
    },
    async getCompanyFromName(itemForm) {
      const data = await getCompanyName(itemForm.name);
      if (data.suggestions.length === 1) {
        itemForm.inn = data.suggestions[0].data.inn;
      }
    },
    async getCompanyFromInn(itemForm) {
      const inn = itemForm.inn;
      if (inn.length >= 12) {
        const company = await getCompanyInn(inn);
        if (company?.suggestions.length > 0) {
          const data = company?.suggestions[0]
          itemForm.name = `${data.value} ${data.data?.address?.unrestricted_value}`;
          itemForm.ogrn = company?.suggestions[0].data.ogrn;
        }
      }
    },
  },
  components: {
    LineStep,
  },
};
</script>

<style>
.w-50 {
  width: 50%;
}
.combobox .v-label {
  color: #b3b2b2;
}
.combobox .v-icon {
  display: none;
}
</style>