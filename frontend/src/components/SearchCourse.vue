<template>
  <!-- <div class="page-search" style="background-color: #0b141c"> -->
  <div
    class="page-search"
    style="background-image: linear-gradient(#033159, rgb(255, 255, 255))"
  >
    <!-- <div class="row" style="height: 100px"></div> -->
    <div class="row full-width">
      <NavBar />
      <router-view />
    </div>
    <div class="row text-white justify-center q-pa-sm">
      <p
        class="text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
      >
        Search Courses
      </p>
    </div>
    <div class="row justify-center">
      <form method="get" action="/search">
        <!-- <form method="get" action=""> -->
        <div class="field has-addons">
          <div class="control">
            <input
              type="text"
              class="input"
              placeholder="Class name"
              name="className"
            />
            <input
              type="text"
              class="input"
              placeholder="Class number"
              name="query"
            />
            <input
              type="text"
              class="input"
              placeholder="Class prof"
              name="prof"
            />
            <select name="offered">
              <option value="">Anytime</option>
              <option value="Fall">FA</option>
              <option value="Spring">SP</option>
            </select>

            <!-- <q-select
              as-input
              borderless
              :options="options"
              label="Borderless"
              style="width: 120px"
            /> -->
            <select name="median">
              <option value="any">Any</option>
              <option value="A+">A+</option>
              <option value="A">A</option>
              <option value="A-">A-</option>
              <option value="B+">B+</option>
            </select>
          </div>

          <div class="control">
            <button class="button is-success">search</button>
          </div>
        </div>
      </form>
    </div>

    <div class="columns is-multiline">
      <!-- <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">
          Search term: "{{ query }}" with "{{ className }}" in its name, taught
          by "{{ prof }}" during the "{{ offered }}" with a median of at
          least"{{ median }}"
        </h2>
      </div> -->

      <div class="q-pa-sm">
        <div class="row text-white on-left" style="height: 20px">
          <p>
            *Note: Course info from Class Roster, medians from Reddit, Prof info
            from RateMyProf, class difficulties from CUReviews
          </p>
        </div>
        <q-table
          class="sticky-header-table"
          virtual-scroll
          :rows-per-page-options="[0]"
          :rows="courses"
          :columns="columns"
          :separator="vertical"
          row-key="Class Number"
          wrap-cells
        />
      </div>
      <!-- <div class="column is-3" v-for="course in courses" v-bind:key="course.id">
          <div class="box">
            <h3 class="is-size-4">{{ course.dept_and_number }}</h3>
            <p class="is-size-6 has-text-grey">{{ course.median }}</p>
            <p class="is-size-6 has-text-grey">{{ course.prof }}</p>
            <p class="is-size-6 has-text-grey">{{ course.name }}</p>
          </div>
        </div> -->

      <!-- <q-markup-table :separator="vertical" flat bordered dense>
       
        <thead>
          <th class="text-left" style="max-width: 318px">Class Name</th>
          <th class="text-right">Class Number</th>
          <th class="text-right">Professor</th>
          <th class="text-right">Median</th>
        </thead>
        <tbody>
          <div
            class="column is-3"
            v-for="course in courses"
            v-bind:key="course.id"
          >
            <tr>
              <td class="text-left">{{ course.name }}</td>
              <td class="text-right">{{ course.dept_and_number }}</td>
              <td class="text-right">{{ course.prof }}</td>
              <td class="text-right">{{ course.median }}</td>
            </tr>
          </div>
        </tbody>
      </q-markup-table> -->
    </div>
  </div>
</template>

<script>
var dict = {
  "A+": 10,
  A: 9,
  "A-": 8,
  "B+": 7,
  B: 6,
  "B-": 5,
  "C+": 4,
  C: 3,
  "C-": 2,
  "": 1,
};
const columns = [
  {
    name: "dept_and_number",
    label: "Class Number",
    field: (row) => row.dept_and_number,
    style: "background-color: #EAFAF1",
  },
  {
    name: "name",
    label: "Name",
    align: "left",
    field: (row) => row.name,
  },
  {
    name: "prof",
    label: "Professor",
    field: (row) => row.prof,
    style: "background-color: #EAFAF1",
  },
  {
    name: "prereq",
    label: "Pre-Requisite",
    field: (row) => row.prereqs,
  },
  {
    name: "starttime",
    label: "Start Time",
    field: (row) => row.start_time,
  },
  {
    name: "endtime",
    label: "End Time",
    field: (row) => row.end_time,
  },
  {
    name: "offered",
    label: "Availability",
    field: (row) => row.offered,
  },
  {
    name: "median",
    label: "Median",
    field: (row) => row.median,
    sortable: true,
    // sortOrder: "da",
    sort: (a, b) => dict[a] - dict[b],
    style: "background-color: #EAFAF1",
  },
  {
    name: "median_semester",
    label: "Semester of Median",
    field: (row) => row.median_semester,
    style: "background-color: #EAFAF1",
  },
  {
    name: "median_prof",
    label: "Prof of Median",
    field: (row) => row.median_prof,
    style: "background-color: #EAFAF1",
  },
  {
    name: "prof_diff",
    label: "Prof's Difficulty",
    field: (row) => row.prof_diff,
  },
  {
    name: "prof_rating",
    label: "Prof's Rating",
    field: (row) => row.prof_rating,
  },
  {
    name: "prof_num_rating",
    label: "Prof's # of Ratings",
    field: (row) => row.prof_num_rating,
  },
  {
    name: "class_diff",
    label: "Class' Difficulty",
    field: (row) => row.class_diff,
  },
  {
    name: "class_rating",
    label: "Class' Rating",
    field: (row) => row.class_rating,
  },
  {
    name: "class_workload",
    label: "Class' Workload",
    field: (row) => row.class_workload,
  },
];
import axios from "axios";
import NavBar from "../components/NavBar.vue";

export default {
  name: "SearchCourse",
  components: { NavBar },
  data() {
    return {
      courses: [],
      query: "",
      prof: "",
      offered: "",
      median: "",
      className: "",
      // toSearch: false,
      columns,
      user: {
        inputs: [],
      },
      options: ["FA", "SP"],
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
    if (params.get("className")) {
      this.className = params.get("className");
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
          className: this.className,
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

<style lang="sass">

.sticky-header-table
  /* height or max-height is important */
  height: 750px

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #c1f4cd

  thead tr th
    position: sticky
    z-index: 1
  thead tr:first-child th
    top: 0

  /* this is when the loading indicator appears */
  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px
</style>
