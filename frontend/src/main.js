import { createApp } from 'vue'
import App from './App.vue'
import { routers } from './routers/index.js'
import "./assets/scss/global.scss";
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'


createApp(App)
.component('VueSlider', VueSlider)
.use(routers)
.mount('#app')




