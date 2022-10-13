<template>
  <div class="document_section">
    <h2 class="text-left mb-10 ">Документы</h2>
    <p class="subtitle text-left document_section_text mb-5">
      Сведения о лицензии на право осуществления деятельности
    </p>
    <AttachButton class="mb-5 " text="Выбрать файл" />
    <PhotoButton text="Сфотографировать" />
  </div>
</template>

<script>
import AttachButton from '../../components/button/attachButton.vue';
import PhotoButton from '../../components/button/photoButton.vue';
export default { components: { AttachButton, PhotoButton } };
</script>

<style scoped>
.document_section_text {
    font-family: Roboto;
    font-size: 18px;
}
</style>