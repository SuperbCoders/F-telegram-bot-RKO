<template>
    <div>
        <div>
            <span>ИНН</span> <span></span>
        </div>
        <div v-for="(val, ind) in formData" :key="ind">
            <div v-for="(val2, ind2) in val" :key="ind2">
                {{ ind2 }} => {{ val2 }}
            </div>
        </div>

        <v-btn elevation="2" class="card_content_button" large @click="sendData()">Отправить</v-btn>
    </div>
</template>
<script>
export default {
    data() {
        return {
            formData: {}
        }
    },
    mounted(){
        this.formData = this.$store.state.formData;
    },
    methods: {
        async sendData(){
            const formData = new FormData();
            for(const obj of this.formData){
                for(const element in obj){
                    const name = element;
                    const value = obj[element];
                    console.log(name, value)
                    formData.append(name, value);
                }
            }
            
            await fetch("http://localhost:8000/loan-application/create/", {
                method: "POST",
                body: formData,
            })

            // this.$router.push("/already")
        }
    }
}
</script>
<style>
.card_content_button {
  width: 100%;
  box-shadow: 0 0 4px #00000030;
  background: #d41367 !important;
  border-radius: 6px;
  margin-top: 20px;
  font-family: Roboto;
  font-size: 14px !important;
  color: #fff !important;
  font-weight: 500;
  padding: 16px 30px !important;
  text-transform: none;
}
</style>