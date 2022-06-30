<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <p
      class="mx-2 d-flex justify-center text-h2 red--text font-weight-normal text-uppercase title"
    >
      MCSA
    </p>

    <div class="q-pa-md q-gutter-md">
      <div class="row justify-between">
        <q-parallax
          :src="require(`../assets/img/${data.img}`)"
          class="align-center"
          width="100%"
        >
          <!-- <h1 class="text-white">MCSA</h1> -->
        </q-parallax>
      </div>
    </div>
    <p
      class="text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
    >
      About
    </p>
    <!-- see https://quasar.dev/vue-components/card -->
    <div
      class="q-pa-md row items-start q-gutter-md"
      v-for="item in data.info"
      v-bind:key="item.title"
    >
      <q-card class="card">
        <q-img :src="require(`../assets/img/${item.img}`)">
          <div class="text-h5 absolute-bottom text-right">{{ item.title }}</div>
        </q-img>

        <q-card-section
          ><div class="q-pt-none">{{ item.body }}</div></q-card-section
        >
      </q-card>
    </div>
    <p
      class="text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
    >
      选课宝典
    </p>

    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <SearchCourse />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchCourse from "@/components/SearchCourse.vue";
import data from "../assets/json/home.json";
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  data() {
    return {
      data: data,
    };
  },

  components: {
    // HelloWorld,
    SearchCourse,
  },
};
</script>
<!-- see https://quasar.dev/style/color-palette -->
<style lang="sass">
p
  color: $red-8
.card
  width: 100%
  max-width: 250px
</style>
