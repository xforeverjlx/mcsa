<template>
  <!-- <div class="home" style="background-color: #0b141c"> -->
  <!-- <div class="home" style="background-color: rgb(255, 255, 255)"> -->
  <div
    class="home"
    style="background-image: linear-gradient(#033159, rgb(255, 255, 255))"
  >
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->

    <div>
      <!-- <div
        class="white-box"
        v-bind:style="{
          background: 'rgba(0,0,0,' + computedOpacity + ')',
        }"
      > -->
      <!-- <div class="white-box" v-bind:style="{ opacity: computedOpacity }"> -->
      <div class="row">
        <div class="col full-height full-width text-center">
          <div class="mcsa">
            <!-- see http://web.simmons.edu/~grabiner/comm244/weekthree/css-basic-properties.html -->
            <p
              class="absolute-center white--text font-weight-normal text-uppercase title"
            >
              M C S A
            </p>
          </div>
        </div>

        <q-parallax class="align-center" :height="p_height">
          <template v-slot:media>
            <img
              :src="require(`../assets/img/${data.img}`)"
              img-class="parrallax"
              class="parallax"
              v-bind:style="{ opacity: computedOpacity }"
              background-blend-mode="multiply"
            />
          </template>
          <div class="row full-width fixed-top">
            <NavBar />
            <router-view />
          </div>
          <div class="row" style="height: 1000px"></div>
          <div class="row q-gutter-y-xl">
            <div class="about">
              <p
                class="about text-h2 font-weight-medium text-uppercase text-center mt-16 primary--text"
              >
                About
              </p>
            </div>
          </div>
          <div class="desc row">
            <p class="on-right">{{ data.description }}</p>
          </div>
          <!-- see https://quasar.dev/vue-components/card -->

          <!-- <div
      class="q-pa-md row items-start q-gutter-md"
      v-for="item in data.info"
      v-bind:key="item.title"
    > -->

          <div class="row justify-center q-pa-xl q-gutter-xl">
            <div v-for="item in data.info" v-bind:key="item.title">
              <div class="col">
                <q-card class="card text-white" style="background: #0b141c">
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
          <div class="row" style="height: 100px"></div>
          <div class="row">
            <router-link to="/search" style="text-decoration: none"
              ><p
                class="toSearch text-h3 justify-center font-weight-medium text-uppercase text-center mt-16 primary--text"
              >
                &gt;&gt; Search Courses &lt;&lt;
              </p></router-link
            >
          </div>
          <div class="row" style="height: 200px"></div>
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
import NavBar from "../components/NavBar.vue";
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  data() {
    return {
      p_opacity: 0.3,
      p_height: 1900,
      data: data,
    };
  },

  components: {
    NavBar,
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
      this.p_opacity = Math.max(
        0.1,
        0.3 - (1 - (elementHeight - 2 * scrollTop) / elementHeight) * 0.8
      );
      // this.p_opacity = 0.1;
      console.log(this.p_opacity);
    },
  },
};
</script>
<!-- see https://quasar.dev/style/color-palette -->
<style lang="sass">
.desc
  font-size:18px

.toSearch
  color: #0b141c

.mcsa
  color: #fff
  font-size: 120px

.about
  font-size:100px
  color: #0b141c
  font-weight: bold

.white-box
  position: absolute
  top: 0
  left: 0
  width: 100%
  height: 100%

  opacity: 0.9

.card
  width: 100%
  max-width: 400px

.parallax
  filter: blur(0px)
  -webkit-filter: blur(0px)
</style>
