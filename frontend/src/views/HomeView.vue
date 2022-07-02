<template>
  <!-- <div class="home" style="background-color: #0b141c"> -->
  <div class="home" style="background-color: rgb(255, 255, 255)">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->

    <div>
      <!-- <div
        class="white-box"
        v-bind:style="{
          background: 'rgba(0,0,0,' + computedOpacity + ')',
        }"
      > -->
      <!-- <div class="white-box" v-bind:style="{ opacity: computedOpacity }"> -->
      <div class="row justify-between">
        <q-parallax class="align-center" :height="p_height">
          <template v-slot:media>
            <img
              :src="require(`../assets/img/${data.img}`)"
              img-class="parrallax"
              class="parallax"
              v-bind:style="{ opacity: computedOpacity }"
            />
          </template>
          <p
            class="mx-2 d-flex justify-center text-h2 white--text font-weight-normal text-uppercase title"
          >
            M C S A
          </p>

          <p
            class="text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
          >
            About
          </p>
          <div class="row">
            <p class="on-right">{{ data.description }}</p>
          </div>
          <!-- see https://quasar.dev/vue-components/card -->

          <!-- <div
      class="q-pa-md row items-start q-gutter-md"
      v-for="item in data.info"
      v-bind:key="item.title"
    > -->

          <div class="row justify-center q-pa-xl q-gutter-xl items-center">
            <div v-for="item in data.info" v-bind:key="item.title">
              <div class="col">
                <q-card class="card">
                  <q-img
                    :src="require(`../assets/img/${item.img}`)"
                    :ratio="16 / 9"
                    style="width: 400px"
                  >
                    <div class="text-h5 absolute-bottom text-right">
                      {{ item.title }}
                    </div>
                  </q-img>

                  <q-card-section
                    ><div class="q-pt-none">
                      {{ item.body }}
                    </div></q-card-section
                  >
                </q-card>
              </div>
            </div>
          </div>
          <div class="row">
            <router-link to="/search"
              ><p
                class="text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
              >
                选课宝典
              </p></router-link
            >
          </div>
        </q-parallax>
      </div>
    </div>
    <!-- <div class="row"> -->
    <!-- <SearchCourse /> -->
    <!-- </div> -->
  </div>

  <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  <!-- </div> -->
</template>

<script>
// @ is an alias to /src
// import SearchCourse from "@/components/SearchCourse.vue";
import data from "../assets/json/home.json";
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  data() {
    return {
      p_opacity: 0.9,
      p_height: 2800,
      data: data,
    };
  },

  components: {
    // HelloWorld,
    // SearchCourse,
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  unmounted() {
    window.removeEventListener("scroll", this.onScroll);
  },
  computed: {
    computedOpacity() {
      return this.p_opacity;
    },
  },
  methods: {
    onScroll() {
      var scrollTop = window.top.scrollY;
      // console.log(scrollTop);
      var elementHeight = this.p_height;
      // this.p_opacity = 0.1;
      this.p_opacity = Math.max(
        0.3,
        1 - (1 - (elementHeight - 2 * scrollTop) / elementHeight) * 0.8
      );
      // this.p_opacity = 0;
      // console.log((elementHeight - 10 * scrollTop) / elementHeight);
    },
  },
};
</script>
<!-- see https://quasar.dev/style/color-palette -->
<style lang="sass">
p
  color: #0b141c


.white-box
  position: absolute
  top: 0
  left: 0
  width: 100%
  height: 100%
  background: rgb(0,0,0)
  opacity: 0.9


.parallax
  filter: blur(0px)
  -webkit-filter: blur(0px)
</style>
