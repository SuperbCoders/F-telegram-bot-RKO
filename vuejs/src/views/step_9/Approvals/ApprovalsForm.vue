<template>
  <div class="approvals_section">
    <div class="form_block">
      <p class="form_block_title">Отметьте все верные утверждения</p>
      <div class="form_block checkboxs">
        <v-checkbox v-for="(item, index) in list" :key="index" class="d-flex align-items-start"
          v-model="currentData.informationGoals" :value="item.value" hide-details>
          <template v-slot:label>
            <div :class="{
              toggleText: !currentData.informationGoals.includes(item.value),
            }">
              {{ item.value }}
            </div>
          </template>
        </v-checkbox>
      </div>
    </div>
    <LineStep :step="8" class="mt-5" />
    <v-btn block large :disabled="!isList" @click="redirect()" class="mt-10 auth_form_bth" color="primary">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "@/components/line_step/line_step.vue";
export default {
  components: {
    LineStep,
  },
  data() {
    return {
      currentData: {
        informationGoals: [],

      },
      list: [
        {
          id: 1,
          value:
            "Компания является Финансовым институтом в соответствии с Законом США «О налогообложении иностранных счетов» (FATCA) и/или главой 20.1 Налогового кодекса РФ",
        },
        {
          id: 2,
          value:
            "Компания, выгодоприобретатель или бенефициар компании является налоговым резидентом США",
        },
        {
          id: 3,
          value:
            "Компания является хозяйственным обществом, имеющим стратегическое значение для оборонно-промышленного комплекса и безопасности РФ либо обществом, находящимся под его прямым или косвенным контролем, которые указаны в Федеральном законе от 27.07.2014 N 213-Ф3",
        },
        {
          id: 4,
          value:
            "Компания осуществляет виды деятельности, которые могут иметь стратегическое значение для оборонно промышленного комплекса и безопасности РФ",
        },
        {
          id: 5,
          value:
            "Компания не относиться к указанным в настоящем пункте юридическим лицам",
        },
      ],
    };
  },
  methods: {
    redirect() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_10',
        value: this.currentData
      })
      this.next();
    },
    toggleText(e) {
      e.preventDefault();
    },
    next() {
      this.$router.push({name: "step_10"});
    }
  },
  computed: {
    isList() {
      if (this.currentData.informationGoals.length >= 1) {
        return true;
      }
      return false;
    },
  },
};
</script>

<style>
.v-input__slot {
  display: flex;
  align-items: flex-start;
}

.toggleText {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.checkboxs label {
  color: #323E48 !important;
}
</style>