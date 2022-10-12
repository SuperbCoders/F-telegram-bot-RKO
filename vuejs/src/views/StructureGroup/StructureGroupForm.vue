<template>
  <div class="structure_group_section">
    <h2 class="text-left mb-10">Структура группы компаний</h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div
        v-for="(itemForm, index) in groupList"
        :key="index"
        class="form_input_block"
      >
        <div class="form_block mt-5">
          <p class="text-left">Название компании</p>
          <v-text-field
            id="oldName"
            placeholder="Наименование"
            class="align-center border-none"
            v-model="itemForm.name"
            name="oldName"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
        <div class="form_block mt-5">
          <p class="text-left">ИНН</p>
          <v-text-field
            id="oldName"
            placeholder="Наименование"
            class="align-center border-none"
            name="oldName"
            v-model="itemForm.inn"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
        <div class="form_block mt-5">
          <p class="text-left">ОГРН</p>
          <v-text-field
            id="oldName"
            placeholder="Наименование"
            class="align-center border-none"
            name="oldName"
            v-model="itemForm.ogrn"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a @click="deleteGroupList" class="text-decoration-none" href="#">
          <v-icon>mdi-trash-can-outline</v-icon>
          Удалить
        </a>
        <v-btn
          class="
            text-center
            d-flex
            align-center
            justify-center
            font-weight-bold
            ml-10
            add_form
          "
          @click="addGroupList()"
        >
          <span class="pr-3">Добавить</span>
          <v-icon>mdi-plus-circle-outline</v-icon>
        </v-btn>
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
</template>

<script>
export default {
  data() {
    return {
      groupList: [
        {
          name: null,
          inn: null,
          ogrn: null,
        },
      ],
      defaultGroupItem: {
        name: null,
        inn: null,
        ogrn: null,
      },
      valid: true,
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        alert(1);
      }
    },
    addGroupList() {
      this.groupList.push(this.defaultGroupItem);
    },
    deleteGroupList() {
      if (this.groupList.length > 1) {
        this.groupList.pop();
      }
    },
  },
};
</script>

<style>
.add_form {
  padding: 15px 15px !important;
  border-radius: 8px;
  text-transform: capitalize;
}
</style>