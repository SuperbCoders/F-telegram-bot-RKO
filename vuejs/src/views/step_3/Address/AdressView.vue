<template>
  <div class="structure_group_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <h2 class="text-left structure_group_title mb-10">Адреса компании</h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div v-for="(itemForm, index) in currentData.addresses" :key="index" class="form_input_block checkboxs">
        <div class="form_block mb-5">
          <v-checkbox @click="isTypeAdress(itemForm)" v-model="itemForm.type_address" label="Юридический"
            value="Юридический" hide-details>
          </v-checkbox>
          <v-checkbox @click="isTypeAdress(itemForm)" v-model="itemForm.type_address" label="Почтовый" value="Почтовый"
            hide-details></v-checkbox>
        </div>
        <p class="error_message" v-if="!valid && currentData.type_address > 0">
          Выберите пункт
        </p>
        <div class="form_block">
          <p class="text-left form_block_title">Адрес</p>
          <AddressInput label="Введите адрес" :index="index" v-model="itemForm.address" />
        </div>
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a @click="deleteGroupList" :class="{ form_block_delete_link_delete: currentData.addresses.length <= 1 }"
          class="form_block_delete_link text-decoration-none" href="#">
          <img src="@/assets/trash.svg" alt="">
          <span class="pl-2 ">Удалить</span>
        </a>
        <v-btn class="text-center d-flex align-center justify-center ml-10 add_form" @click="addGroupList()">
          <span class="pr-2">Добавить</span>
          <img src="@/assets/plus-circle.svg" alt="">
        </v-btn>
      </div>
      <line-step :step="number_step" />

      <v-btn block large :disabled="(!isValidAllAddress)" class="mt-10 auth_form_bth" color="primary" @click="validate">
        Продолжить
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import LineStep from "@/components/line_step/line_step.vue";
import AddressInput from '@/components/addressInput.vue';
import { loadCurrentData } from '@/utils/loadStore'

export default {
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      groupList: [
        {
          name: null,
          inn: null,
          ogrn: null,
        },
      ],

      currentData: {
        addresses: [
          {
            type_address: [],
            legal_address: "",
            mail_address: "",
            address: "",
          },
        ],
      },
      currentResult: {
        addresses: [],
      },
      addresses: [],
      checkboxList: [],
      valid: false,
      innRules: [
        (v) => !!v || "Это поле обязательно",
        (v) =>
          (v && v.length >= 13) || "ИНН не может содержать меньше 10 симоволов",
      ],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  mounted() {
    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });
  },
  methods: {
    validate() {
      this.currentData.addresses.map((item) => {
        this.currentResult.addresses.push({
          legal_address: item.legal_address,
          physic_address: item.physic_address,
          mail_address: item.mail_address,
        });
      });
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.dispatch("addObjectFormData", {
          object: `step_${this.number_step}`,
          value: this.currentData,
        });
        this.next();
      }
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
    },
    isTypeAdress(object) {
      if (object.type_address.includes("Фактический")) {
        object.physic_address = object.address;
      }
      if (object.type_address.includes("Почтовый")) {
        object.mail_address = object.address;
      }
      if (object.type_address.includes("Юридический")) {
        object.legal_address = object.address;
      }
    },
    addGroupList() {
      const defaultGroupItem = {
        type_address: [],
        legal_address: null,
        physic_address: null,
        mail_address: null,
      };
      this.currentData.addresses.push(defaultGroupItem);
    },
    deleteGroupList() {
      if (this.currentData.addresses.length > 1) {
        this.currentData.addresses.pop();
      }
    },
  },
  computed: {
    isValidAllAddress() {
      let is_main_address = false;
      let is_legal_address = false;

      for (const address of this.currentData.addresses) {
        console.log(address);
        const type_address = address?.type_address;
        is_legal_address = type_address.indexOf("Юридический") >= 0 || is_legal_address;
        is_main_address = type_address.indexOf("Почтовый") >= 0 || is_main_address;
        console.log(`is_legal_address=${is_legal_address} is_main_address=${is_main_address}`);
      }
      console.log("is_legal_address && is_main_address", is_legal_address, is_main_address);
      return is_legal_address && is_main_address;
    }
  },
  components: { LineStep, AddressInput },
};
</script>

<style>
.auth_form_bth {
  font-size: 14px;
  border-radius: 8px;
}

.checkboxs label {
  color: #323E48 !important;
}

.form_block {}

.form_block_delete_link_delete {
  opacity: 0;
  cursor: default !important;
}

div[role="combobox"] .v-label {

  color: #b6b4b4 !important;

}

.error_message {
  color: red;
  font-family: Roboto;
  margin-left: 10px;
  margin-top: 10px;
  font-size: 12px !important;
}

.add_form {
  padding: 25px 15px !important;
  border-radius: 8px;
  font-family: Roboto;
  font-weight: 500;
  box-shadow: none;
  color: #5b656d !important;
  text-transform: capitalize;
}

.form_block_delete_link {
  font-size: 14px;
  font-weight: 500;
  color: #8e909b !important;
}

.form_block_delete_link:active {
  filter: invert(16%) sepia(98%) saturate(3234%) hue-rotate(321deg) brightness(82%) contrast(102%);
}

.form_block_delete_link_active {
  /* filter: invert(16%) sepia(98%) saturate(3234%) hue-rotate(321deg) brightness(82%) contrast(102%); */
}
</style>