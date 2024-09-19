<template>
  <div>
    <v-card class="ma-4" elevation="0">
      <v-toolbar title="Clientes" color="blue-grey-lighten-4"></v-toolbar>
      <d-data-table
        :data="customers"
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
const { data: customers } = useApi("/customer/");
const columns = [
  { title: "Cliente", key: "name" },
  { title: "Telefone", key: "phone" },
  { title: "Endereço", key: "address" },
  { title: "Email", key: "email" },
];
</script>
