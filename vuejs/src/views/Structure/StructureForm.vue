<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold form_block_label">
      Структура органов управления
    </h2>
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
          placeholder="Высший орган управления"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Руководитель</p>
        <v-combobox
          filled
          v-model="currentData.supreme_management_person"
          :items="isLeaderType"
          outlined
          :rules="requiredRules"
          placeholder="Тип"
        ></v-combobox>
      </div>
      <div v-if="isManagementCompany" class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <v-combobox
          label="Введите ИНН или название компании"
          outlined
          v-model="currentData.supreme_management_inn"
          :rules="requiredRules"
          required
          class="mt-1 auth_form combobox"
          @keyup="getListCompanyFromName"
          :items="listCompany"
        ></v-combobox>
      </div>
      <div class="form_group mb-10">
        <p class="text-left form_block_label mt-5">
          Наличие наблюдательного совета
        </p>
        <RadioGroup
          @isStatus="(status) => (currentData.is_collegiate_body = status)"
          :status="currentData.is_collegiate_body"
          name="Existence of a supervisory board"
        />
      </div>
      <div v-if="currentData.is_collegiate_body" class="form_block mt-2">
        <p class="text-left form_block_title">
          Наименования наблюдательного совета
        </p>
        <v-text-field
            id="oldName"
            placeholder="Наименования"
            class="align-center border-none"
            name="oldName"
            v-model="currentData.supervisory"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
          <v-card
            elevation="2"
            class="pa-4 mb-2"
            v-for="(val, key) in listSupervisotyBoardPersone" :key="key"
          >
            {{ val['page-1'].account_own_lastname }}
            {{ val['page-1'].account_own_name }}
            {{ val['page-1'].account_own_surname }}
          </v-card>
          <div class="title_btn">Члены наблюдательного совета</div>
          <div class="contain_btn_add">
            <v-btn
              large
              style="width: 50%; background: #F3F4F4 !important; color: #5B656D !important"
              class="text-center
                d-flex
                align-center
                justify-center
                add_form"
              @click="createSupervisoryBoard"
            >
              <span class="pr-3">Добавить</span>  
              <v-icon>mdi-plus-circle-outline</v-icon>
            </v-btn>
          </div>
          
      </div>
      <div class="form_group mt-5">
        <p class="text-left form_block_label mb-2">
          Наличие коллегиального исполнительного органа
        </p>
        <RadioGroup
          @isStatus="(status) => (currentData.is_supervisoty = status)"
          :status="currentData.is_supervisoty"
          name="The presence of a collegial executive body"
        />
      </div>
      <div v-if="currentData.is_supervisoty" class="form_block mt-5">
        <p class="text-left form_block_title">
          Наименование коллегиального исполнительного органа
        </p>
        <v-text-field
          id="oldName"
          placeholder="Наименование"
          class="align-center border-none"
          name="oldName"
          outlined
          v-model="currentData.supervisotyBoardPersone_name"
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
        <v-card
            elevation="2"
            class="pa-4 mb-2"
            v-for="(val, key) in listCollegialExecutiveBody" :key="key"
          >
            {{ val['page-1'].account_own_lastname }}
            {{ val['page-1'].account_own_name }}
            {{ val['page-1'].account_own_surname }}
          </v-card>
          <div class="title_btn">Члены коллегиального исполнительного органа</div>
          <div class="contain_btn_add">
            <v-btn
              large
              class="d-flex
                align-center
                justify-center
                add_form"
              style="width: 50%; background: #F3F4F4 !important; color: #5B656D !important"
              @click="createCollegialExecutive"
            >
              <span class="pr-3">Добавить</span>  
              <v-icon>mdi-plus-circle-outline</v-icon>
            </v-btn>
          </div>
      </div>
    </v-form>
    <line-step :step="2" class="mt-2" />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
    >
      Продолжить
    </v-btn>
  </div>
</template>
<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";
import LineStep from "../../components/line_step/line_step.vue";
import { getCompanyName } from "../../api/getInfoCompany";
import { mask } from "vue-the-mask";

export default {
  directives: { mask },
  data: () => ({
    valid: true,
    listCompany: [],
    currentData: {
      supreme_management_body: null,
      supreme_management_type: null,
      supreme_management_inn: null,
      supreme_management_person: null,
      is_collegiate_body: false,
      supervisory: "",
      supervisotyBoardPersone_name: "",
      is_supervisoty: false,
      collegiate_person: null,
    },
    isTest1: false,
    isTest2: false,
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 13) || "ИНН не может содержать меньше 10 симоволов",
    ],
    requiredRules: [(v) => !!v || "Это поле обязательно"],
  }),

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {

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
    async getListCompanyFromName(e) {
      const value = e.target.value;
      const data = await getCompanyName(value);
      if (value.match(/^\d+/)) {
        this.listCompany = data.suggestions.map((elem) => elem.data.inn);
      } else {
        this.listCompany = data.suggestions.map((elem) => `${elem.value} ${elem.data?.address?.unrestricted_value}`);
      }
    },
    createSupervisoryBoard() {
      this.$store.dispatch('addObjectFormData', {
          object: 'step_3',
          value: this.currentData
        })
      this.$router.push({
        path: "/individual-info", 
        query: {
          "type": "SupervisoryBoard"
        }
      })
    },
    createCollegialExecutive() {
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
    listSupervisotyBoardPersone() {
      return this.$store.state.listSupervisotyBoardPersone
    },
    listCollegialExecutiveBody() {
      return this.$store.state.listCollegialExecutiveBody
    }
  },
  components: {
    RadioGroup,
    LineStep,
  },
  mounted () {
    const dataStep = this.$store.state.formData.step_3;
    if (dataStep) {
      this.currentData.supreme_management_body =
        dataStep.supreme_management_body;
      this.currentData.supreme_management_type =
        dataStep.supreme_management_type;
      this.currentData.supreme_management_inn = dataStep.supreme_management_inn;

      this.currentData.supreme_management_person = dataStep.supreme_management_person;
      this.currentData.supervisotyBoardPersone_name = dataStep.supervisotyBoardPersone_name;
      this.currentData.supervisory = dataStep.supervisory;
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
  width: 200px;
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