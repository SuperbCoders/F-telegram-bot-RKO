<template>
    <div class="form_block mt-5">
        <p class="text-left">Адрес</p>
        <v-text-field
            id="oldName"
            placeholder="ООО Ромашка"
            class="align-center border-none"
            name="oldName"
            outlined
            :required="true"
        ></v-text-field>
    </div>
</template>

<script>
export default {
    props: {
        label: String,
        placeholder: String
    }
}
</script>

<style>

</style>