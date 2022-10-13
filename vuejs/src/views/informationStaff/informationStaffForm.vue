<template>
  <div class="imformation_staff_section">
    <h2 class="text-left mb-10 font-bold w-50">
      Группа взаимосвязанных компаний
    </h2>
    <div class="form_block">
      <p class="text-left form_block_title">Название группы компаний</p>
      <v-text-field
        id="oldName"
        placeholder="Напишите назание"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">Дата начала действия</p>
      <v-menu
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            placeholder="xx.xx.xxxx"
            id="passportIssueDate"
            name="passportIssueDate"
            outlined
            append-icon="mdi-calendar-blank"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker @input="passportIssueDateMenu = false"></v-date-picker>
      </v-menu>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Дата окончания действия</p>
      <v-menu
        v-model="passportIssueDateMenu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            placeholder="xx.xx.xxxx"
            id="passportIssueDate"
            name="passportIssueDate"
            append-icon="mdi-calendar-blank"
            outlined
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker @input="passportIssueDateMenu = false"></v-date-picker>
      </v-menu>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.w-50 {
  width: 50%;
}
</style>