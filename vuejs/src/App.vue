<template>
  <v-app id="base">
      <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({}),

  mounted: function () {},

  watch: {},

  computed: {
    layout() {
      return this.$route.meta.layout || 'default-layout'
    },
  },

  methods: {},
};
</script>

<style>
@import url('./assets/font/Geometria/stylesheet.css');
@font-face {
  font-family: "Montserrat";
  src: url("./assets/font/Montserrat/Montserrat-VariableFont_wght.ttf");
}
@font-face {
  font-family: face;
  src: url('./assets/font/Roboto/Roboto-Regular.ttf')
}
html,
body,
#base {
  padding: 10px;
  min-height: 0 !important;
}
* {
  font-family: 'Roboto' !important;
}
.v-application--wrap {
  min-height: 0 !important;
}
fieldset{
  border: 1px solid #D6D8DA !important;
  border-radius: 8px;
  background: none;
}
.v-input__slot {
  font-family: face;
  border-radius: 8px !important;
  font-weight: 400 !important;
  background: none !important;
}
input, p, label, .v-list-item__title, .v-select__selection, .v-label {
  font-size: 14px !important;
  font-family: 'Roboto' !important;
}
.v-btn {
  letter-spacing: none;
}
.v-label {
  color: #b6b4b4 !important;
}

/* button {
  font-family: Roboto;
} */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
.v-btn__content {
  font-family: 'Roboto' !important;
  font-weight: 500 !important;
  font-size: 14px !important;
  line-height: 22px !important;
}
</style>
