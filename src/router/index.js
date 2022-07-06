import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Singin from "../views/Signin.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },
  {
    path: "/signin",
    name: "Signin",
    component: Singin,
  },
  {
    path: "/home",
    name: "Home",
    component: () => import(/* webpackChunkName: "Home" */ "../views/Home.vue"),
  },
  {
    path: "/guardados",
    name: "Guardados",
    component: () =>
      import(/* webpackChunkName: "Guardados" */ "../views/Guardados.vue"),
  },
  {
    path: "/perfil",
    name: "Perfil",
    component: () =>
      import(/* webpackChunkName: "Perfil" */ "../views/Perfil.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
