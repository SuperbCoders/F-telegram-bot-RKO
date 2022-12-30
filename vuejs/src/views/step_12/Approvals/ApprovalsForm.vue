<template>
  <div class="approvals_section">
    <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
    <div class="form_block">
      <h2 class="">Сведения о соответствии FATCA и и стратегическом значении компании (выберите все верные утверждения)</h2>
      <div class="form_block checkboxs">
        <v-checkbox v-for="(item, index) in list" :key="index" class="d-flex align-items-start"
          v-model="currentData.information_goals" :value="item.key" hide-details>
          <template v-slot:label>
            <div :class="{
              toggleText: !currentData.information_goals.includes(item.value),
            }">
              {{ item.value }}
            </div>
          </template>
        </v-checkbox>
      </div>
    </div>
    <LineStep :step="11" class="mt-5" />
    <v-btn block large :disabled="!isList" @click="redirect()" class="mt-10 auth_form_bth" color="primary">Продолжить
    </v-btn>
  </div>
</template>

<script>
import LineStep from "@/components/line_step/line_step.vue";
import { loadCurrentData } from '@/utils/loadStore'

export default {
  components: {
    LineStep,
  },
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      currentData: {
        information_goals: [],

      },
      list: [
        {
          id: 1,
          key: 'isFatcaFinanceInstitute',
          value:
            "Является ли юридическое лицо Финансовым институтом в соответствии с Законом США «О налогообложении иностранных счетов» (FATCA) и/или главой 20.1 Налогового кодекса РФ",
        },
        {
          id: 2,
          key: 'isForeignTaxResident',
          value:
            "Является ли юридическое лицо, или бенефициар, или выгодоприобретатель налоговым резидентом иностранного государства и/или у юридического лица, бенефициара или выгодоприобретателя отсутствует налоговое резидентство во всех государствах (территориях))? Имеет ли юридическое лицо признаки Пассивной нефинансовой организации",
        },
        {
          id: 3,
          key: 'isForeignTaxResidentIndividual',
          value:
            "Подтверждаю и гарантирую, что все Выгодоприобретатели/бенефициары индивидуального предпринимателя являются налогоплательщиками исключительно в РФ и, если выгодоприобретателем является юридическое лицо, то оно не имеет признаков Пассивной нефинансовой организации",
        },
        {
          id: 4,
          key: 'isUsaTaxResident',
          value:
            "Является ли юридическое лицо, выгодоприобретатель или бенефициар налоговым резидентом США?",
        },
        {
          id: 5,
          key: 'isStrategicImportanceOPK',
          value:
            "Компания осуществляет виды деятельности, которые могут иметь стратегическое значение для оборонно-промышленного комплекса и безопасности РФ",
        },
        {
          id: 6,
          key: 'isStrategicImportanceOPK213FZ',
          value:
            "Компания является хозяйственным обществом, имеющим стратегическое значение для оборонно-промышленного комплекса и безопасности РФ либо обществом, находящимся под его прямым или косвенным контролем, которые указаны в Федеральном законе от 21.07.2014 № 213-ФЗ",
        },
        {
          id: 7,
          key: 'isNoneOfThis',
          value:
            "Компания не относится к указанным в настоящем пункте юридическим лицам",
        },
      ],
    };
  },
  methods: {
    redirect() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_12',
        value: this.currentData
      })
      this.next();
    },
    toggleText(e) {
      e.preventDefault();
    },
    next() {
      this.$router.push({ name: `step_${this.number_step + 1}` });
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
        },
  },
  computed: {
    isList() {
      if (this.currentData.information_goals.length >= 1) {
        return true;
      }
      return false;
    },
  },
  mounted(){
    loadCurrentData({
      currentData: this.currentData,
      step: `step_${this.number_step}`,
      vue: this,
    });
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