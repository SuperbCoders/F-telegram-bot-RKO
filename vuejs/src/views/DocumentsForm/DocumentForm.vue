<template>
  <div class="document_form_block">
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block mt-5">
        <p class="text-left form_block_title">ИНН</p>
        <v-text-field id="oldName" placeholder="Введите ИНН" class="align-center border-none" outlined
          :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">СНИЛС (при наличии)</p>
        <v-text-field id="oldName" placeholder="Введите ИНН" class="align-center border-none" outlined
         :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Гражданство</p>
        <v-text-field id="oldName" placeholder="Введите ИНН" class="align-center border-none" outlined
          :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Телефон</p>
        <v-text-field id="oldName" placeholder="Введите ИНН" class="align-center border-none" outlined
          :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <div class="form_block">
        <p class="text-left form_block_title">Доля владения</p>
        <v-text-field id="oldName" placeholder="Введите текст" class="align-center border-none" outlined
          :rules="requiredRules" :required="true">
        </v-text-field>
      </div>
      <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
      </v-btn>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      valid: true,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    }
  },
  methods: {
    validate() {
      this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$router.push("/address");
      }
    },
  },
}
</script>

<style>

</style>