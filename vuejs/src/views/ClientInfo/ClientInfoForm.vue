<template>
    <div class="client_info_section">
        <v-form ref="form" v-model="valid" lazy-validation>
            <div class="form_block">
                <p class="text-left form_block_title">Место рождения</p>
                <v-text-field id="oldName" placeholder="Введите адрес" class="align-center border-none" outlined
                    :rules="requiredRules" :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Дата рождения</p>
                <v-menu :close-on-content-click="false" transition="scale-transition" offset-y min-width="auto">
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field placeholder="Дата" id="passportIssueDate" name="passportIssueDate" outlined
                            append-icon="mdi-calendar-blank" readonly v-model="dateStarting" :rules="requiredRules"
                            :required="true" v-bind="attrs" v-on="on"></v-text-field>
                    </template>
                    <v-date-picker v-model="dateStarting" @input="passportIssueDateMenu = false"></v-date-picker>
                </v-menu>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Тип документа удостоверяющего личность</p>
                <v-combobox filled outlined :rules="requiredRules" placeholder="Выберите тип"></v-combobox>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Серия документа удостоверяющего личность (при наличии)</p>
                <v-text-field id="oldName" placeholder="Введите серию документа" class="align-center border-none"
                    outlined :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Номер документа удостоверяющего личность</p>
                <v-text-field id="oldName" placeholder="Введите номер документа" class="align-center border-none"
                    outlined :rules="requiredRules" :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Кем выдан</p>
                <v-text-field id="oldName" placeholder="Наименование" class="align-center border-none" outlined
                    :rules="requiredRules" :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Код подзразделения (при наличии)</p>
                <v-text-field id="oldName" placeholder="Введите имя" class="align-center border-none" outlined
                    :required="true"></v-text-field>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Дата выдачи</p>
                <v-menu :close-on-content-click="false" transition="scale-transition" offset-y min-width="auto">
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field placeholder="Дата" id="passportIssueDate" name="passportIssueDate" outlined
                            append-icon="mdi-calendar-blank" readonly v-model="dateStarting" :rules="requiredRules"
                            :required="true" v-bind="attrs" v-on="on"></v-text-field>
                    </template>
                    <v-date-picker v-model="dateStarting" @input="passportIssueDateMenu = false"></v-date-picker>
                </v-menu>
            </div>
            <div class="form_block">
                <p class="text-left form_block_title">Срок действия</p>
                <v-menu :close-on-content-click="false" transition="scale-transition" offset-y min-width="auto">
                    <template v-slot:activator="{ on, attrs }">
                        <v-text-field placeholder="Дата" id="passportIssueDate" name="passportIssueDate" outlined
                            append-icon="mdi-calendar-blank" readonly v-model="dateStarting" :rules="requiredRules"
                            :required="true" v-bind="attrs" v-on="on"></v-text-field>
                    </template>
                    <v-date-picker v-model="dateStarting" @input="passportIssueDateMenu = false"></v-date-picker>
                </v-menu>
            </div>
        </v-form>
        <v-btn block large :disabled="!valid" class="mt-10 auth_form_bth" color="primary" @click="validate">Продолжить
        </v-btn>
    </div>
</template>

<script>
export default {
    data: () => ({
        valid: true,
        listRole: [],
        dateStarting: null,
        dateEnd: null,
        test: [],
        requiredRules: [(v) => !!v || "Это поле обязательно"],
    }),
    methods: {
        validate() {
            this.$refs.form.validate();
            if (this.$refs.form.validate()) {
                this.$router.push("/address");
            }
        },
    },
};
</script>

<style>

</style>