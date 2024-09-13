<template>
  <v-app class="bg-grey-lighten-2 overflow-auto">
    <v-app-bar color="primary"> </v-app-bar
    ><v-card>
      <div class="d-flex flex-row">
        <v-tabs direction="vertical">
          <v-tab
            v-for="item in items"
            :to="item.value"
            :text="item.title"
          ></v-tab
        ></v-tabs>
        <v-tabs-window>
          <v-tabs-window-item>
            <v-card flat><NuxtPage /></v-card></v-tabs-window-item
        ></v-tabs-window></div
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
