<template>
  <v-navigation-drawer
    v-model="drawer"
    :clipped="$vuetify.breakpoint.lgAndUp"
    app
  >
    <p>Сань, верни сотку</p>
    <v-list nav>
      <template v-for="(item, index) in items">
        <v-list-item
          class="mb-n2"
          v-if="item.heading"
          :key="`${item.text}${index}`"
        >
          <v-list-item-content>
            <v-list-item-title class="title">{{
              item.heading
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider class="mt-2" v-else-if="item.divider" :key="index" />
        <v-list-item
          class="mt-0 mb-0"
          v-else
          :key="`${item.text}${index}`"
          link
          :to="{ name: item.routeName, params: item.routeParams }"
          color="primary"
        >
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Drawer',

  data: () => ({
  }),

  computed: {
    drawer: {
      get() {
        return this.$store.state.drawer
      },
      set(value) {
        this.$store.commit('toggleDrawer', value)
      }
    },
    items: function () {
      const items = [
        { heading: "Empty" },
        { divider: true },
      ]
      return items
    },
  }

};
</script>
