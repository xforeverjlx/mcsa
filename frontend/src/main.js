import axios from "axios";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { Quasar } from "quasar";
import quasarUserOptions from "./quasar-user-options";

axios.defaults.baseURL = "http://127.0.0.1:8000";

createApp(App)
  .use(Quasar, quasarUserOptions)
  .use(store)
  .use(router, axios)
  .mount("#app");
