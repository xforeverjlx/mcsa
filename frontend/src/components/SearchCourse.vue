<template>
  <div class="page-search">
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

    <div class="columns is-multiline">
      <!-- <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">
          Search term: "{{ query }}" with "{{ className }}" in its name, taught
          by "{{ prof }}" during the "{{ offered }}" with a median of at
          least"{{ median }}"
        </h2>
      </div> -->

      <div class="q-pa-md">
        <q-table
          class="sticky-header-table"
          virtual-scroll
          :rows-per-page-options="[0]"
          title="Courses"
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
  },
  {
    name: "median",
    label: "Median",
    field: (row) => row.median,
    sortable: true,
    // sortOrder: "da",
    sort: (a, b) => dict[a] - dict[b],
  },
];
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
      className: "",
      // toSearch: false,
      columns,
      user: {
        inputs: [],
      },
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
