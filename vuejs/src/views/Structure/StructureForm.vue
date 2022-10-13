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
      <p class="text-left mb-5 form_block_title">Наличие наблюдательного совета</p>
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
      <p class="text-left form_block_label">Наименования наблюдательного совета</p>
      <v-text-field
        id="oldName"
        append-icon="mdi-map-marker"
        placeholder="Наименования"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left form_block_label mb-5">Наличие коллегиального исполнительного органа</p>
      <v-btn-toggle
        active-class
        color="pink darken-1"
        class="d-flex align-start"
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
      <p class="text-left form_block_label">Наименование коллегиального исполнительног органа</p>
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
      <p class="text-left">Члены коллегиального исполнительного органа</p>
      <v-text-field
        id="oldName"
        placeholder="Укажите Физ лицо"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style>
.form_block {
  font-family: Roboto;
  font-size: 14px;
}
.form_block_title {
  font-size: 12px;
}
.form_block_label {
  font-family: Roboto;
  color: black;
}
</style>