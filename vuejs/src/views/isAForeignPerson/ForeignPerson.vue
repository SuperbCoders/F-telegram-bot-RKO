<template>
  <div class="foreign_person_section">
    <div class="form_block">
        <p class="form_block_label">
            Является ли лицо иностранно публичным должностным лицом либо лицом, связанным с таком родственным
            партнеским или иными отношениями
        </p>
        <RadioGroup @isStatus="(status) => isForegn = status" name="foreign_person_section" />
    </div>

    <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect">
      Продолжить
    </v-btn>
  </div>
</template>

<script>
import RadioGroup from '../../components/radioButton/radioGroup/radioGroup.vue';

export default {
    data () {
      return {
        currentData: {
          assigned_publ_pers_relation: '',
        },
        isForegn: false
      }
    },
    components: { RadioGroup },
    methods: {
      redirect () {
        this.$store.commit('isForeginStatus')
        if (this.isForegn) {
          this.currentData.assigned_publ_pers_relation = 'Да'
        } else {
          this.currentData.assigned_publ_pers_relation = 'Нет'
        }

        if(this.$route.query?.type === 'SupervisoryBoard') {
          this.$store.commit("setSupervisoryBoardPersone", {key: "page-3", value: this.currentData});
        }else if(this.$route.query?.type === 'CollegialExecutive') {
          this.$store.commit("setCollegialExecutiveBody", {key: "page-3", value: this.currentData});
        }
        this.$router.push({path:"/kinship-status-forms", query: this.$route.query});

      }
    },
}
</script>

<style>

</style>