import Vue from "vue";
import VueRouter from "vue-router";
import LoanForm from "../views/loan/LoanForm";
import AuthView from '../views/Auth/AuthView.vue'
import Address from '../views/Address/AdressView.vue'
import Structure from '../views/Structure/StructureForm.vue'
import Intelligence from '../views/intelligence/intelligenceForm.vue'
import StructureGroup from '../views/StructureGroup/StructureGroupForm.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "loan-form",
    component: LoanForm,
  },
  {
    path: "/auth",
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
    path: "/intelligence",
    name: "intelligence-form",
    component: Intelligence
  }
];к

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
