<template>
    <div>
        <p class="text">Шаг {{ step }} из {{ count_step }}</p>
        <div class="line">
            <div 
                v-for="index in count_step" 
                :key="index" class="step"
                :style="{background: step < index ? '#F1BAD2' : '#D41367'}"
                ></div>
        </div>
    </div>
    
</template>
<script>
export default {
    name: "line_step",
    props: {
        step: Number
    },
    data(){
        return {
            count_step: 16,
        }
    },
    methods: {

    }
}
</script>
<style scoped>
.line {
    display: flex;
    gap: 10px;
}
.step {
    width: 100%;
    height: 5px;
    background: #F1BAD2;
    border-radius: 4px;
}
.text { 
    color: #8E909B;
    font-size: 13px;
    text-align: left;
}
</style>