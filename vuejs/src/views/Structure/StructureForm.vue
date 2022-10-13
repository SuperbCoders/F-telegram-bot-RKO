<template>
  <div class="structure_form">
    <h2 class="text-left mb-10 font-bold">Структура органов управления</h2>
    <div class="form_block">
      <p class="text-left form_block_title">Выберите из списка</p>
      <v-combobox
        filled
        outlined
        placeholder="Выберите из списка"
      ></v-combobox>
    </div>
    <default-input />
    <div class="form_block">
      <p class="text-left form_block_title">Руководитель</p>
      <v-combobox
        filled
        outlined
        placeholder="Тип"
      ></v-combobox>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">ИНН</p>
      <v-text-field
        id="oldName"
        placeholder="Введите ИНН или название компании"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5 form_block_label">Наличие наблюдательного совета</p>
      <RadioGroup />
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Наименования наблюдательного совета</p>
      <v-text-field
        id="oldName"
        placeholder="Наименования"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left form_block_title mb-5">Наличие коллегиального исполнительного органа</p>
      <RadioGroup />
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Наименование коллегиального исполнительног органа</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Члены коллегиального исполнительного органа</p>
      <v-text-field
        id="oldName"
        placeholder="Укажите Физ лицо"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <v-btn block large class="mt-10 auth_form_bth" color="primary">
      <router-link class="auth_form_bth color-white text-decoration-none" to="/information-staff"> Продолжить </router-link>
    </v-btn>
  </div>
</template>
<script>
import RadioGroup from '../../components/radioButton/radioGroup/radioGroup.vue';
export default { components: { RadioGroup } };
</script>

<style>
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
.auth_form_bth {
  border-radius: 10px;
  color: white !important;
  text-transform: capitalize;
  font-size: 14px;
}
</style>