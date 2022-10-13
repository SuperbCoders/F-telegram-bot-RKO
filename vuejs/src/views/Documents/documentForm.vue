<template>
  <div class="document_section">
    <h2 class="text-left mb-10 ">Документы</h2>
    <p class="subtitle text-left document_section_text mb-5">
      Сведения о лицензии на право осуществления деятельности
    </p>
    <AttachButton class="mb-5 " text="Выбрать файл" />
    <PhotoButton text="Сфотографировать" />
    <LineStep :step="6" class="mt-5" />
    <v-btn block large class="mt-10 auth_form_bth" color="primary">
      <router-link class="auth_form_bth color-white text-decoration-none" to="/rate"> Продолжить </router-link>
    </v-btn>
  </div>
</template>

<script>
import AttachButton from '../../components/button/attachButton.vue';
import PhotoButton from '../../components/button/photoButton.vue';
import LineStep from '../../components/line_step/line_step.vue';
export default { components: { AttachButton, PhotoButton, LineStep } };
</script>

<style scoped>
.document_section_text {
    font-family: Roboto;
    font-size: 18px;
}
</style>