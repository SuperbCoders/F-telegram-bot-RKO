<template>
  <div class="document_section">
    <h2 class="text-left mb-10">Документы</h2>
    <p class="subtitle text-left document_section_text mb-5">
      Сведения о лицензии на право осуществления деятельности
    </p>
    <AttachButton class="mb-5" text="Загрузить документ" />
    <v-btn
      block
      large
      :disabled="!valid"
      class="mt-10 auth_form_bth"
      color="primary"
      @click="redirect()"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import AttachButton from "../../components/button/attachButton.vue";

export default {
  components: { AttachButton },
  methods: {
    redirect () {
      this.$router.push('/client-info')
    }
  }
  };
</script>

<style scoped>
.document_section_text {
  font-family: Roboto;
  font-size: 18px;
}
</style>