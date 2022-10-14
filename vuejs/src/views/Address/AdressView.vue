<template>
  <div class="structure_group_section">
    <h2 class="text-left structure_group_title mb-10">Адрес</h2>
    <v-form ref="form" v-model="valid" lazy-validation>
      <div class="form_block mb-5">
        <v-checkbox
          v-model="currentData.typeAddress"
          label="Юридический"
          value="red"
          hide-details
        ></v-checkbox>
        <v-checkbox
          v-model="currentData.typeAddress"
          label="Фактический"
          value="Фактический"
          hide-details
        ></v-checkbox>
        <v-checkbox
          v-model="currentData.typeAddress"
          label="Почтовый"
          value="Почтовый"
          hide-details
        ></v-checkbox>
      </div>
      <p class="error_message" v-if="!valid && checkboxList.length < 1">Выберите пункт</p>
      <div
        v-for="(itemForm, index) in groupList"
        :key="index"
        class="form_input_block"
      >
        <div class="form_block">
          <p class="text-left form_block_title">Адрес</p>
          <v-text-field
            id="oldName"
            placeholder="Напишите адрес"
            class="align-center border-none"
            v-model="currentData.Address"
            name="oldName"
            outlined
            :rules="requiredRules"
            :required="true"
          ></v-text-field>
        </div>
        <div class="form_block">
          <p class="text-left form_block_title">Основание</p>
          <v-combobox
            filled
            outlined
            v-model="currentData.footing"
            :rules="requiredRules"
            placeholder="Выберите основание"
          ></v-combobox>
        </div>
        <!-- <div class="form_block">
        <p class="text-left form_block_title">ИНН</p>
        <v-text-field
          id="oldName"
          placeholder="Введите ИНН или название компании"
          class="align-center border-none"
          name="oldName"
          outlined
          :rules="requiredRules"
          :required="true"
        ></v-text-field>
      </div>
        <div class="form_block">
          <p class="text-left form_block_title">ОГРН</p>
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
        </div> -->
      </div>
      <div class="form_block d-flex align-center justify-center">
        <a
          @click="deleteGroupList"
          class="form_block_delete_link text-decoration-none"
          href="#"
        >
          <v-icon>mdi-trash-can-outline</v-icon>
          Удалить
        </a>
        <v-btn
          class="text-center d-flex align-center justify-center ml-10 add_form"
          @click="addGroupList()"
        >
          <span class="pr-3">Добавить</span>
          <v-icon>mdi-plus-circle-outline</v-icon>
        </v-btn>
      </div>
      <line-step :step='1' />
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
      currentData: {
        typeAddress: null,
        Address: null,
        footing: null
      },
      checkboxList: [],
      valid: true,
      innRules: [
        (v) => !!v || "Это поле обязательно",
        (v) =>
          (v && v.length >= 10) || "ИНН не может содержать меньше 10 симоволов",
        (v) =>
          (v && v.length <= 12) || "ИНН не может содержать больше 12 симоволов",
      ],
      requiredRules: [(v) => !!v || "Это поле обязательно"],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();

      if (this.$refs.form.validate() && this.checkboxList.length > 0) {
        this.$router.push("/sctructure");
        this.$store.commit('')
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
  components: { LineStep },

};
</script>

<style>
.auth_form_bth {
  font-size: 14px;
  border-radius: 8px;
}
.form_block {
}
.error_message {
  color: red;
  font-family: Roboto;
  margin-left: 10px;
  margin-top: 10px;
  font-size: 12px !important;
}
.add_form {
  padding: 25px 15px !important;
  border-radius: 8px;
  font-family: Roboto;
  font-weight: 500;
  box-shadow: none;
  color: #5b656d !important;
  text-transform: capitalize;
}
.form_block_delete_link {
  font-size: 14px;
  font-weight: 500;
  color: #8e909b !important;
}
</style>