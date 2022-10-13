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
import Rate from '../views/Rate/RateForm.vue'
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
    name: "address-form",
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
    path: "/intelligence",
    name: "intelligence-form",
    component: Intelligence
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
