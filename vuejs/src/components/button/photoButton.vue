<template>
    <v-btn large class="w-100 block photo_button" block>
      <v-icon class="photo_button_" color="grey darken-1">
        mdi-camera-outline
      </v-icon>
      <span class="pl-2">
        {{ text }}
      </span>
    </v-btn>
  </template>

  <script>
  export default {
    props: {
      text: String,
    },
  };
  </script>

  <style scoped>
  .photo_button {
    padding: 20px 10px;
    font-family: Roboto;
    font-weight: 500;
    color: #5B656D !important;
    text-transform: none;
  }
  </style>