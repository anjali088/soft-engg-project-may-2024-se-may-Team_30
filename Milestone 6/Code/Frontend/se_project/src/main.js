import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

createApp(App).use(router).use(router).mount('#app')
