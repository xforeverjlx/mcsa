<template>
  <!-- <q-layout>
    <q-layout-header> -->
  <div class="q-pa-md" style="background-color: #0b141c">
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
      <q-btn flat label="Homepage" />

      <q-space></q-space>
      <q-tabs v-model="tab" shrink>
        <q-tab name="tab1" label="Search" />
        <q-tab name="tab2" label="About" />
      </q-tabs>
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
