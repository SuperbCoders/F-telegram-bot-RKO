import Vue from "vue";
import VueRouter from "vue-router";

import AuthView from '@/views/step_1/Auth/AuthView.vue'
import Contact from '@/views/step_2/Contact/Contact.vue'
import Address from '@/views/step_3/Address/AdressView.vue'
import Information_individuals_organization from '@/views/step_4/Information_individuals_organization/Information_individuals_organization.vue'
import Documents from '../views//step_5/Documents/Documents.vue'
import Structure from '@/views/step_6/Structure/StructureForm.vue'
import Founders from '@/views/step_7/Founders/Founders.vue'
import Beneficiaries from '@/views/step_8/Beneficiaries/BeneficiariesForm.vue'
import AdditionalInformation from '@/views/step_9/AdditionalInformation/AdditionalInformation.vue'
import PlanningOperation from '@/views/step_10/PlanningOperation/PlanningOperationForm.vue'
import Approvals from '@/views/step_11/Approvals/ApprovalsForm.vue'
import Codeword from '@/views/step_12/Codeword/Codeword.vue'
import Information_counterparties from '@/views/step_13/Information_counterparties/Information_counterparties.vue'
import Purposes from '@/views/step_14/Purposes/PurposesForm.vue'
import Rate from '@/views/step_15/Rate/RateForm.vue'
import AllData from '@/views/step_16/AllData/AllData.vue'







// import Select_additional_products from '@/views/Select_additional_products/Select_additional_products.vue'
// import Consent_receive_newsletter from '@/views/Consent_receive_newsletter/Consent_receive_newsletter.vue'


import individualsForm from '@/views/substep/substep_1/informationIndivduals/individualsForm.vue'
import DocumentsForms from '@/views/substep/substep_2/DocumentsForm/DocumentForm.vue'
import KinshipStatus from '@/views/substep/substep_3/KinshipStatus/KinshipStatusForm.vue'
import AddressForm from '@/views/substep/substep_4/AddressForm/AddressForm.vue'
import ClientInfo from '@/views/substep/substep_5/ClientInfo/ClientInfoForm.vue'
import AllDataPersone from '@/views/substep/substep_6/allDataPersone/AllDataPersone.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "step_1",
    component: AuthView,
    props: {
      number_step: 1,
    }
  },
  {
    path: "/contact",
    name: "step_2",
    component: Contact,
    props: {
      number_step: 2,
    }
  },
  {
    path: "/address",
    name: "step_3",
    component: Address,
    props: {
      number_step: 3,
    }
  },
  {
    path: "/information_individuals_organization",
    name: "step_4",
    component: Information_individuals_organization,
    props: {
      number_step: 4,
    }
  },
  {
    path: "/documents",
    name: "step_5",
    component: Documents,
    props: {
      number_step: 5,
    }
  },
  {
    path: "/sctructure",
    name: "step_6",
    component: Structure,
    props: {
      number_step: 6,
    }
  },
  {
    path: "/founders",
    name: "step_7",
    component: Founders,
    props: {
      number_step: 7,
    }
  },
  {
    path: "/beneficiaries",
    name: "step_8",
    component: Beneficiaries,
    props: {
      number_step: 8,
    }
  },
  {
    path: "/additional_information",
    name: "step_9",
    component: AdditionalInformation,
    props: {
      number_step: 9,
    }
  },
  {
    path: "/planning",
    name: "step_10",
    component: PlanningOperation,
    props: {
      number_step: 10,
    }
  },
  {
    path: "/approvals",
    name: "step_11",
    component: Approvals,
    props: {
      number_step: 11,
    }
  },
  {
    path: "/codeword",
    name: "step_12",
    component: Codeword,
    props: {
      number_step: 12,
    }
  },
  {
    path: "/information_counterparties",
    name: "step_13",
    component: Information_counterparties,
    props: {
      number_step: 13,
    }
  },
  {
    path: "/purposes",
    name: "step_14",
    component: Purposes,
    props: {
      number_step: 14,
    }
  },
  {
    path: "/rate",
    name: "step_15",
    component: Rate,
    props: {
      number_step: 15,
    }
  },
  {
    path: "/all-data",
    name: "step_16",
    component: AllData,
    props: {
      number_step: 16,
    }

  },






  // Неприкаяные

  // {
  //   path: "/consent_receive_newsletter",
  //   name: "Consent_receive_newsletter",
  //   component: Consent_receive_newsletter,
  // },



  // {
  //   path: "/information_counterparties",
  //   name: "Information_counterparties",
  //   component: Information_counterparties,
  // },

  // {
  //   path: "/select_additional_products",
  //   name: "Select_additional_products",
  //   component: Select_additional_products,
  // },
  //



  {
    path: "/individual-info/:id",
    name: "substep_1",
    component: individualsForm
  },
  {
    path: "/documents-forms/:id",
    name: "substep_2",
    component: DocumentsForms
  },
  {
    path: "/kinship-status-forms/:id",
    name: "substep_3",
    component: KinshipStatus
  },
  {
    path: "/address-form/:id",
    name: "substep_4",
    component: AddressForm
  },
  {
    path: "/client-info/:id",
    name: "substep_5",
    component: ClientInfo
  },
  {
    path: "/all-data-persone/:id",
    name: "substep_6",
    component: AllDataPersone
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
