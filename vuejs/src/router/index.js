import Vue from "vue";
import VueRouter from "vue-router";

import AuthView from '@/views/step_1/Auth/AuthView.vue'
import Address from '@/views/step_2/Address/AdressView.vue'
import Structure from '@/views/step_3/Structure/StructureForm.vue'
// DELETE step_4
// DELETE step_5
import PlanningOperation from '@/views/step_6/PlanningOperation/PlanningOperationForm.vue'
import Beneficiaries from '@/views/step_7/Beneficiaries/BeneficiariesForm.vue'
import Purposes from '@/views/step_8/Purposes/PurposesForm.vue'
import Approvals from '@/views/step_9/Approvals/ApprovalsForm.vue'
import Rate from '@/views/step_10/Rate/RateForm.vue'
import AllData from '@/views/step_11/AllData/AllData.vue'

import Contact from '@/views/Contact/Contact.vue'
import AdditionalInformation from '@/views/AdditionalInformation/AdditionalInformation.vue'
import Founders from '@/views/Founders/Founders.vue'
import Codeword from '@/views/Codeword/Codeword.vue'
import Information_counterparties from '@/views/Information_counterparties/Information_counterparties.vue'
import Select_additional_products from '@/views/Select_additional_products/Select_additional_products.vue'
import Consent_receive_newsletter from '@/views/Consent_receive_newsletter/Consent_receive_newsletter.vue'
import Information_individuals_organization from '@/views/Information_individuals_organization/Information_individuals_organization.vue'

import individualsForm from '@/views/substep/substep_1/informationIndivduals/individualsForm.vue'
import DocumentsForms from '@/views/substep/substep_2/DocumentsForm/DocumentForm.vue'
import ForeignPerson from '@/views/substep/substep_3/isAForeignPerson/ForeignPerson.vue'
import KinshipStatus from '@/views/substep/substep_4/KinshipStatus/KinshipStatusForm.vue'
import AddressForm from '@/views/substep/substep_5/AddressForm/AddressForm.vue'
import EmailForm from '@/views/substep/substep_6/EmailForm/EmailForm.vue'
import DocumentPage from '@/views/substep/substep_7/Documents/documentForm.vue'
import ClientInfo from '@/views/substep/substep_8/ClientInfo/ClientInfoForm.vue'
import DocumentFogeiner from '@/views/substep/substep_9/DocumentFogeiner/DocumentFogeinerForm.vue'
import AllDataPersone from '@/views/substep/substep_10/allDataPersone/AllDataPersone.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "step_1",
    component: AuthView
  },
  {
    path: "/address",
    name: "step_2",
    component: Address
  },
  {
    path: "/sctructure",
    name: "step_3",
    component: Structure
  },
  // STEP 4 is delete
  // STEP 5 is delete

  {
    path: "/planning",
    name: "step_6",
    component: PlanningOperation
  },
  {
    path: "/beneficiaries",
    name: "step_7",
    component: Beneficiaries
  },
  {
    path: "/purposes",
    name: "step_8",
    component: Purposes
  },
  {
    path: "/approvals",
    name: "step_9",
    component: Approvals
  },
  {
    path: "/rate",
    name: "step_10",
    component: Rate
  },
  {
    path: "/all-data",
    name: "step_11",
    component: AllData
  },

  // Неприкаяные
  {
    path: "/contact",
    name: "contact",
    component: Contact,
  },
  {
    path: "/consent_receive_newsletter",
    name: "Consent_receive_newsletter",
    component: Consent_receive_newsletter,
  },
  {
    path: "/additional_information",
    name: "AdditionalInformation",
    component: AdditionalInformation,
  },
  {
    path: "/founders",
    name: "Founders",
    component: Founders,
  },
  {
    path: "/information_individuals_organization",
    name: "Information_individuals_organization",
    component: Information_individuals_organization,
  },
  {
    path: "/information_counterparties",
    name: "Information_counterparties",
    component: Information_counterparties,
  },
  {
    path: "/codeword",
    name: "Codeword",
    component: Codeword,
  },
  {
    path: "/select_additional_products",
    name: "Select_additional_products",
    component: Select_additional_products,
  },
  //


  
  {
    path: "/individual-info",
    name: "substep_1",
    component: individualsForm
  },
  {
    path: "/documents-forms",
    name: "substep_2",
    component: DocumentsForms
  },
  {
    path: "/foreign-person",
    name: "substep_3",
    component: ForeignPerson
  },
  {
    path: "/kinship-status-forms",
    name: "substep_4",
    component: KinshipStatus
  },
  {
    path: "/address-form",
    name: "substep_5",
    component: AddressForm
  },
  {
    path: "/email-form",
    name: "substep_6",
    component: EmailForm
  },
  {
    path: "/document",
    name: "substep_7",
    component: DocumentPage
  },
  {
    path: "/client-info",
    name: "substep_8",
    component: ClientInfo
  },
  {
    path: "/document-fogeiner",
    name: "substep_9",
    component: DocumentFogeiner
  },
  {
    path: "/all-data-persone",
    name: "substep_10",
    component: AllDataPersone
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
