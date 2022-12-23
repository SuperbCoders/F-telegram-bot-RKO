import Vue from "vue";
import VueRouter from "vue-router";

import AuthView from '@/views/step_1/Auth/AuthView.vue'
import Contact from '@/views/step_2/Contact/Contact.vue'
import Address from '@/views/step_3/Address/AdressView.vue'
import Information_individuals_organization from '@/views/step_4/Information_individuals_organization/Information_individuals_organization.vue'
// import Structure from '@/views/step_3/Structure/StructureForm.vue'
// import PlanningOperation from '@/views/step_4/PlanningOperation/PlanningOperationForm.vue'
// import Beneficiaries from '@/views/step_5/Beneficiaries/BeneficiariesForm.vue'
// import Purposes from '@/views/step_6/Purposes/PurposesForm.vue'
// import Approvals from '@/views/step_9/Approvals/ApprovalsForm.vue'
// import Rate from '@/views/step_10/Rate/RateForm.vue'
// import AllData from '@/views/step_11/AllData/AllData.vue'


// import AdditionalInformation from '@/views/AdditionalInformation/AdditionalInformation.vue'
// import Founders from '@/views/Founders/Founders.vue'
// import Codeword from '@/views/Codeword/Codeword.vue'
// import Information_counterparties from '@/views/Information_counterparties/Information_counterparties.vue'
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
    component: AuthView
  },
  {
    path: "/contact",
    name: "step_2",
    component: Contact,
  },
  {
    path: "/address",
    name: "step_3",
    component: Address
  },
  {
    path: "/information_individuals_organization",
    name: "step_4",
    component: Information_individuals_organization,
  },
  // {
  //   path: "/sctructure",
  //   name: "step_3",
  //   component: Structure
  // },

  // STEP 4 is delete
  // STEP 5 is delete

  // {
  //   path: "/planning",
  //   name: "step_6",
  //   component: PlanningOperation
  // },
  // {
  //   path: "/beneficiaries",
  //   name: "step_7",
  //   component: Beneficiaries
  // },
  // {
  //   path: "/purposes",
  //   name: "step_8",
  //   component: Purposes
  // },
  // {
  //   path: "/approvals",
  //   name: "step_9",
  //   component: Approvals
  // },
  // {
  //   path: "/rate",
  //   name: "step_10",
  //   component: Rate
  // },
  // {
  //   path: "/all-data",
  //   name: "step_11",
  //   component: AllData
  // },

  // Неприкаяные
 
  // {
  //   path: "/consent_receive_newsletter",
  //   name: "Consent_receive_newsletter",
  //   component: Consent_receive_newsletter,
  // },
  // {
  //   path: "/additional_information",
  //   name: "AdditionalInformation",
  //   component: AdditionalInformation,
  // },
  // {
  //   path: "/founders",
  //   name: "Founders",
  //   component: Founders,
  // },
  
  // {
  //   path: "/information_counterparties",
  //   name: "Information_counterparties",
  //   component: Information_counterparties,
  // },
  // {
  //   path: "/codeword",
  //   name: "Codeword",
  //   component: Codeword,
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
