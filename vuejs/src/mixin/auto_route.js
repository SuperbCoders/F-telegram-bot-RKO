export const auto_route = {
    methods: {
        async auto_route() {
            const phone = this.$route.query?.phone;
            if (!phone) return
            this.currentData.contact_number = phone;

            const response = await fetch(process.env.VUE_APP_HOST_API + `/api/loan-application/current/${phone}/`)
            const formData = await response.json();
            console.log({ formData });
            this.$store.dispatch("loadObjectFormData", formData);
            const last_step = formData?.last_step;

            if (!last_step) return

            let next_push = "step_1";
            switch (last_step) {
                case 'step_1':
                    next_push = 'step_2';
                    break;
                case 'step_2':
                    next_push = 'step_3';
                    break
                case 'step_3':
                    next_push = 'step_4';
                    break
                case 'step_4':
                    next_push = 'step_5';
                    break
                case 'step_5':
                    next_push = 'step_6';
                    break
                case 'step_6':
                    next_push = 'step_7';
                    break
                case 'step_7':
                    next_push = 'step_8';
                    break
                case 'step_8':
                    next_push = 'step_9';
                    break
                case 'step_9':
                    next_push = 'step_10';
                    break
                case 'step_10':
                    next_push = 'step_11';
                    break
                case 'step_11':
                    next_push = 'step_12';
                    break
                case 'step_12':
                    next_push = 'step_13';
                    break
                case 'step_13':
                    next_push = 'step_14';
                    break
                case 'step_14':
                    next_push = 'step_15';
                    break
                case 'step_15':
                    next_push = 'step_16';
                    break
                case 'step_16':
                    next_push = 'step_17';
                    break


                case 'substep_0':
                    next_push = 'step_4';
                    break
                case 'substep_1':
                    next_push = 'step_4';
                    break
                case 'substep_2':
                    next_push = 'step_4';
                    break
                case 'substep_3':
                    next_push = 'step_4';
                    break
                case 'substep_4':
                    next_push = 'step_4';
                    break
                case 'substep_5':
                    next_push = 'step_4';
                    break
            }

            this.$router.push({ name: next_push });

        }
    }
}