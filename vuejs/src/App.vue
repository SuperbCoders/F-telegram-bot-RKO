<template>
  <v-app id="base">
    <v-main>
      <router-view></router-view>
    </v-main>
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
@font-face {
  font-family: "Montserrat";
  src: url("./assets/font/Montserrat/Montserrat-VariableFont_wght.ttf");
}
@font-face {
  font-family: 'Geometria';
  src: url('./assets/font/Geometria/geometria_light.otf');
}
html,
body,
#base {
  font-family: Geometria;
}
fieldset{
  border: 1px solid #D6D8DA !important;
  border-radius: 8px;
}
</style>
