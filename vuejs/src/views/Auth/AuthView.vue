<template>
  <div class="auth_section">
    <div class="auth_logo_block mt-3">
      <img src="@/assets/images/logo.svg" alt="" />
    </div>
    <div class="auth_title_block">
      <h2 class="auth_title font-weight-bold">
        Заявка на открытие рассчетного счета
      </h2>
    </div>
    <div class="auth_form mt-12">
      <v-form ref="form" v-model="valid" lazy-validation>
        <InnAndNameInput :value="inn_or_name" @input="getInnAndNameComnany" />
        <v-text-field label="Контактный номер телефона" outlined v-model="currentData.contact_number"
          :rules="requiredRules" :required="true" v-mask="'+# (###) ### ## ##'" masked="true" class="mt-1 auth_form">
        </v-text-field>
        <div class="auth_form_cheked_block d-flex w-100">
          <v-checkbox :rules="requiredRules">
            <template v-slot:label>
              <div class="text-left auth_form_link_container">
                <span class="black--text">Я ознакомился и согласен с условиями </span>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <a target="_blank" class="text-decoration-none" href="https://vuetifyjs.com" v-on="on" @click.stop>
                      обработки и хранения персональных данных
                    </a>
                    <span class="black--text"> а также с условиями </span>

                    <a target="_blank" class="text-decoration-none text-left" href="https://vuetifyjs.com" v-on="on"
                      @click.stop>
                      <span>резервирования счета,</span>

                    </a>
                  </template>
                </v-tooltip>
              </div>
            </template>
          </v-checkbox>
        </div>
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
      </v-form>
    </div>
  </div>
</template>

<script>
import { getCompanyInn, getCompanyName } from "../../api/getInfoCompany";
import { mask } from "vue-the-mask";
import InnAndNameInput from '../../components/innAndNameInput.vue';

export default {
  directives: { mask },
  data: () => ({
    currentData: {
      inn: null,
      company_name: null,
      contact_number: null,
    },
    inn_or_name: '',
    listCompany: [],
    valid: true,
    name: "",
    maskPhone: {},
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
    ],
    email: "",
    requiredRules: [(v) => !!v || "Это поле обязательно"],
    nameCompanyRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    numberRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
    ],
    select: null,
    items: ["Item 1", "Item 2", "Item 3", "Item 4"],
  }),

  async mounted() {
    const phone = this.$route.query?.phone;
    if (phone) {
      this.currentData.contact_number = phone;

      const response = await fetch(`https://rko-bot.spaaace.io/api/loan-application/current/${phone}/`)
      // const response = await fetch(`http://localhost:8000/api/loan-application/current/${phone}/`)
      const formData = await response.json();
      console.log('formData', formData);
      this.$store.dispatch("loadObjectFormData", formData);
      const last_step = formData?.last_step;
      if (!last_step) {
        return
      }
      const arr_last_step = last_step.split("*");

      if (arr_last_step.length === 2) {
        const type = arr_last_step[1];
        const sub_last_step = arr_last_step[0];
        console.log(sub_last_step, type);
        let next_push = "/";
        switch (sub_last_step) {
          case 'page-0':
            next_push = '/individual-info';
            break;
          case 'page-1':
            next_push = '/documents-forms';
            break;
          case 'page-2':
            next_push = '/foreign-person';
            break
          case 'page-3':
            next_push = '/kinship-status-forms';
            break
          case 'page-4':
            next_push = '/address-form';
            break
          case 'page-5':
            next_push = '/email-form';
            break
          case 'page-6':
            next_push = '/document';
            break
          case 'page-7':
            next_push = '/client-info';
            break
          case 'page-8':
            next_push = '/document-fogeiner';
            break
          case 'page-9':
            next_push = '/all-data-persone';
            break
        }
        if (type === 'supervisory') {
          this.$router.push({ 'path': next_push, query: { "type": "SupervisoryBoard" } });
        } else if (type === 'collegial') {
          this.$router.push({ 'path': next_push, query: { "type": "CollegialExecutive" } });
        }
      } else {
        let next_push = "/";
        switch (last_step) {
          case 'step_1':
            next_push = '/address';
            break;
          case 'step_2':
            next_push = '/sctructure';
            break
          case 'step_3':
            next_push = '/information-staff';
            break
          case 'step_4':
            next_push = '/intelligence';
            break
          case 'step_6':
            next_push = '/planning';
            break
          case 'step_7':
            next_push = '/beneficiaries';
            break
          case 'step_8':
            next_push = '/purposes';
            break
          case 'step_9':
            next_push = '/approvals';
            break
          case 'step_10':
            next_push = '/rate';
            break
          case 'step_11':
            next_push = '/all-data';
            break
        }
        this.$router.push(next_push);
      }
    }

  },

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: 'step_1',
          value: this.currentData
        });
        // this.$store.commit('addItemFormData', this.currentData)
        this.$router.push("/address");
      }
    },

    async getCompanyFromInn(inn) {
      if ((inn.length >= 10)) {
        const company = await getCompanyInn(inn);
        if (company?.suggestions.length > 0) {
          this.$store.commit("setDataCompany", company?.suggestions[0]);
          const data = company?.suggestions[0];
          this.currentData.company_name = `${data.value}, ${data.data.address.unrestricted_value}`;
        }
      }
    },

    async getListCompanyFromName(e) {
      const value = e.target.value;
      const data = await getCompanyName(value);
      this.listCompany = data.suggestions.map((elem) => `${elem.value}, ${elem.data?.address?.unrestricted_value}`);
    },
    async getCompanyFromName() {
      const data = await getCompanyName(this.currentData.company_name.split(',')[0]);
      if (data.suggestions.length === 1) {
        this.currentData.inn = data.suggestions[0].data.inn
      }
    },
    async getInnAndNameComnany(input) {
      this.inn_or_name = input;
      if (input.match(/^\d+/)) {
        const data = await getCompanyInn(input);
        this.currentData.inn = input;
        if (data.suggestions.length > 0) {
          this.currentData.company_name = data.suggestions[0].value;
        }
      } else {
        const data = await getCompanyInn(input.split(',')[0]);
        this.currentData.company_name = input;
        if (data.suggestions.length > 0) {
          this.currentData.inn = data.suggestions[0].data.inn;
        }
      }
    }
  },
  computed: {},
  components: {
    InnAndNameInput
  }
};
</script>
<style scoped>
.auth_title_block {
  margin-top: 30px;
}

.auth_title {}

.auth_form {
  border-radius: 8px;
  font-family: face;
}

.auth_form_bth {
  border-radius: 10px;
  text-transform: capitalize;
  font-size: 14px;
  font-weight: 400;
}

.auth_form_link_container {
  font-size: 14px;
}

.combobox .v-icon {
  display: none;
}
</style>