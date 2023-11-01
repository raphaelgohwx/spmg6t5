// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '',
    component: () => import('@/views/Home.vue'),
    // children: [
    //   {
    //     path: '',
    //     name: 'Home',
    //     // route level code-splitting
    //     // this generates a separate chunk (about.[hash].js) for this route
    //     // which is lazy-loaded when the route is visited.
    //     component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
    //   },
    // ],
  },
  {
    path:'/staff',
    component: () => import('@/views/staff.vue'),
    name:'staff'
  },
  {
    path:'/hr',
    component: () => import('@/views/hr.vue'),
    name:'hr'
  },
  {
    path:'/manager',
    component: () => import('@/views/manager.vue'),
    name:'manager'
  },
  {
    path:'/roleCreation',
    component: () => import('@/views/RoleCreation.vue'),
    name:'roleCreation'
  },
  {
    path:'/updateRole/:id',
    component: () => import('@/views/UpdateRole.vue'),
    name:'updateRole',
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
