<template>
  <div class="structure_form">
    <h2 class="text-left mb-10">Структура органов управления</h2>
    <div class="form_block mt-5">
      <p class="text-left">Выберите из списка</p>
      <v-combobox
        filled
        outlined
        placeholder="Выберите из списка"
        :items="availableCities"
      ></v-combobox>
    </div>
    <default-input />
    <div class="form_block mt-5">
      <p class="text-left">Руководитель</p>
      <v-combobox
        filled
        outlined
        placeholder="Тип"
        :items="availableCities"
      ></v-combobox>
    </div>
    <div class="form_block mt-5">
      <p class="text-left">ИНН</p>
      <v-text-field
        v-model="formData['oldName']"
        id="oldName"
        placeholder="Введите ИНН или название компании"
        class="align-center border-none"
        name="oldName"
        outlined
        :error-messages="formErrors['oldName']"
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5">Наличие наблюдательного совета</p>
      <v-btn-toggle
        active-class
        color="pink darken-1"
        class="d-flex align-start"
        v-model="toggle_exclusive"
      >
        <v-btn class="d-flex align-center">
          <p class="pl-5 pr-5 mb-0">Да</p>
        </v-btn>
        <v-btn>
          <p class="pl-5 pr-5 mb-0">Нет</p>
        </v-btn>
      </v-btn-toggle>
    </div>
    <div class="form_block mt-5">
      <p class="text-left">Наименования наблюдательного совета</p>
      <v-text-field
        v-model="formData['oldName']"
        id="oldName"
        append-icon="mdi-map-marker"
        placeholder="Адрес"
        class="align-center border-none"
        name="oldName"
        outlined
        :error-messages="formErrors['oldName']"
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5">Наличие коллегиального исполнительног органа</p>
      <v-btn-toggle
        active-class
        color="pink darken-1"
        class="d-flex align-start"
        v-model="toggle_exclusive"
      >
        <v-btn class="d-flex align-center">
          <p class="pl-5 pr-5 mb-0">Да</p>
        </v-btn>
        <v-btn>
          <p class="pl-5 pr-5 mb-0">Нет</p>
        </v-btn>
      </v-btn-toggle>
    </div>
    <div class="form_block mt-5">
      <p class="text-left">Наименование коллегиального исполнительног органа</p>
      <v-text-field
        v-model="formData['oldName']"
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        outlined
        :error-messages="formErrors['oldName']"
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block mt-5">
      <p class="text-left">Члены коллегиального исполнительного органа</p>
      <v-text-field
        v-model="formData['oldName']"
        id="oldName"
        placeholder="Укажите ФИЗ"
        class="align-center border-none"
        name="oldName"
        outlined
        :error-messages="formErrors['oldName']"
        :required="true"
      ></v-text-field>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style>
</style>