<template>
  <div class="license_information_form">
    <h2 class="form_block_label">Сведения о лицензии</h2>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Вид</p>
      <v-text-field
        id="oldName"
        placeholder="xxxxxx"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Номер</p>
      <v-text-field
        id="oldName"
        placeholder="xxxxxx"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Кем выдан</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">
        Дата выдачи лицензии
      </p>
      <v-menu
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            placeholder="Дата"
            id="passportIssueDate"
            name="passportIssueDate"
            outlined
            append-icon="mdi-calendar-blank"
            readonly
            v-model="dateStarting"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStarting"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div>
    <div class="form_block">
      <p class="text-left form_block_title">
        Срок дей
      </p>
      <v-menu
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            placeholder="Дата"
            id="passportIssueDate"
            name="passportIssueDate"
            outlined
            append-icon="mdi-calendar-blank"
            readonly
            v-model="dateStarting"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStarting"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Срок действия</p>
      <v-menu
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            placeholder="Дата"
            id="passportIssueDate"
            name="passportIssueDate"
            outlined
            append-icon="mdi-calendar-blank"
            readonly
            v-model="dateStarting"
            :rules="requiredRules"
            :required="true"
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStarting"
          @input="passportIssueDateMenu = false"
        ></v-date-picker>
      </v-menu>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Численность персонала</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        :rules="requiredRules"
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
</style>