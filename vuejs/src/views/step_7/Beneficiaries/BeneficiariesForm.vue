<template>
  <div class="beneficiaries_section">
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
        placeholder="Укажите третьи лица, к выгоде которых действует компания" 
        class="align-center border-none mt-5"
        outlined>
      </v-text-field>
    </div>
    <line-step :step='6' class="mt-5" />
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '@/components/line_step/line_step.vue';

export default {
  data() {
    return {
      isShow: false,
      currentData: {
        beneficiaries: null,
        third_parties: null,
      }
    };
  },
  methods: {
    redirect() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_8',
        value: this.currentData
      })
      this.next();
    },
    next() {
      this.$router.push({ name: "step_8" })
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