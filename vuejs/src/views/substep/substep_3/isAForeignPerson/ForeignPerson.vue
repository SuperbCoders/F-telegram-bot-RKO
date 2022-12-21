<template>
  <div class="foreign_person_section">
    <div class="form_block">
      <p class="form_block_label">
        Является ли лицо иностранным публичным должностным лицом либо лицом, связанным с таковым родственными,
        партнерскими или иными отношениями?
      </p>
      <RadioGroup @isStatus="(status) => isForegn = status" name="foreign_person_section" />
    </div>

    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect">
      Продолжить
    </v-btn>
  </div>
</template>

<script>
import RadioGroup from '@/components/radioButton/radioGroup/radioGroup.vue';

export default {
  data() {
    return {
      currentData: {
        is_person_a_foreign_public: '',
      },
      isForegn: false
    }
  },
  components: { RadioGroup },
  methods: {
    redirect() {
      this.currentData.is_person_a_foreign_public = this.isForegn ? 'Да' : 'Нет'

      this.$store.commit("setPersone", { key: "substep_3", value: this.currentData });

      if (this.currentData.is_person_a_foreign_public === 'Да') {
        this.$router.push({ name: "substep_4" });
      } else {
        this.$router.push({ name: "substep_5" });
      }


    }
  },
}
</script>

<style>

</style>