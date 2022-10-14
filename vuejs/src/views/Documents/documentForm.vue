<template>
  <div class="document_section">
    <h2 class="text-left mb-10 ">Документы</h2>
    <p class="subtitle text-left document_section_text mb-5">
      Сведения о лицензии на право осуществления деятельности
    </p>

    <div v-if="files" class="list_file">
      <div v-for="(file, index) in files" :key="index" class="block_file">
        <div class="card_file">
          <div class="type_file">PDF</div>
          <div class="size_file">12 Мб</div>
        </div>
        <div class="name_file">Test</div>
        <!-- {{ file.name }}
        {{ file.type }}
        {{ file.size }} -->
      </div>
    </div>

    <AttachButton class="mb-5 " text="Загрузить документ" @file="onfile" />

    <LineStep :step="6" class="mt-5" />

    <v-btn block large class="mt-10 auth_form_bth" color="primary">
      <router-link class="auth_form_bth color-white text-decoration-none" to="/rate"> Продолжить </router-link>
    </v-btn>
  </div>
</template>

<script>
import AttachButton from '../../components/button/attachButton.vue';
import LineStep from '../../components/line_step/line_step.vue';

export default {
  data(){
    return {
      files: null,
    }
  },
  methods: {
    onfile(files) {
      console.log(files);
      this.files = files;
    }
  },
  components: { AttachButton, LineStep }
};

</script>

<style scoped>
.list_file {
  display: flex;
}
.card_file{
  background: #F3F4F4;
  padding: 10px 14px;
  border-radius: 6px;
}
.size_file {
  text-align: center;
  font-size: 12px;
}
.type_file {
  font-size: 20px;
  font-weight: bold;
  color: #D41367;
  text-align: center;
}
.name_file {
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 12px;
}
.document_section_text {
    font-family: Roboto;
    font-size: 18px;
}
</style>