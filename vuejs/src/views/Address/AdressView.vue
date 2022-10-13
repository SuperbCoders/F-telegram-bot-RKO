<template>
  <div class="address_form">
    <h2 class="text-left mb-5 font-weight-bold">Адрес</h2>
    <div class="form_block mt-2">
      <p class="text-left form_block_title">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="ООО Ромашка"
        class="align-center border-none address_form_input"
        name="oldName"
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
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5 form_group_label form_block_title">
        Фактический и юридический адреса совпадают?
      </p>
      <RadioGroup />
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="Адрес"
        class="align-center form_block_input border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5 form_group_label form_block_title">
        Фактический и почтовый адрес совпадают?
      </p>
      <RadioGroup />
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="Адрес"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <v-btn block large class="mt-10 auth_form_bth" color="primary">
      <router-link class="auth_form_bth color-white text-decoration-none" to="/sctructure"> Продолжить </router-link>
    </v-btn>
  </div>
</template>

<script>
import RadioGroup from "../../components/radioButton/radioGroup/radioGroup.vue";
export default {
  data() {
    return {};
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