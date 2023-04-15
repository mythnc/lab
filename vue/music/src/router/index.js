import { createRouter, createWebHistory } from "vue-router";

import About from "@/views/AboutView.vue";
import Home from "@/views/HomeView.vue";
import Manage from "@/views/Manage.vue";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/about",
    component: About,
  },
  {
    path: "/manage",
    component: Manage,
  },
];
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
