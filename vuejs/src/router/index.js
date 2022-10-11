import Vue from "vue";
import VueRouter from "vue-router";
import LoanForm from "../views/loan/LoanForm";
import AuthView from '../views/Auth/AuthView.vue'
import Address from '../views/Address/AdressView.vue'
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
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
