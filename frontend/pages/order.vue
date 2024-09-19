<template>
  <div>
    <v-card class="ma-4" elevation="0">
      <v-toolbar title="Vendas" color="blue-grey-lighten-4"></v-toolbar>
      <d-data-table
        :data="
          orders?.map((row) => ({
            ...row,
            client: clients[row.client_id],
            product: products[row.product_id],
          }))
        "
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
const { data: orders } = useApi("/order/");
const { data: customers } = useApi("/customer/");
const { data: product } = useApi("/product/");

const clients = computed(() => {
  let client = {};
  customers.value?.forEach((item) => {
    client[item.id] = item.name;
  });
  return client;
});

const products = computed(() => {
  let productDict = {};
  product.value?.forEach((item) => {
    productDict[item.id] = item.name;
  });
  return productDict;
});

const columns = [
  { title: "Cliente", key: "client" },
  { title: "Produto", key: "product" },
  { title: "Quantidade", key: "quantity" },
  { title: "Preço", key: "price" },
  { title: "Pagamento", key: "payment" },
  { title: "Data de Venda", key: "order_date", type: 'date' },
  { title: "Data da Entrega", key: "delivery_date", type: 'date' },
  { title: "Desconto", key: "discount" },
];
</script>
