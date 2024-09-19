<template>
  <v-app class="bg-grey-lighten-2 overflow-auto">
    <v-app-bar color="primary">
      <template v-slot:prepend>
        <Icon name="carbon:area-custom" size="30" class="ml-4"/>
      </template>
      <v-app-bar-title class="text-uppercase">Custom</v-app-bar-title> </v-app-bar
    ><v-card>
      <div class="d-flex flex-row mt-16">
        <v-tabs direction="vertical">
          <v-tab
            v-for="item in items"
            color="primary"
            :prepend-icon="item.icon"
            :to="item.value"
            :text="item.title"
          ></v-tab
        ></v-tabs>
        <v-divider vertical></v-divider>
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
    icon: "mdi-chart-bar-stacked",
  },
  {
    title: "Clientes",
    value: "customer",
    icon: "mdi-account-multiple",
  },
  {
    title: "Produtos",
    value: "product",
    icon: "mdi-package-variant-closed",
  },
  {
    title: "Vendas",
    value: "order",
    icon: "mdi-handshake-outline",
  },
  {
    title: "Estoque",
    value: "stock",
    icon: "mdi-grid-large",
  },
  {
    title: "Compras",
    value: "purchase",
    icon: "mdi-cash-multiple",
  },
  {
    title: "Fornecedores",
    value: "supplier",
    icon: "mdi-domain",
  },
];
</script>
