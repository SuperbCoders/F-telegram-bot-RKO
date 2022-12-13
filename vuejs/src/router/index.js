import Vue from "vue";
import VueRouter from "vue-router";

import AuthView from '../views/Auth/AuthView.vue'
import Address from '../views/Address/AdressView.vue'
import Structure from '../views/Structure/StructureForm.vue'
import Intelligence from '../views/intelligence/intelligenceForm.vue'
import informationStaff from '../views/informationStaff/informationStaffForm.vue'
import DocumentPage from '../views/Documents/documentForm.vue'
import individualsForm from '../views/informationIndivduals/individualsForm.vue'
import DocumentsForms from '../views/DocumentsForm/DocumentForm.vue'
import AddressForm from '../views/AddressForm/AddressForm.vue'
import KinshipStatus from '../views/KinshipStatus/KinshipStatusForm.vue'
import ForeignPerson from '../views/isAForeignPerson/ForeignPerson.vue'
import EmailForm from '../views/EmailForm/EmailForm.vue'
import ClientInfo from '../views/ClientInfo/ClientInfoForm.vue'
import DocumentFogeiner from '../views/DocumentFogeiner/DocumentFogeinerForm.vue'
import PlanningOperation from '../views/PlanningOperation/PlanningOperationForm.vue'
import Beneficiaries from '../views/Beneficiaries/BeneficiariesForm.vue'
import Rate from '../views/Rate/RateForm.vue'
import Purposes from '../views/Purposes/PurposesForm.vue'
import Approvals from '../views/Approvals/ApprovalsForm.vue'
import AllData from '../views/AllData/AllData.vue'
import AllDataPersone from '../views/allDataPersone/AllDataPersone.vue'

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
  {
    path: "/information-staff",
    name: "step_4",
    component: informationStaff
  },
  {
    path: "/intelligence",
    name: "step_5",
    component: Intelligence
  },
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
