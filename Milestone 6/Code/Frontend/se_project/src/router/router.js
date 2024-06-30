import LandingPage from '../components/landing_page.vue'

import {createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        path: '/',
        name: 'LandingPage',
        component: LandingPage
    }
]

const router=createRouter({
    history:createWebHistory(),
    routes
})

export default router