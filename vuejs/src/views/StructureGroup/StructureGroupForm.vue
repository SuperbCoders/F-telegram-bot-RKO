<template>
  <div class="structure_group_section">
    <h3 class="text-left structure_group_title mb-10">Состав группы компаний</h3>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div
        v-for="(itemForm, index) in groupList"
        :key="index"
        class="form_input_block"
      >
        <div class="form_block">
          <p class="text-left form_block_title">Название компании</p>
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
        <div class="form_block">
          <p class="text-left form_block_title">ИНН</p>
          <v-text-field
            id="oldName"
            placeholder="ИНН"
            class="align-center border-none"
            name="oldName"
            v-mask="'### ### ### ###'"
            masked="true"
            v-model="itemForm.inn"
            outlined
            :rules="innRules"
            :required="true"
          ></v-text-field>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">ОГРН</p>
          <v-text-field
            id="oldName"
            placeholder="ОГРН"
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
        <a @click="deleteGroupList" class="form_block_delete_link text-decoration-none" href="#">
          <v-icon>mdi-trash-can-outline</v-icon>
          Удалить
        </a>
        <v-btn
          class="
            text-center
            d-flex

            align-center
            justify-center
            ml-10
            add_form
          "
          @click="addGroupList()"
        >
          <span class="pr-3">Добавить</span>
          <v-icon>mdi-plus-circle-outline</v-icon>
        </v-btn>

      </div>
      <LineStep step="4" />
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
import LineStep from '../../components/line_step/line_step.vue';
import { mask } from "vue-the-mask";

export default {
  directives: { mask },
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
      innRules: [
      (v) => !!v || "Это поле обязательно",
      (v) => (v && v.length >= 10)  || "ИНН не может содержать меньше 10 симоволов",
      ],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate()) {
        this.$router.push('/credit-page')
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
  components: {
    LineStep,
  }
};
</script>

<style>
.auth_form_bth {
  font-size: 14px;
  border-radius: 8px;
}
.form_block {

}
.add_form {
  padding: 25px 15px !important;
  border-radius: 8px;
  font-family: Roboto;
  font-weight: 500;
  box-shadow: none;
  color: #5B656D !important;
  text-transform: capitalize;
}
.form_block_delete_link {
  font-size: 14px;
  font-weight: 500;
  color: #8E909B !important;
}

</style>