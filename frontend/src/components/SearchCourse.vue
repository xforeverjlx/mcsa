<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">
          Search term: "{{ query }}" taught by "{{ prof }}" during the "{{
            offered
          }}" with a median of at least"{{ median }}"
        </h2>
      </div>

      <div class="column is-3" v-for="course in courses" v-bind:key="course.id">
        <div class="box">
          <h3 class="is-size-4">{{ course.dept_and_number }}</h3>
          <p class="is-size-6 has-text-grey">{{ course.median }}</p>
          <p class="is-size-6 has-text-grey">{{ course.prof }}</p>
          <p class="is-size-6 has-text-grey">{{ course.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SearchCourse",
  data() {
    return {
      courses: [],
      query: "",
      prof: "",
      offered: "",
      median: "",
      name: "",
      // toSearch: false,
    };
  },
  mounted() {
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      // toSearch = true;
    }
    if (params.get("offered")) {
      this.offered = params.get("offered");
      // toSearch = true;
    }
    if (params.get("prof")) {
      this.prof = params.get("prof");
      // toSearch = true;
    }
    if (params.get("median")) {
      this.median = params.get("median");
      // toSearch = true;
    }
    if (params.get("name")) {
      this.name = params.get("name");
    }
    this.performSearch();
    // if (this.toSearch) {
    //   this.toSearch = false;
    //   this.performSearch();
    // }
  },
  methods: {
    async performSearch() {
      await axios
        .post("/api/v1/courses/search/", {
          query: this.query,
          offered: this.offered,
          prof: this.prof,
          median: this.median,
          name: this.name,
        })
        .then((response) => {
          this.courses = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
