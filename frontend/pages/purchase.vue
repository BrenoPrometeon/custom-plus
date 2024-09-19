<template>
  <div>
    <v-card class="ma-4" elevation="0">
      <v-toolbar title="Compras" color="blue-grey-lighten-4"></v-toolbar>
      <d-data-table
        :data="
          purchases?.map((row) => ({
            ...row,
            product: products[row.product_id],
            supplier: suppliers[row.supplier_id],
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
const { data: purchases } = useApi("/purchase/");
const { data: supplier } = useApi("/supplier/");
const { data: product } = useApi("/product/");

const products = computed(() => {
  let productDict = {};
  product.value?.forEach((item) => {
    productDict[item.id] = item.name;
  });
  return productDict;
});

const suppliers = computed(() => {
  let supplierDict = {};
  supplier.value?.forEach((item) => {
    supplierDict[item.id] = item.name;
  });
  return supplierDict;
});

const columns = [
  { title: "Produto", key: "product" },
  { title: "Fornecedor", key: "supplier" },
  { title: "Quantidade", key: "quantity" },
  { title: "Preço", key: "price" },
  { title: "Forma de Pagamento", key: "payment_method" },
  { title: "Data", key: "purchase_date", type: "date" },
];
</script>
