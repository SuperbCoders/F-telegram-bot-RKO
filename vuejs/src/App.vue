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

<style scoped>
@font-face {
  font-family: "Montserrat";
  src: url("./assets/font/Montserrat-VariableFont_wght.ttf");
}
html,
body,
#base {
  font-family: Montserrat;
  padding: 20px;
}
</style>
