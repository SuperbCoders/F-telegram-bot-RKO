<template>
  <v-app-bar
    :clipped-left="$vuetify.breakpoint.lgAndUp"
    app
    color="primary"
    dark
  >
    фцвфцвфцвфцвфцвцф
    <v-toolbar-title style="width: 300px" class="toolbar-title ml-0 pl-4">{{
      title
    }}</v-toolbar-title>
    <v-spacer />
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppBar',

  props: {
    isDrawerHidden: Boolean,
    isAuthenticated: Boolean,
  },

  computed: {
    title: function () {
      return "Loan Application"
    }
  },

  methods: {
  }
};
</script>

<style lang="scss">
</style>
