<template>
    <div>
      <v-card class="ma-4" elevation="0">
        <v-toolbar title="Fornecedores" color="blue-grey-lighten-4"></v-toolbar>
        <d-data-table
          :data="suppliers"
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
  const { data: suppliers } = useApi("/supplier/");
  const columns = [
    { title: "Fornecedor", key: "name" },
    { title: "Endereço", key: "address" },
    { title: "CNPJ", key: "cnpj" },
    { title: "Contato", key: "contact" },
  ];
  </script>