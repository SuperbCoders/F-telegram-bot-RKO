import Vue from "vue";
import VueRouter from "vue-router";
import LoanForm from "../views/loan/LoanForm";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "loan-form",
    component: LoanForm,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
