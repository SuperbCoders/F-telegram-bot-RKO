<template>
  <div class="document_section">
    <p class="subtitle text-left document_section_text mb-5">
      Загрузить первую страницу паспорта
    </p>

    <div v-if="files" class="list_file">
      <div v-for="(file, index) in files" :key="index" class="block_file">
        <div class="card_file">
          <div class="type_file">{{ getType(file.type) }}</div>
          <div class="size_file">{{ getSize(file.size) }} Мб</div>
        </div>
        <div class="name_file">{{ file.name }}</div>
      </div>
    </div>

    <AttachButton class="mb-5 " text="Загрузить документ" @file="onfile" />

    <LineStep :step="9" class="mt-5" />

    <v-btn
      block
      large
      class="mt-10 auth_form_bth"
      color="primary"
      @click="redirect()"
      >Продолжить
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
    },
    getType(type) {
      type = type.split('/')[1];
      return type;
    },
    getSize(size) {
      size = ""+size;
      return size[0] + size[1];
    },
    getName(name) {
      return name;
    },
    redirect () {
      this.$router.push('/client-info')
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
  text-transform: uppercase;
}
.name_file {
  margin-top: 5px;
  margin-bottom: 10px;
  font-size: 12px;
  width: 60px;
  overflow-x: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.document_section_text {
  font-family: Roboto;
  font-size: 18px;
}
</style>