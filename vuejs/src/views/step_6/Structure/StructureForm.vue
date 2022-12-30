<template>
  <div class="structure_form">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
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
    <line-step :step="6" class="mt-4" />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
      Продолжить
    </v-btn>
  </div>
</template>
<script>
import LineStep from "@/components/line_step/line_step.vue";
import { mask } from "vue-the-mask";
import { loadCurrentData } from '@/utils/loadStore'

export default {
  directives: { mask },
  props: {
    number_step: {
      type: Number,
    }
  },
  data: () => ({
    valid: true,
    listCompany: [],
    currentData: {
      structure_value: "",
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
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
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

    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });

    if (this.$store.state.formData.step_1.opf.short !== "ИП") {
      this.next();
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