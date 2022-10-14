<template>
    <div class="status_kinship_block">
        <div class="form_block">
            <p class="text-left form_block_label">
                Степень родства либо статус
                (супруг или супруга) по отношению к публичному должностному лицу</p>
            <v-combobox filled :rules="requiredRules" required outlined placeholder="Выберите из списка"></v-combobox>
            <div class="form_block">
                <p class="text-left form_block_title">Адрес регистрации</p>
                <v-text-field id="oldName" placeholder="Введите имя" class="align-center border-none" outlined
                    :rules="requiredRules" :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Адресс регистрации</p>
                <v-text-field id="oldName" placeholder="Введите имя" class="align-center border-none" outlined
                    :rules="requiredRules" :required="true"></v-text-field>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>