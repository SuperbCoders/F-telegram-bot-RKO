<template>
  <div class="beneficiaries_section">
    <h3 class="form_block_label">Выгодоприобретатели</h3>
    <div class="form_block mt-5">
      <p class="form_block_title">Имеются ли Выгодоприобретатели</p>
      <v-radio-group mandatory v-model="currentData.beneficiaries" column>
        <v-radio label="Отсуствуют" value="Отсуствуют"></v-radio>
        <v-radio label="Имеются" value="Имеются"></v-radio>
      </v-radio-group>
    </div>
    <line-step :step='15' class="mt-5"/>
    <v-btn
      block
      large
      class="mt-10 auth_form_bth"
      color="primary"
      @click="redirect"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from '../../components/line_step/line_step.vue';
export default {
  data() {
    return {
     isShow: false,
     currentData: {
      beneficiaries: null
     }
    };
  },
  methods: {
    redirect () {
      this.$store.dispatch('addObjectFormData', {
          object: 'step_15',
          value: this.currentData
        })
        this.$router.push('/purposes')
    }
  },
  components: {
    LineStep,
  }
};
</script>

<style>
</style>