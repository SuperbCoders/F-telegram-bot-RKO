<template>
<v-btn class="w-100" block>
    <v-icon
        class="attach_button"
        color="grey darken-1"
    >
        mdi-attachment
    </v-icon>{{text}}</v-btn>
</template>

<script>
export default {
 props: {
    text: String
 }
}
</script>

<style scoped>
.attach_button {
  transform: rotateZ(-45deg);
}
</style>