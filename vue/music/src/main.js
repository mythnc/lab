import "./assets/base.css";
import "./assets/main.css";

import { createPinia } from "pinia";
import { createApp } from "vue";

import App from "./App.vue";
import { auth } from "./includes/firebase";
import VeeValidatePlugin from "./includes/validation";
import router from "./router";

let app;

auth.onAuthStateChanged(() => {
  if (!app) {
    const app = createApp(App);

    app.use(createPinia());
    app.use(router);
    app.use(VeeValidatePlugin);

    app.mount("#app");
  }
});
