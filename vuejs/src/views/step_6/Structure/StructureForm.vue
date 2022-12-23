<template>
  <div class="structure_form">
    <h2 class="text-left mb-5 font-bold form_block_label">
      Структура органов управления
    </h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-radio-group v-model="currentData.structure_value" class="checkboxs">
        <v-radio label="Общее собрание участников" value="Общее собрание участников" />
        <v-radio label="Единоличный исполнительный орган" value="Единоличный исполнительный орган" />
        <v-radio label="Иное" value="Иное" />
      </v-radio-group>

    </v-form>
    <line-step :step="2" class="mt-4" />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
      Продолжить
    </v-btn>
  </div>
</template>
<script>
import LineStep from "@/components/line_step/line_step.vue";
import { mask } from "vue-the-mask";

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listCompany: [],
    currentData: {
      structure_value: "",

      is_collegiate_body: false,
      supervisoty_board_persone_name: "",
      list_collegial_executive_body: [],

      is_supervisoty: false,
      collegiate_person: "",
      list_supervisoty_board_persone: [],
    },
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
    ],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.currentData.list_collegial_executive_body = this.list_collegial_executive_body;
        this.currentData.list_supervisoty_board_persone = this.list_supervisoty_board_persone;

        this.$store.dispatch("addObjectFormData", {
          object: "step_6",
          value: this.currentData,
        });
        this.next()
      }
    },
    getCompanyData({ inn }) {
      this.currentData.supreme_management_inn = inn;
    },
    next() {
      this.$router.push({ name: 'step_7' });
    },
    addObjectList(object) {
      const result = {
        account_onw_role: [],
        account_own_lastname: null,
        account_own_gender: null,
        account_own_name: null,
        account_own_surname: null,
      };
      object.push(result);
    },
    deleteObjectList(object) {
      if (object.length > 1) {
        object.pop();
      }
    },
    async createSupervisoryBoard() {
      await this.$store.commit('addSupervisoryBoardPersone')
      this.currentData.list_supervisoty_board_persone = this.$store.state.formData.step_3.list_supervisoty_board_persone;
      this.currentData.list_collegial_executive_body = this.$store.state.formData.step_3.list_collegial_executive_body;
      await this.$store.dispatch('addObjectFormData', {
        object: 'step_3',
        value: this.currentData,
      })

      this.$router.push({
        path: "/individual-info",
        query: {
          "type": "SupervisoryBoard"
        }
      })
    },
    async createCollegialExecutive() {
      await this.$store.commit('addCollegialExecutiveBody')
      this.currentData.list_supervisoty_board_persone = this.$store.state.formData.step_3.list_supervisoty_board_persone;
      this.currentData.list_collegial_executive_body = this.$store.state.formData.step_3.list_collegial_executive_body;
      this.$store.dispatch('addObjectFormData', {
        object: 'step_3',
        value: this.currentData
      })
      this.$router.push({
        path: "/individual-info",
        query: {
          "type": "CollegialExecutive"
        }
      })
    },
    renderName(obj) {
      return `${obj?.account_own_lastname} ${obj?.account_own_name} ${obj?.account_own_surname}`
    }

  },
  computed: {
    isLeaderList() {
      return this.$store.getters.isList;
    },
    isLeaderType() {
      return this.$store.getters.isLeaderTypeTitle;
    },
    isManagementCompany() {
      return (
        this.currentData.supreme_management_person === "Управляющая компания"
      );
    },
    list_supervisoty_board_persone() {
      return this.$store.state.formData.step_3.list_supervisoty_board_persone
    },
    list_collegial_executive_body() {
      return this.$store.state.formData.step_3.list_collegial_executive_body
    }
  },
  components: {
    LineStep,
  },
  mounted() {
    const dataStep = this.$store.state.formData.step_3;
    if (dataStep) {
      this.currentData.supreme_management_body =
        dataStep.supreme_management_body;
      this.currentData.supreme_management_inn = dataStep.supreme_management_inn;

      this.currentData.supreme_management_person = dataStep.supreme_management_person;
      this.currentData.supervisoty_board_persone_name = dataStep.supervisoty_board_persone_name;
      this.currentData.collegiate_person = dataStep.collegiate_person;
      this.currentData.is_supervisoty = dataStep.is_supervisoty;
      this.currentData.is_collegiate_body = dataStep.is_collegiate_body;
    }
  },
};
</script>

<style>
.structure_form_title {
  font-family: Geometria;
}

.form_block {
  font-family: Roboto;
  font-size: 14px;
}

.form_block_title {
  font-size: 12px;
  width: 300px;
}

.form_block_label {
  font-family: Roboto;
  color: black;
}

.add_btn {
  background: #F3F4F4 !important;
  color: #000 !important;
}

.auth_form_bth {
  border-radius: 10px;
  color: white !important;
  text-transform: capitalize;
  font-size: 14px;
}

.contain_btn_add {
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
}

.title_btn {
  color: #8E909B;
  font-size: 13px;
  margin-bottom: 3px;
}
</style>