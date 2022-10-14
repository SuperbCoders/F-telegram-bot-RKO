<template>
  <div class="beneficiaries_section">
    <h3 class="form_block_label">Выгодоприобретатели</h3>
    <div class="form_block">
      <p class="form_block_title">Имеються ли Выгодоприобретатели</p>
      <v-radio-group mandatory v-model="isShow" column>
        <v-radio label="Отсуствуют" value="Отсуствуют"></v-radio>
        <v-radio label="Имеются" value="Имеются"></v-radio>
      </v-radio-group>
    </div>
    <v-btn
      block
      large
      class="mt-10 auth_form_bth"
      color="primary"
      @click="redirect"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
     isShow: false
    };
  },
  methods: {
    redirect () {
        this.$router.push('/purposes')
    }
  }
};
</script>

<style>
</style>