<template>
  <!-- <q-layout>
    <q-layout-header> -->
  <div class="full-width q-pa-md">
    <!-- <div class="q-pa-md"> -->
    <!-- <div class="q-pa-md" style="background-color: #0b141c"> -->
    <!-- <div
    class="q-pa-md"
    style="background-image: linear-gradient(#0b141c, rgb(255, 255, 255))"
  > -->
    <q-toolbar class="text-white">
      <!-- <q-btn flat dense round aria-label="Menu">
        <q-icon name="menu" />
      </q-btn> -->
      <img
        class="ml-2"
        height="30"
        alt="Company logo"
        src="../assets/logo.png"
      />
      <q-btn flat label="Homepage" to="/" />

      <q-space />
      <q-btn flat label="Search" to="/search" />
      <!-- <q-tabs v-model="tab" shrink>
        <q-tab name="tab1" label="Search" to="/search" />
      </q-tabs>-->
    </q-toolbar>
  </div>
  <!-- </q-layout-header>
  </q-layout> -->
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    return {
      tab: ref(""),
    };
  },
};
</script>
