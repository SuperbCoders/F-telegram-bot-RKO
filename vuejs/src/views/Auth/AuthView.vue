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
        <v-text-field
          label="Введите ИНН"
          outlined
          v-model="currentData.inn"
          :rules="innRules"
          v-mask="'### ### ### ###'"
          masked="true"
          required
          @input="getCompanyFromInn"
          class="mt-1 auth_form"
        ></v-text-field>
        <v-combobox 
          label="Наименование компании"
          outlined
          v-model="currentData.company_name"
          :rules="requiredRules"
          required
          class="mt-1 auth_form combobox"
          @keyup="getListCompanyFromName"
          @input="getCompanyFromName"
          :items="listCompany"
        ></v-combobox>
        <v-text-field
          label="Контактный номер телефона"
          outlined
          v-model="currentData.contact_number"
          :rules="requiredRules"
          :required="true"
          v-mask="'+# (###) ### ## ##'"
          masked="true"
          class="mt-1 auth_form"
        ></v-text-field>
        <div class="auth_form_cheked_block d-flex w-100">
          <v-checkbox :rules="requiredRules">
            <template v-slot:label>
              <div class="text-left auth_form_link_container">
                <span>Я ознакомился и согласен с условиями</span>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <a
                      target="_blank"
                      class="text-decoration-none"
                      href="https://vuetifyjs.com"
                      v-on="on"
                      @click.stop
                    >
                      обработки и хранения персональных данных
                    </a>
                    а также с условиями
                    <a
                      target="_blank"
                      class="text-decoration-none text-left"
                      href="https://vuetifyjs.com"
                      v-on="on"
                      @click.stop
                    >
                      резервирного счета,
                    </a>
                  </template>
                </v-tooltip>
              </div>
            </template>
          </v-checkbox>
        </div>
        <v-btn
          block
          large
          :disabled="!valid"
          class="mt-10 auth_form_bth"
          color="primary"
          @click="validate"
          >Продолжить</v-btn
        >
      </v-form>
    </div>
  </div>
</template>

<script>
import { getCompanyInn, getCompanyName } from "../../api/getInfoCompany";
import { mask } from "vue-the-mask";

export default {
  directives: { mask },
  data: () => ({
    currentData: {
      inn: null,
      company_name: null,
      contact_number: null,
    },
    listCompany: [],
    valid: true,
    name: "",
    maskPhone: {},
    innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) =>
        (v && v.length >= 13) || "ИНН не может содержать меньше 10 симоволов",
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

  mounted() {
    const phone = this.$route.query?.phone;
    if (phone) {
      this.currentData.contact_number = phone;
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
      if ((inn.length >= 10) & (inn.length <= 12)) {
        const company = await getCompanyInn(inn);
        if (company?.suggestions.length > 0) {
          this.$store.commit("setDataCompany", company?.suggestions[0]);
          const data = company?.suggestions[0];
          this.currentData.company_name = `${data.value} ${data.data.address.unrestricted_value}`;
        }
      }
    },

    async getListCompanyFromName(e) {
      const value = e.target.value;
      const data = await getCompanyName(value);
      console.log(data);
      this.listCompany = data.suggestions.map((elem)=> `${elem.value} ${elem.data?.address?.unrestricted_value}`);
    },
    async getCompanyFromName() {
      const data = await getCompanyName(this.currentData.company_name);
      if(data.suggestions.length === 1) {
        this.currentData.inn = data.suggestions[0].data.inn
      }
    }
  },
  computed: {},
};
</script>
<style scoped>
.auth_title_block {
  margin-top: 30px;
}
.auth_title {
}
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