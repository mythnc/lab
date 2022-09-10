<template>
  <select name="" id="" v-model="currentTab">
    <option value="Home">Home</option>
    <option value="About">About</option>
  </select>
  <KeepAlive>
    <component :is="currentTab"></component>
  </KeepAlive>
</template>

<script>
import Home from "@/components/Home.vue";
import About from "@/components/About.vue";

export default {
  name: "App",
  components: {
    Home,
    About,
  },
  data() {
    return {
      currentTab: "Home",
    };
  },
};
</script>
