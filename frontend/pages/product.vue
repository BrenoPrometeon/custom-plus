<template>
    <div>
      <v-card class="ma-4" elevation="0">
        <v-toolbar title="Produtos" color="blue-grey-lighten-4"></v-toolbar>
        <d-data-table
          :data="products"
          :columns="columns"
          :pagination="{
            defaultPageSize: 15,
            showSizePicker: true,
            pageSizes: [15, 30, 50],
            size: 'small',
            pageSlot: 5,
          }"
          :row-key="(row) => row.id"
          selectable
        ></d-data-table
      ></v-card>
    </div>
  </template>
  <script setup>
  const { data: products } = useApi("/product/");
  const columns = [
    { title: "Produto", key: "name" },
    { title: "Descrição", key: "description" },
    { title: "Categoria", key: "category" },
  ];
  </script>