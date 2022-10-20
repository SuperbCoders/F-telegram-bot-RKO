<template>
  <div class="document_section">
    <p class="subtitle text-left document_section_text mb-5">
      Загрузить первую страницу паспорта
    </p>

    <div v-if="this.currentData.first_passport_page" class="list_file">
      <div
        v-for="(file, index) in this.currentData.first_passport_page"
        :key="index"
        class="block_file"
      >
        <div class="card_file">
          <div class="type_file">{{ getType(file.type) }}</div>
          <div class="size_file">{{ getSize(file.size) }} Мб</div>
        </div>
        <div class="name_file">{{ file.name }}</div>
      </div>
    </div>

    <AttachButton class="mb-5" text="Загрузить документ" @file="onfile" />

    <v-btn
      block
      large
      class="mt-10 auth_form_bth"
      color="primary"
      :disabled="currentData.first_passport_page === null"
      @click="redirect()"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import AttachButton from '../../components/button/attachButton.vue';


export default {
  data() {
    return {
      currentData: {
        first_passport_page: null,
      },
    };
  },
  methods: {
    onfile(files) {
      this.currentData.first_passport_page = files;
    },
    getType(type) {
      type = type.split("/")[1];
      return type;
    },
    getSize(size) {
      size = "" + size;
      return size[0] + size[1];
    },
    getName(name) {
      return name;
    },
    redirect () {

      if(this.$route.query?.type === 'SupervisoryBoard') {
          this.$store.commit("setSupervisoryBoardPersone", {key: "page-7", value: this.currentData});
      }else if(this.$route.query?.type === 'CollegialExecutive') {
        this.$store.commit("setCollegialExecutiveBody", {key: "page-7", value: this.currentData});
      }
      
      this.$router.push({path:"/client-info", query: this.$route.query});
    }
  },
  components: { AttachButton }

};
</script>

<style scoped>
.list_file {
  display: flex;
}
.card_file {
  background: #f3f4f4;
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
  color: #d41367;
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