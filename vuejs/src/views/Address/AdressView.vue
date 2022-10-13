<template>
  <div class="address_form">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h2 class="text-left mb-5 font-weight-bold">Адрес</h2>
      <div class="form_block mt-2">
        <p class="text-left form_block_title">Адрес</p>
        <v-text-field
          id="oldName"
          placeholder="ООО Ромашка"
          class="align-center border-none address_form_input"
          name="oldName"
          :rules="requiredRules"
          outlined
          :required="true"
        ></v-text-field>
      </div>
      <default-input />
      <div class="form_block">
        <p class="text-left form_block_title">Тип</p>
        <v-combobox
          filled
          outlined
          :rules="requiredRules"
          :required="true"
          class="default_select"
          placeholder="Тип"
          :items="availableCities"
        ></v-combobox>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Основания</p>
        <v-text-field
          id="oldName"
          placeholder="ООО Ромашка"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left mb-5 form_group_label form_block_title">
          Фактический и юридический адреса совпадают?
        </p>
        <RadioGroup @isStatus="isActualAdressShow" name="ActualAndLegalAddress" />
      </div>
      <div v-if="!addressActualShow" class="form_block mt-5">
        <p class="text-left form_block_title">Адрес</p>
        <v-text-field
          id="oldName"
          placeholder="Адрес"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
      <div class="form_group">
        <p class="text-left mb-5 mt-10 form_group_label form_block_title">
          Фактический и почтовый адрес совпадают?
        </p>
        <RadioGroup @isStatus="isActualEmailShow" name="Actualandpostaladdress" />
      </div>
      <div v-if="!emailActualShow" class="form_block mt-5">
        <p class="text-left form_block_title">Адрес</p>
        <v-text-field
          id="oldName"
          placeholder="Адрес"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
    </v-form>
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="validate"
      >Продолжить</v-btn
    >
  </div>
</template>

<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";

export default {
  data() {
    return {
      valid: false,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
      addressActualShow: false,
      emailActualShow: false
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$router.push("/sctructure");
      }
    },
    isActualAdressShow (e) {
      this.addressActualShow = e
    },
    isActualEmailShow (e) {
      this.emailActualShow = e
    }
  },
  components: { RadioGroup },
};
</script>

<style scoped>
.default_select {
  background: none !important;
}
.form_radio_btn {
  display: flex;
  font-family: Roboto;
}
.auth_form_bth {
  color: white;
  border-radius: 10px;
  text-transform: capitalize;
  font-size: 14px;
}
.form_radio_btn input {
  display: none;
}
.auth_form_bth {
  border-radius: 10px;
  text-transform: capitalize;
  font-size: 14px;
}
.form_group {
  font-family: face;
}
.form_block_input .form_block {
  font-family: Roboto;
  border-radius: 8px;
  background: none;
}

.form_block_title {
  font-size: 12px;
  font-family: Roboto;
  color: #8e909b;
}

.form_block_radio {
  border-radius: 10px;
  font-family: face;
}

.form_group_label {
  width: 80%;
  color: #323e48;
  font-size: 14px;
  font-weight: 500;
}

.form_block_label {
  font-family: face;
  font-size: 12px;
}
</style>