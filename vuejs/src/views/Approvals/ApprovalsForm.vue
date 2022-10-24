<template>
  <div class="approvals_section">
    <div class="form_block">
      <!-- <div class="form_block_title">Отметьте все верные утверждени</div> -->
      <p class="form_block_title">Отметьте все верные утверждения</p>
      <div class="form_block">
        <v-radio-group v-model="currentData.informationGoals">
          <v-checkbox
            v-for="(item, index) in currentData.list"
            :key="index"
            class="d-flex align-items-start"
            v-model="currentData.informationGoals"
            :value="item.value"
            hide-details
          >
            <template v-slot:label>
              <div
                :class="{
                  toggleText: currentData.informationGoals != item.value,
                }"
              >
                {{ item.value }}
              </div>
            </template>
          </v-checkbox>
        </v-radio-group>
      </div>
    </div>
    <LineStep :step="17" class="mt-5" />
    <v-btn
      block
      large
      :disabled="!isList"
      @click="redirect()"
      class="mt-10 auth_form_bth"
      color="primary"
      >Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "../../components/line_step/line_step.vue";
export default {
  components: {
    LineStep,
  },
  data() {
    return {
      currentData: {
        informationGoals: [],
        list: [
          {
            id: 1,
            value:
              "Компания является финансовым институтом в соотвестии с законом США о налогооблажении иностранных счетов (FATCA) и/или главой 20.1",
          },
          {
            id: 2,
            value:
              "Компания, выгодоприобретатель или бенецифиар компания является налоговым резидентом США",
          },
          {
            id: 3,
            value:
              "Компания является хозяйственным обществом, имеющим стратегическое значение для оборонно-промышленного комплекса и безопасности РФ, либо обществом, находящийся под его прямым или косвенным контроллем, которые указаны в Федеральном законе от 27.07.2014 N 213-Ф3",
          },
          {
            id: 4,
            value:
              "Компания осуществляет виды деятельности, которые могут именить стратегическое значение для оборонно промышленного комплекса и безопасноти РФ",
          },
          {
            id: 5,
            value:
              "Компания не относиться к указанным в настоящем пунтке юридическим лицам",
          },
        ],
      },
      list: [
        {
          id: 1,
          value:
            "Компания является финансовым институтом в соотвестии с законом США о налогооблажении иностранных счетов (FATCA) и/или главой 20.1",
        },
        {
          id: 2,
          value:
            "Компания, выгодоприобретатель или бенецифиар компания является налоговым резидентом США",
        },
        {
          id: 3,
          value:
            "Компания является хозяйственным обществом, имеющим стратегическое значение для оборонно-промышленного комплекса и безопасности РФ, либо обществом, находящийся под его прямым или косвенным контроллем, которые указаны в Федеральном законе от 27.07.2014 N 213-Ф3",
        },
        {
          id: 4,
          value:
            "Компания осуществляет виды деятельности, которые могут именить стратегическое значение для оборонно промышленного комплекса и безопасноти РФ",
        },
        {
          id: 5,
          value:
            "Компания не относиться к указанным в настоящем пунтке юридическим лицам",
        },
      ],
    };
  },
  methods: {
    redirect() {
      this.$router.push("/rate");
    },
    toggleText(e) {
      e.preventDefault();
    },
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
</style>