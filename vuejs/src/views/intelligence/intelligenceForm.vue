<template>
  <div class="intelligence_section">
    <h2 class="text-left mb-10">Сведенья о персонале</h2>
    <div class="form_block mt-5">
      <p class="text-left">Численность персонала</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
        name="oldName"
        outlined
        :required="true"
      ></v-text-field>
    </div>
    <!-- <input type="file" accept="image/*" capture="environment" /> -->
    <div class="form_block mt-5">
      <p class="text-left">Задолжность по зп</p>
      <v-text-field
        id="oldName"
        placeholder="Наименование"
        class="align-center border-none"
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
</style>