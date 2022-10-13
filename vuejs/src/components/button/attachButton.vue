<template>
  <v-btn large class="w-100 block attach_button" block>
    <v-icon class="attach_button_" color="grey darken-1">
      mdi-attachment
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