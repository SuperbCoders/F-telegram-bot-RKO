<template>
  <button class="default_button">{{ text }}</button>
</template>

<script>
export default {
  props: {
    text: String
  }
}
</script>

<style scoped>
.default_button {
  width: 100%;
  height: 46px;
  color: white;
  background: #D41367;
  border: none;
  border-radius: 8px;
}
.default_button:disabled {
background: #E571A4;
}
</style>