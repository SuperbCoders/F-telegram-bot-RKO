<template>
  <div class="radio_group_block">
    <div class="form_radio_group d-flex">
      <div class="form_radio_btn">
        <input
          class="form_radio_btn_input"
          :id="name + '_1'"
          type="radio"
          :name="name"
          :value="true"
          :checked="is_checked"
        />
        <label
          class="form_radio form_radio_btn_input_radius__left"
          :for="name + '_1'"
          @click="updateStatus(true)"
          >Да</label
        >
      </div>
      <div class="form_radio_btn">
        <input
          class="form_radio_btn_input"
          :id="name + '_2'"
          type="radio"
          :name="name"
          :value="false"
          :checked="!is_checked"
        />
        <label @click="updateStatus(false)" class="form_radio_btn_input_radius__right" :for="name + '_2'"
          >Нет</label
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      
    }
  },
  methods: {
    updateStatus (status) {
      this.$emit('isStatus', status)
    }
  },
  mounted () {
  },
  computed: {
    is_checked(){
      return this.status
    }
  },
  props: {
    name: {
      type: String
    },
    defaultButton: {
      type: String
    },
    status: {
      type: Boolean,
      default: false,
    }
  }
};
</script>

<style scoped>
.form_radio_btn {
  display: flex;
  font-family: Roboto;
}
.form_radio_btn_input_radius__left {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
.form_radio_btn_input_radius__right {
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}
.form_radio_btn input[type="radio"]:checked + label {
  color: white;
  background: #d41367;
}
.form_radio_btn > label {
  background: #f0f2f5;
  color: #323e48;
  padding: 8px 24px;
}
.form_radio_btn input[type="radio"]:disabled + label {
  background: #efefef;
  color: #666;
}
.form_radio_btn input {
  display: none;
}
</style>