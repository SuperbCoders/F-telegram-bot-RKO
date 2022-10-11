<template>
  <div class="auth_section">
    <div class="auth_logo_block">
      <img src="@/assets/images/logo.png" alt="">
    </div>
    <div class="auth_title_block">
      <h2 class="auth_title font-weight-bold">Заявка на открытие рассчетного счета</h2>
    </div>
    <div class="auth_form mt-12">
      <v-text-field
          label="Введите ИНН"
          outlined
          class="mt-2 auth_form"
        ></v-text-field>
        <v-text-field
          label="Наименования компании"
          outlined
          class="mt-2 auth_form"
        ></v-text-field>
        <v-text-field
          label="Контактный номер телефона"
          outlined
          class="mt-2 auth_form"
        ></v-text-field>
        <div class="auth_form_cheked_block d-flex w-100">
          <v-checkbox v-model="checkbox">
      <template v-slot:label>
        <div class="text-left">
          <span>Я ознакомился и согласен с условиями</span>
          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <a
                target="_blank"
                class="text-decoration-none"
                href="https://vuetifyjs.com"
                @click.stop
                v-on="on"
              >
                резервирного счета,
              </a>
            </template>
          </v-tooltip>
          а также с условиями
          <a
            target="_blank"
            class="text-decoration-none"
                href="https://vuetifyjs.com"
                @click.stop
                v-on="on"
              >
                обработки и хранения персональных данных
              </a>
        </div>
      </template>
    </v-checkbox>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.auth_section {
  margin: 30px 20px;
}
.auth_title_block {
  margin-top: 30px;
}
.auth_title {

}
.auth_form {
  border-radius: 8px;
}
</style>