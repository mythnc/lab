import { createRouter, createWebHistory } from "vue-router";

import About from "@/views/AboutView.vue";
import Home from "@/views/HomeView.vue";
import Manage from "@/views/Manage.vue";

const routes = [
  {
    name: "home",
    path: "/",
    component: Home,
  },
  {
    name: "about",
    path: "/about",
    component: About,
  },
  {
    name: "manage",
    // alias: "/manage",
    path: "/manage-music",
    component: Manage,
    beforeEnter: (to, from, next) => {
      console.log("Pre-Route Guard");
      next();
    },
  },
  {
    path: "/manage",
    redirect: { name: "manage" },
  },
  {
    path: "/:cacthAll(.*)*",
    redirect: { name: "home" },
  },
];
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: "text-yellow-500",
});

router.beforeEach(async (to, from, next) => {
  console.log("Global Guard");
  next();
});

export default router;
