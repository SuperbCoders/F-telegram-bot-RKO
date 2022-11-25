<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold form_block_label">
      Структура органов управления
    </h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Высший орган управления</p>
        <v-combobox v-model="currentData.supreme_management_body" filled :rules="requiredRules" required
          :items="isLeaderList" outlined placeholder="Выберите из списка"></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title"><span class="star">*</span>Руководитель</p>
        <v-combobox filled v-model="currentData.supreme_management_person" :items="isLeaderType" outlined
          :rules="requiredRules" placeholder="Тип"></v-combobox>
      </div>
      <div v-if="isManagementCompany" class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <InnAndNameInput v-model="currentData.supreme_management_inn" />
      </div>
      <div class="form_group mb-10">
        <p class="text-left form_block_label mt-5">
          Наличие наблюдательного совета
        </p>
        <RadioGroup @isStatus="(status) => (currentData.is_collegiate_body = status)"
          :status="currentData.is_collegiate_body" name="Existence of a supervisory board" />
      </div>
      <div v-if="currentData.is_collegiate_body" class="form_block mt-2">
        <p class="text-left form_block_title">
          <span class="star">*</span>
          Наименование наблюдательного совета
        </p>

        <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" name="oldName"
          v-model="currentData.collegiate_person" outlined :rules="requiredRules" :required="true"></v-text-field>
        <div class="title_btn">Члены наблюдательного совета</div>
        <v-card elevation="2" class="pa-4 mb-2" v-for="(val, key) in list_supervisoty_board_persone" :key="key">
          {{  renderName(val['page-1']) }}
        </v-card>

        <div class="contain_btn_add">
          <v-btn large style="width: 50%; background: #F3F4F4 !important; color: #5B656D !important" class="text-center
                d-flex
                align-center
                justify-center
                add_form" @click="createSupervisoryBoard">
            <span class="pr-3">Добавить</span>
            <v-icon>mdi-plus-circle-outline</v-icon>
          </v-btn>
        </div>

      </div>
      <div class="form_group mt-5">
        <p class="text-left form_block_label mb-2">
          Наличие коллегиального исполнительного органа
        </p>
        <RadioGroup @isStatus="(status) => (currentData.is_supervisoty = status)" :status="currentData.is_supervisoty"
          name="The presence of a collegial executive body" />
      </div>
      <div v-if="currentData.is_supervisoty" class="form_block mt-5">
        <p class="text-left form_block_title">
          <span class="star">*</span>
          Наименование коллегиального исполнительного органа
        </p>
        <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" name="oldName" outlined
          v-model="currentData.supervisoty_board_persone_name" :rules="requiredRules" :required="true"></v-text-field>
        <div class="title_btn">Члены коллегиального исполнительного органа</div>
        <v-card elevation="2" class="pa-4 mb-2" v-for="(val, key) in list_collegial_executive_body" :key="key">
          {{  renderName(val['page-1']) }}
        </v-card>

        <div class="contain_btn_add">
          <v-btn large class="d-flex
                align-center
                justify-center
                add_form" style="width: 50%; background: #F3F4F4 !important; color: #5B656D !important"
            @click="createCollegialExecutive">
            <span class="pr-3">Добавить</span>
            <v-icon>mdi-plus-circle-outline</v-icon>
          </v-btn>
        </div>
      </div>
    </v-form>
    <line-step :step="2" class="mt-4" />
    <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">
      Продолжить
    </v-btn>
  </div>
</template>
<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";
import LineStep from "../../components/line_step/line_step.vue";
import InnAndNameInput from '../../components/innAndNameInput.vue'
import { mask } from "vue-the-mask";

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listCompany: [],
    currentData: {
      supreme_management_body: "Единственный участник (один участник с долей 100%)",
      supreme_management_person: "Руководитель",
      supreme_management_inn: "",

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
          object: "step_3",
          value: this.currentData,
        });
        this.$router.push("/information-staff");
      }
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
    renderName(obj){
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
    RadioGroup,
    LineStep,
    InnAndNameInput,
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