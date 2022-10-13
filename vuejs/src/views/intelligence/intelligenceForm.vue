<template>
  <div class="intelligence_section">
    <h2 class="text-left mb-10">Сведенья о персонале</h2>
    <div class="form_block mt-5">
      <p class="text-left form_block_title">Численность персонала</p>
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
      <p class="text-left form_block_input">Задолжность по зп</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none form_block_input"
        name="oldName"
        type="number"
        append-icon="mdi-currency-rub"
        outlined
        :required="true"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      test: false
    }
  }
}
</script>

<style>
.form_block_input {
  font-family: face;
  color: #8E909B;
  font-size: 13px;
}
.form_block_title {
  font-size: 13px;
  font-family: face;
  color: #8E909B;
}
</style>