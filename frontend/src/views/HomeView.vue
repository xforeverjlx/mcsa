<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <CourseList />
  </div>
</template>

<script>
// @ is an alias to /src
import CourseList from "@/components/CourseList.vue";
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",

  components: {
    HelloWorld,
    CourseList,
  },
};
</script>
