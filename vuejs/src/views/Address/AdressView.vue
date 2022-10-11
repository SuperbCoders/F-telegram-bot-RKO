<template>
  <div class="address_form">
    <h1 class="display-1 text-left mb-10">Адрес</h1>
    <!-- <defalt-input v-model="formData['oldName']" /> -->
    <div class="form_block mt-5">
      <p class="text-left">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="ООО Ромашка"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <default-input />
    <div class="form_block mt-5">
      <p class="text-left">Тип</p>
      <v-combobox
        filled
        outlined
        placeholder="Тип"
        :items="availableCities"
      ></v-combobox>
    </div>
    <div class="form_block mt-5">
      <p class="text-left">Основания</p>
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
      <p class="text-left mb-5">Основания</p>
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
      <p class="text-left">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="Адрес"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5">Основания</p>
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
      <p class="text-left">Адрес</p>
      <v-text-field
        id="oldName"
        placeholder="Адрес"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
    data () {
        return {
            
        }
    }
};
</script>

<style>
</style>