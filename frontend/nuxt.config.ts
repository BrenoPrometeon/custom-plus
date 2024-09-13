export default defineNuxtConfig({
  app: {
      head: {
          title: 'Custom',
      },
      pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: ['d-naive',"@nuxt/icon", "@nuxtjs/apollo"],
  ssr: false,
  css: ['vuetify/lib/styles/main.sass'],

  build: {
      transpile: ['vuetify'],
  },

  apollo: {
    clients: {
      default: {
        httpEndpoint: process.env.API_URL + "graphql",
        tokenStorage: "cookie",
        httpLinkOptions: {
          credentials: "include",
        },
        inMemoryCacheOptions: {
          addTypename: false,
        },
      },
    },
  },

  runtimeConfig: {
      public: {
          apiUrl: process.env.API_URL
      },
  },

  compatibilityDate: '2024-09-09',
})