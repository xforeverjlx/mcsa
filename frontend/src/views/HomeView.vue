<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />

    <div class="columns-is-multiline">
      <div class="column-is-12">
        <h2 class="is-size-2 has-text-centered">Courses</h2>
      </div>
      <div
        class="column is-3"
        v-for="course in allCourses"
        v-bind:key="course.id"
      >
        <div class="box">
          <h3 class="is-size-4">{{ course.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ course.median }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      allCourses: [],
    };
  },
  components: {
    HelloWorld,
  },
  mounted() {
    this.getCourses();
  },
  methods: {
    getCourses() {
      axios
        .get("/api/v1/courses/")
        .then((response) => {
          this.allCourses = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
