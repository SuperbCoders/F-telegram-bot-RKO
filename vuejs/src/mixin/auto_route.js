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

            const arr_last_step = last_step.split("*");

            if (arr_last_step.length === 2) {
                const type = arr_last_step[1];
                const sub_last_step = arr_last_step[0];
                console.log(sub_last_step, type);
                let next_push = "step_1";
                switch (sub_last_step) {
                    case 'substep_0':
                        next_push = 'substep_1';
                        break;
                    case 'substep_1':
                        next_push = 'substep_2';
                        break;
                    case 'substep_2':
                        next_push = 'substep_3';
                        break
                    case 'substep_3':
                        next_push = 'substep_4';
                        break
                    case 'substep_4':
                        next_push = 'substep_5';
                        break
                    case 'substep_5':
                        next_push = 'substep_6';
                        break
                    case 'substep_6':
                        next_push = 'substep_7';
                        break
                    case 'substep_7':
                        next_push = 'substep_8';
                        break
                }
                if (type === 'supervisory') {
                    this.$router.push({ 'name': next_push });
                } else if (type === 'collegial') {
                    this.$router.push({ 'name': next_push });
                }
            } else {
                let next_push = "/";
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
                }
                this.$router.push({ name: next_push });
            }

        }
    }
}