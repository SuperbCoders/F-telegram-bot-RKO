<template>
    <div class="document_section">
        <v-btn class="mb-5 auth_form_bth" color="primary" @click="back">Назад
        </v-btn>
        <div>
            <p class="subtitle text-left document_section_text mb-5">
                <span class="star">*</span>
                Документ,удостоверяющий личность единоличного исполнительного органа
            </p>

            <div v-if="this.currentData.document_certifying_identity_executive_file" class="list_file">
                <div v-for="(file, index) in this.currentData.document_certifying_identity_executive_file" :key="index"
                    class="block_file mr-4">
                    <div class="card_file">
                        <div class="type_file">{{ getType(file.type) }}</div>
                        <div class="size_file">{{ getSize(file.size) }} Мб</div>
                    </div>
                    <div class="name_file">{{ file.name }}</div>
                </div>
            </div>
        </div>

        <AttachButton class="mb-5" text="Загрузить документ" @file="onfile_certifying_identity_executive" />

        <div>
            <p class="subtitle text-left document_section_text mb-5">
                <span class="star">*</span>
                Документы,подтверждающие реальную деятельность
            </p>

            <div v-if="this.currentData.document_confirming_real_activity_file" class="list_file">
                <div v-for="(file, index) in this.currentData.document_confirming_real_activity_file" :key="index"
                    class="block_file">
                    <div class="card_file">
                        <div class="type_file">{{ getType(file.type) }}</div>
                        <div class="size_file">{{ getSize(file.size) }} Мб</div>
                    </div>
                    <div class="name_file">{{ file.name }}</div>
                </div>
            </div>
        </div>

        <AttachButton class="mb-5" text="Загрузить документ" @file="onfile_confirming_real_activity" />

        <div>
            <p class="subtitle text-left document_section_text mb-5">
                Лицензии
            </p>

            <div v-if="this.currentData.document_licenses_file" class="list_file">
                <div v-for="(file, index) in this.currentData.document_licenses_file" :key="index" class="block_file">
                    <div class="card_file">
                        <div class="type_file">{{ getType(file.type) }}</div>
                        <div class="size_file">{{ getSize(file.size) }} Мб</div>
                    </div>
                    <div class="name_file">{{ file.name }}</div>
                </div>
            </div>
        </div>


        <AttachButton class="mb-5" text="Загрузить документ" @file="onfile_licenses" />

        <div>
            <p class="subtitle text-left document_section_text mb-5">
                Документ, удостоверяющий личность ЕИО
            </p>

            <div v-if="this.currentData.document_certifying_identity_ceo_file" class="list_file">
                <div v-for="(file, index) in this.currentData.document_certifying_identity_ceo_file" :key="index"
                    class="block_file">
                    <div class="card_file">
                        <div class="type_file">{{ getType(file.type) }}</div>
                        <div class="size_file">{{ getSize(file.size) }} Мб</div>
                    </div>
                    <div class="name_file">{{ file.name }}</div>
                </div>
            </div>
        </div>


        <AttachButton class="mb-5" text="Загрузить документ" @file="onfile_certifying_identity_ceo" />

        <line-step :step="number_step" class="mt-6" />

        <v-btn block large class="mt-10 auth_form_bth" color="primary" @click="redirect()">Продолжить
        </v-btn>
    </div>
</template>

<script>
import AttachButton from '@/components/button/attachButton.vue';
import LineStep from "@/components/line_step/line_step.vue";
import { loadCurrentData } from '@/utils/loadStore'

export default {
    props: {
        number_step: {
            type: Number,
        }
    },
    data() {
        return {
            currentData: {
                document_certifying_identity_executive_file: null,
                document_confirming_real_activity_file: null,
                document_licenses_file: null,
                document_certifying_identity_ceo_file: null,

                document_certifying_identity_executive: [],
                document_confirming_real_activity: [],
                document_licenses: [],
                document_certifying_identity_ceo: [],

            },
        };
    },
    mounted() {
        loadCurrentData({
            currentData: this.currentData,
            step: `step_${this.number_step}`,
            vue: this,
        });
    },
    methods: {
        async onfile_certifying_identity_executive(files) {
            this.currentData.document_certifying_identity_executive_file = files;
            const { images } = await this.getURLfile(files);
            this.currentData.document_certifying_identity_executive = images;
        },
        async onfile_confirming_real_activity(files) {
            this.currentData.document_confirming_real_activity_file = files;
            const { images } = await this.getURLfile(files);
            this.currentData.document_confirming_real_activity = images;
        },
        async onfile_licenses(files) {
            this.currentData.document_licenses_file = files;
            const { images } = await this.getURLfile(files);
            this.currentData.document_licenses = images;
        },
        async onfile_certifying_identity_ceo(files) {
            this.currentData.document_certifying_identity_ceo_file = files;
            const { images } = await this.getURLfile(files);
            this.currentData.document_certifying_identity_ceo = images;
        },
        getType(type) {
            type = type.split("/")[1];
            return type;
        },
        getSize(size) {
            size = "" + size;
            return size[0] + size[1];
        },
        getName(name) {
            return name;
        },
        back() {
            this.$router.push({ name: `step_${this.number_step - 1}` });
        },
        async redirect() {
            const formData = new FormData();

            formData.append("documents", this.currentData.document_certifying_identity_executive)

            const response = await fetch(process.env.VUE_APP_HOST_API + `/api/document-load/`, {
                method: "POST",
                body: formData,
            });

            const data = await response.json();

            this.currentData.first_passport_page_url = data.path;

            this.$store.dispatch("addObjectFormData", {
                object: `step_${this.number_step}`,
                value: this.currentData,
            });
            this.next();
        },
        next() {
            this.$router.push({ name: `step_${this.number_step + 1}` });
        },

        async getURLfile(files) {
            const formData = new FormData();
            for (const index in files) {
                formData.append(`document_${index}`, files[index])
            }

            const response = await fetch(process.env.VUE_APP_HOST_API + `/api/document-load/`, {
                method: "POST",
                body: formData,
            });

            const data = await response.json();
            return data
        }
    },
    components: {
        AttachButton,
        LineStep,
    }

};
</script>
  
<style scoped>
.list_file {
    display: flex;
}

.card_file {
    background: #f3f4f4;
    padding: 10px 14px;
    border-radius: 6px;
    max-width: 150px;
}

.size_file {
    text-align: center;
    font-size: 12px;
}

.type_file {
    font-size: 20px;
    font-weight: bold;
    color: #d41367;
    text-align: center;
    text-transform: uppercase;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.name_file {
    margin-top: 5px;
    margin-bottom: 10px;
    font-size: 12px;
    width: 60px;
    overflow-x: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

.document_section_text {
    font-family: Roboto;
    font-size: 18px;
}
</style>