<template>
  <v-app class="bg-grey-lighten-2 overflow-auto">
    <v-app-bar color="primary"> </v-app-bar
    ><v-card class="mt-16">
      <div class="d-flex flex-row mt-16">
        <v-tabs direction="vertical">
          <v-tab
            v-for="item in items"
            :to="item.value"
            :text="item.title"
          ></v-tab
        ></v-tabs>
        <v-row
          ><v-col><NuxtPage /></v-col
        ></v-row></div
    ></v-card>
  </v-app>
</template>

<script setup>
const items = [
  {
    title: "Dashboard",
    value: "/",
  },
  {
    title: "Indicadores",
    value: "products",
  },
];
</script>
