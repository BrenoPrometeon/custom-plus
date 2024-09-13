<template>
  <div><v-card class="bg-primary">PAULO VIADO</v-card>{{ customers }}{{ result }}</div>
</template>
<script setup>
const query = gql`
  query MyQuery {
    customers {
      address
      email
      id
      name
      phone
    }
  }
`;

const { result } = useQuery(query)
const { data: customers} = useApi('/customer/')
console.log(result.value)
</script>
