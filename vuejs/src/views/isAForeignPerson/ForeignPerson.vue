<template>
  <div class="foreign_person_section">
    <div class="form_block">
        <p class="form_block_label">
            Является ли лицо иностранно публичным должностным лицом либо лицом, связанным с таком родственным
            партнеским или иными отношениями
        </p>
        <RadioGroup @isStatus="(status) => test = status " name="foreign_person_section" />
    </div>
    <line-step :step='5' class="mt-5" />
    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect">Продолжить
    </v-btn>
  </div>
</template>

<script>
import RadioGroup from '../../components/radioButton/radioGroup/radioGroup.vue';
import LineStep from '../../components/line_step/line_step.vue';

export default {
    data () {
      return {
        test: true
      }
    },
    components: { RadioGroup, LineStep },
    methods: {
      redirect () {
        this.$store.commit('isForeginStatus', this.test)
        this.$router.push('/kinship-status-forms')
      }
    },
}
</script>

<style>

</style>