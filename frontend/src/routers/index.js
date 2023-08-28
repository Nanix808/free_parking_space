import {createRouter, createWebHistory} from "vue-router"

export const routers = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'first', component: () => import('@/views/FirstPage.vue') },
    { path: '/settings', name: 'settings', component: () => import('@/views/SettingsPage.vue') },
    
  ],
})