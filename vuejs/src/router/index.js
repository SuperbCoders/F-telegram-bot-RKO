import Vue from "vue";
import VueRouter from "vue-router";
import LoanForm from "../views/loan/LoanForm";
import AuthView from '../views/Auth/AuthView.vue'
import Address from '../views/Address/AdressView.vue'
import Structure from '../views/Structure/StructureForm.vue'
import Intelligence from '../views/intelligence/intelligenceForm.vue'
import StructureGroup from '../views/StructureGroup/StructureGroupForm.vue'
import informationStaff from '../views/informationStaff/informationStaffForm.vue'
import CreditForm from '../views/credit/creditForm.vue'
import DocumentPage from '../views/Documents/documentForm.vue'
import individualsForm from '../views/informationIndivduals/individualsForm.vue'
import DocumentsForms from '../views/DocumentsForm/DocumentForm.vue'
import AddressForm from '../views/AddressForm/AddressForm.vue'
import KinshipStatus from '../views/KinshipStatus/KinshipStatusForm.vue'
import ForeignPerson from '../views/isAForeignPerson/ForeignPerson.vue'
import EmailForm from '../views/EmailForm/EmailForm.vue'
import ClientInfo from '../views/ClientInfo/ClientInfoForm.vue'
import DocumentFogeiner from '../views/DocumentFogeiner/DocumentFogeinerForm.vue'
import LicenseInfo from '../views/LicenseInformation/LicenseInformationForm.vue'
import PlanningOperation from '../views/PlanningOperation/PlanningOperationForm.vue'
import Beneficiaries from '../views/Beneficiaries/BeneficiariesForm.vue'
import Rate from '../views/Rate/RateForm.vue'
import Purposes from '../views/Purposes/PurposesForm.vue'
import AllData from '../views/AllData/AllData.vue'
import Already from '../views/Already/Already.vue'
Vue.use(VueRouter);

const routes = [
  {
    path: "/loan-form",
    name: "loan-form",
    component: LoanForm,
  },
  {
    path: "/",
    name: "auth-form",
    component: AuthView
  },
  {
    path: "/address",
    name: "address",
    component: Address
  },
  {
    path: "/sctructure-group",
    name: "sctructure-group",
    component: StructureGroup
  },
  {
    path: "/sctructure",
    name: "sctructure",
    component: Structure
  },
  {
    path: "/information-staff",
    name: "information-staff",
    component: informationStaff
  },
  {
    path: "/planning",
    name: "planning",
    component: PlanningOperation
  },
  {
    path: "/beneficiaries",
    name: "beneficiaries",
    component: Beneficiaries
  },
  {
    path: "/purposes",
    name: "purposes",
    component: Purposes
  },
  {
    path: "/intelligence",
    name: "intelligence-form",
    component: Intelligence
  },
  {
    path: "/email-form",
    name: "email-form",
    component: EmailForm
  },
  {
    path: "/client-info",
    name: "client-info",
    component: ClientInfo
  },
  {
    path: "/credit-page",
    name: "credit-page",
    component: CreditForm
  },
  {
    path: "/document",
    name: "document",
    component: DocumentPage
  },
  {
    path: "/individual-info",
    name: "individual-info",
    component: individualsForm
  },
  {
    path: "/license-info",
    name: "license-info",
    component: LicenseInfo
  },
  {
    path: "/documents-forms",
    name: "documents-forms",
    component: DocumentsForms
  },
  {
    path: "/kinship-status-forms",
    name: "kinship-status-forms",
    component: KinshipStatus
  },
  {
    path: "/address-form",
    name: "address-form2",
    component: AddressForm
  },
  {
    path: "/document-fogeiner",
    name: "document-fogeiner",
    component: DocumentFogeiner
  },
  {
    path: "/foreign-person",
    name: "foreign-person",
    component: ForeignPerson
  },
  {
    path: "/all-data",
    name: "all-data",
    component: AllData
  },
  {
    path: "/already",
    name: "already",
    component: Already
  },
  {
    path: "/rate",
    name: "rate",
    component: Rate
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
