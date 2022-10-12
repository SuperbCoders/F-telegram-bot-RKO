<template>
  <div class="address_form">
    <h2 class="text-left mb-10 font-weight-bold">Адрес</h2>
    <div class="form_block mt-5">
      <p class="text-left">Адрес</p>
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
    <div class="form_block mt-5">
      <p class="text-left">Тип</p>
      <v-combobox
        filled
        outlined
        class="default_select"
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

<style scoped>
.default_select {

}
</style>