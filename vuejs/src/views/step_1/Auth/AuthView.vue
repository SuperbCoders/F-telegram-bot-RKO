<template>
  <div class="auth_section">
    <div class="auth_logo_block mt-3">
      <img src="@/assets/images/logo.svg" alt="" />
    </div>
    <div class="auth_title_block">
      <h2 class="auth_title font-weight-bold">
        Заявка на открытие расчетного счета
      </h2>
    </div>
    <div class="auth_form mt-12">
      <v-form ref="form" v-model="valid" lazy-validation>
        <InnAndNameInput @input="getInnAndNameComnany" :value="currentData.company_name" />
        <v-text-field placeholder="Контактный номер телефона" outlined v-model="currentData.contact_number"
          :rules="requiredRules" :required="true" v-mask="'+# (###) ### ## ##'" masked="true" class="mt-5 auth_form">
        </v-text-field>
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
      </v-form>
    </div>
  </div>
</template>

<script>
import { getCompanyInn, getCompanyName } from "@/api/getInfoCompany";
import { mask } from "vue-the-mask";
import InnAndNameInput from '@/components/innAndNameInput.vue';
import { loadCurrentData } from '@/utils/loadStore'
import { auto_route } from '@/mixin/auto_route'

export default {
  directives: { mask },
  mixins: [auto_route],
  props: {
    number_step: {
      type: Number,
    }
  },
  data: () => ({
    currentData: {
      inn: "",
      company_name: "",
      contact_number: "",
      ogrn: "",
      opf: {},
      is_conditions: false,
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

  }),

  async mounted() {
    this.auto_route();

    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });


  },

  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$store.dispatch('addObjectFormData', {
          object: `step_${this.number_step}`,
          value: this.currentData
        });
        // this.$store.commit('addItemFormData', this.currentData)
        this.next();
      }
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    onClose() {
      this.$refs.contact_number.blur()
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
        this.currentData.short = data.suggestions[0].data?.name?.short
      }
    },
    async getInnAndNameComnany({ name, inn, ogrn, opf, short }) {
      this.currentData.company_name = name;
      this.currentData.inn = inn;
      this.currentData.ogrn = ogrn;
      this.currentData.opf = opf;
      this.currentData.short = short;
      console.log(short);
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
  font-family: mont;
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