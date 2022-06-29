<template>
  <div>
    <div class="columns-is-multiline">
      <div class="column-is-12">
        <h2 class="is-size-2 has-text-centered">Courses</h2>
      </div>

      <form method="get" action="/search">
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

      <!-- <div
        class="column is-3"
        v-for="course in allCourses"
        v-bind:key="course.id"
      >
        <div class="box">
          <h3 class="is-size-4">{{ course.dept_and_number }}</h3>
          <p class="is-size-6 has-text-grey">{{ course.median }}</p>
          <p class="is-size-6 has-text-grey">{{ course.prof }}</p>
          <p class="is-size-6 has-text-grey">{{ course.name }}</p>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script>
// import axios from "axios";

// export default {
//   name: "CourseList",
//   data() {
//     return {
//       allCourses: [],
//     };
//   },
//   components: {},
//   mounted() {
//     this.getCourses();
//   },
//   methods: {
//     getCourses() {
//       axios
//         .get("/api/v1/courses/")
//         .then((response) => {
//           this.allCourses = response.data;
//         })
//         .catch((error) => {
//           console.log(error);
//         });
//     },
//   },
// };
</script>
