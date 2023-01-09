<template>
  <div class="beneficiaries_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
    </v-btn>
    <h3 class="form_block_label">Выгодоприобретатели</h3>
    <div class="form_block mt-5 ">
      <p class="form_block_title">Имеются ли Выгодоприобретатели</p>
      <v-radio-group mandatory v-model="currentData.beneficiaries" column class="checkboxs">
        <v-radio label="Отсутствуют" value="Отсутствуют"></v-radio>
        <v-radio label="Имеются" value="Имеются"></v-radio>
      </v-radio-group>
    </div>
    <div class="form_block" v-if="currentData.beneficiaries === 'Имеются'">
      <p class="form_block_title">Укажите третьи лица, к выгоде которых действует компания</p>
      <v-text-field v-model="currentData.third_parties"
        placeholder="Укажите третьи лица, к выгоде которых действует компания" class="align-center border-none mt-5"
        outlined>
      </v-text-field>
    </div>
    <line-step :step='number_step' class="mt-5" />
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '@/components/line_step/line_step.vue';
import { loadCurrentData } from '@/utils/loadStore'

export default {
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      isShow: false,
      currentData: {
        beneficiaries: "",
        third_parties: "",
      }
    };
  },
  mounted() {
    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });
  },
  methods: {
    redirect() {
      this.$store.dispatch('addObjectFormData', {
        object: `step_${this.number_step}`,
        value: this.currentData
      })
      this.next();
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {

      if (this.$store.state.formData.step_1.opf.short !== "ИП") {
        this.$router.push({ name: `step_${this.number_step - 3}` });
      } else {
        this.$router.push({ name: `step_${this.number_step - 1}` });
      }
    },
  },
  components: {
    LineStep,
  }
};
</script>

<style>
.checkboxs label {
  color: #323E48 !important;
}
</style>