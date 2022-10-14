<template>
    <div class="email_section">
        <div class="form_block">
            <p class="text-left form_block_title">Адрес фактического проживания</p>
            <v-radio-group v-model="isAddress" mandatory>
                <v-radio label="Совпадает с адресом регистации" value="Совпадает с адресом регистации"></v-radio>
                <v-radio label="Совпадает с адресом проживания" value="Совпадает с адресом проживания"></v-radio>
                <v-radio label="Не совпадает с адресом регистации и адресом проживания" value="true"></v-radio>
            </v-radio-group>
            <p class="form_block_title">
                Адрес фактического проживания
            </p>
            <v-text-field id="oldName" v-if="isAddress" placeholder="Введите адрес"
                class="align-center border-none mt-5" outlined :required="true"></v-text-field>
        </div>
        <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
    </v-btn>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>