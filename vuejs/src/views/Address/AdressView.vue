<template>
  <div class="address_form">
    <h2 class="text-left mb-10 font-weight-bold">Адрес</h2>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Адрес</p>
      <v-text-field id="oldName" placeholder="ООО Ромашка" class="align-center border-none address_form_input"
        name="oldName" outlined :required="true"></v-text-field>
    </div>
    <default-input />
    <div class="form_block">
      <p class="text-left form_block_title">Тип</p>
      <v-combobox filled outlined class="default_select" placeholder="Тип" :items="availableCities"></v-combobox>
    </div>
    <div class="form_block">
      <p class="text-left form_block_label">Основания</p>
      <v-text-field id="oldName" placeholder="ООО Ромашка" class="align-center border-none" name="oldName" outlined
        :required="true"></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5 form_group_label form_block_title">
        Фактический и юридический
        адреса совпадают?
      </p>
      <v-btn-toggle active-class color="pink darken-1" class="d-flex align-start form_block_radio"
        v-model="toggle_exclusive">
        <v-btn class="d-flex align-center">
          <p class="pl-5 pr-5 mb-0">Да</p>
        </v-btn>

        <v-btn>
          <p class="pl-5 pr-5 mb-0">Нет</p>
        </v-btn>
      </v-btn-toggle>
    </div>
    <div class="form_block mt-5">
      <p class="text-left form_group_label">Адрес</p>
      <v-text-field id="oldName" placeholder="Адрес" class="align-center form_block_input border-none" name="oldName"
        outlined :required="true"></v-text-field>
    </div>
    <div class="form_group">
      <p class="text-left mb-5 form_group_label ">Фактический и юридический адреса совпадают?</p>
      <v-btn-toggle active-class color="pink darken-1" class="d-flex align-start form_block_radio"
        v-model="toggle_exclusive">
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
      <v-text-field id="oldName" placeholder="Адрес" class="align-center border-none" name="oldName" outlined
        :required="true"></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
    }
  }
};
</script>

<style scoped>
.default_select {
  background: none !important;
}

.form_group {
  font-family: face;
}

.form_block_input .form_block {
  font-family: fade;
}

.form_block_title {
  font-size: 12px;
  font-family: face;
  color:#8E909B;
}

.form_block_radio {
  border-radius: 10px;
  font-family: face;
}

.form_group_label {
  width: 60%;
  font-size: 14px;
  color:#8E909B;
  font-weight: 500;
}

.form_block_label {
  font-family: face;
  font-size: 12px;
}
</style>