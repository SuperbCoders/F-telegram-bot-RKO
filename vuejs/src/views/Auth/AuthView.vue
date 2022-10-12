<template>
  <div class="auth_section">
    <div class="auth_logo_block">
      <img src="@/assets/images/logo.png" alt="" />
    </div>
    <div class="auth_title_block">
      <h2 class="auth_title font-weight-bold">
        Заявка на открытие рассчетного счета
      </h2>
    </div>
    <div class="auth_form mt-12">
      <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        label="Введите ИНН"
        outlined
        v-model="name"
        :rules="requiredRules"
        required
        class="mt-2 auth_form"
      ></v-text-field>
      <v-text-field
        label="Наименования компании"
        outlined
        v-model="email"
        :rules="requiredRules"
        required
        type="email"
        error-message="true"
        class="mt-2 auth_form"
      ></v-text-field>
      <v-text-field
        label="Контактный номер телефона"
        outlined
        :rules="requiredRules"
        :required="true"
        class="mt-2 auth_form"
      ></v-text-field>
      <div class="auth_form_cheked_block d-flex w-100">
        <v-checkbox :rules="requiredRules" v-model="checkbox">
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
      <v-btn
        block
        large
        :disabled="!valid"
        class="mt-10 auth_form_bth"
        color="primary"
        @click="validate"
        >Продолжить</v-btn
      >
    </v-form>
    </div>
  </div>
</template>

<script>
  export default {
    data: () => ({
      valid: true,
      name: '',
      innRules: [
        v => !!v || 'Name is required'
      ],
      email: '',
      requiredRules: [
        v => !!v || 'Это поле обязательно'
      ],
      nameCompanyRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      numberRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()

        if (this.$refs.form.validate()) {
          alert(1)
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
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
.auth_form_bth {
  border-radius: 10px;
  font-size: 12px;
}
</style>