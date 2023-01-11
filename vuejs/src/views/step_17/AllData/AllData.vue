<template>
  <div>
    <line-step :step="number_step" class="mt-10" />
  </div>
</template>
<script>
import LineStep from "@/components/line_step/line_step.vue"
import { translateMixin } from '@/mixin/translate'
export default {
  mixins: [translateMixin],
  props: {
    number_step: {
      type: Number,
    }
  },
  data() {
    return {
      dialog: false,
      dialogAgreement: false,
      formData: {},
    };
  },
  methods: {
    async sendData() {
      this.$store.dispatch('addObjectFormData', {
        object: 'step_11',
        value: {
          is_finished: true,
        }
      });


      this.dialog = true;
    },
    deepClone(obj) {
      if (obj === null) return null;
      let clone = Object.assign({}, obj);

      Object.keys(clone).forEach(
        key =>
        (clone[key] =
          typeof obj[key] === "object" ? this.deepClone(obj[key]) : obj[key])
      );

      return Array.isArray(obj) && obj.length
        ? (clone.length = obj.length) && Array.from(clone)
        : Array.isArray(obj)
          ? Array.from(obj)
          : clone;
    },
    isObject(element) {
      if (typeof element == "object") {
        return true;
      } else {
        return false;
      }
    },
    isBoolean(element) {
      if (typeof element == "boolean") {
        return true;
      } else {
        return false;
      }
    },
    isArray(element) {
      if (Array.isArray(element)) {
        return true;
      } else {
        return false;
      }
    },
    isTypeObject(object) {
      if (Array.isArray(object)) {
        return "";
      }
      return "";
    },
    closeAll() {
      window.Telegram.WebApp.close();
    },

    isFormData(index) {
      return !!this.$store.state.formData['step_' + index]
    },
    getStepFromFormData(index) {
      return this.$store.state.formData?.['step_' + index]
    },
    back() {
      this.$router.push({ name: `step_${this.number_step - 1}` });
    },
  },
  computed: {
    getFormData() {
      let formData = this.deepClone(this.$store.state.formData);
      for (const stepName in formData) {
        let step = formData[stepName]
        for (let keyStep in step) {
          // SKIP
          const list_skip = [
            'opf',
            'document_certifying_identity_executive_file',
            'document_certifying_identity_executive',

            'document_confirming_real_activity_file',
            'document_licenses_file',

            'document_confirming_real_activity',
            'document_licenses',
          ];
          if (list_skip.indexOf(keyStep) >= 0) {
            continue
          }

          let valueStep = step[keyStep]
          if (this.isArray(valueStep)) {
            let isTypeArray = null;

            if (keyStep === 'list_persone') {
              const arr_fio = valueStep.map((val) => {
                const account_own_lastname = val?.['substep_1']?.account_own_lastname;
                const account_own_name = val?.['substep_1']?.account_own_name;
                const account_own_surname = val?.['substep_1']?.account_own_surname;
                return {
                  type: 'Variable',
                  body: `${account_own_lastname} ${account_own_name} ${account_own_surname}`,
                }
              })
              console.log('arr_fio', arr_fio);
              step[keyStep] = {
                type: 'Array',
                typeArray: 'Variable',
                body: arr_fio,
              }

              continue
            }

            for (let keySubStep in valueStep) {
              let valueSubStep = valueStep[keySubStep];
              if (this.isArray(valueSubStep)) {
                valueStep[keySubStep] = {
                  type: 'Array',
                  body: valueSubStep,
                }
                isTypeArray = "Array";
              } else if (this.isObject(valueSubStep)) {
                valueStep[keySubStep] = {
                  type: 'Object',
                  body: valueSubStep,
                }

                isTypeArray = "Object";
              } else if (this.isBoolean(valueSubStep)) {
                valueStep[keyStep] = {
                  type: 'Boolean',
                  body: valueSubStep,
                }
                isTypeArray = "Boolean";
              } else {
                valueStep[keySubStep] = {
                  type: 'Variable',
                  body: valueSubStep,
                }
                isTypeArray = "Variable";
              }
            }
            step[keyStep] = {
              type: 'Array',
              typeArray: isTypeArray,
              body: valueStep,
            }
          } else if (this.isObject(valueStep)) {
            step[keyStep] = {
              type: 'Object',
              body: valueStep,
            }
          } else if (this.isBoolean(valueStep)) {
            step[keyStep] = {
              type: 'Boolean',
              body: valueStep,
            }
          } else if (valueStep || valueStep === 0) {
            step[keyStep] = {
              type: 'Variable',
              body: valueStep,
            }
          } else {
            step[keyStep] = {
              type: 'Unknow',
              body: valueStep,
            }
          }
        }
      }

      return formData;
    },
    is_OOO() {
      return this.$store.state.formData.step_1?.opf?.short === 'ООО';
    },

  },
  mounted() {

  },
  components: { LineStep },
};
</script>
<style scoped>

</style>