<template>
  <div>
    <v-btn large class="w-100 block attach_button" block>
      <v-icon class="attach_button_" color="grey darken-1">
        mdi-attachment
      </v-icon>
      <span class="pl-2">
        {{ text }}
      </span>
    </v-btn>
    <input class="attach_upload_input" @click="udpateFile" value="" :placeholder="eaaggn" type="file">
  </div>
</template>

<script>
export default {
  props: {
    text: String,
  },
  methods: {
    udpateFile () {
      const fileList = document.querySelector('attach_upload_input')
      console.log(fileList)
    }
  }
};
</script>

<style scoped>
.attach_upload_input::-webkit-file-upload-button {
  visibility: hidden;
  font-family: Roboto;
  color: #5B656D !important;
}
.attach_upload_input {
  width: 100%;
  height: 50px;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #F3F4F4;
  margin: 0;
  padding: 0;
}
.attach_button {
  box-shadow: none;
  font-family: Roboto;
  color: #5B656D !important;
  padding: 20px 10px;
  text-transform: none;
}

.attach_button_ {
  transform: rotateZ(-45deg);
}
</style>