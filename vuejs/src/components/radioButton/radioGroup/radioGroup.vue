<template>
  <div class="radio_group_block">
    <div class="form_radio_group d-flex">
        <div class="form_radio_btn">
          <input
            class="form_radio_btn_input"
            id="radio-1"
            type="radio"
            name="radio"
            value="1"
            checked
          />
          <label class="form_radio form_radio_btn_input_radius__left" for="radio-1">Да</label>
        </div>
        <div class="form_radio_btn ">
          <input class="form_radio_btn_input" id="radio-2" type="radio" name="radio" value="2" />
          <label class="form_radio_btn_input_radius__right" for="radio-2">Нет</label>
        </div>
      </div>
  </div>
</template>

<script>
export default {

}
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
  background: #D41367;
}
.form_radio_btn > label {
  background:#F0F2F5;
  color: #323E48;
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