export const loadCurrentData = function({currentData, step, vue}) {
    const formData = vue.$store.state.formData;
    for(const field in currentData){
        currentData[field] = formData[step][field]
    }
}

export const loadSubCurrentData = function({currentData, substep, vue, index}) {
    const formData = vue.$store.state.formData;
    for(const field in currentData){
        currentData[field] = formData['step_4']['list_persone'][index][substep][field]
    }
}