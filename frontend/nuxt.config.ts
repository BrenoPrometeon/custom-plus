export default defineNuxtConfig({
  app: {
      head: {
          title: 'Custom',
      },
      pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: ['d-naive',"@nuxt/icon"],
  ssr: false,
  css: ['vuetify/lib/styles/main.sass'],

  build: {
      transpile: ['vuetify'],
  },

  runtimeConfig: {
      public: {
          apiUrl: process.env.API_URL
      },
  },

  compatibilityDate: '2024-09-09',
})