// import SignUp from './components/SignUp.vue'
// import LoginPage from './components/LoginPage.vue'
import LandingPage from './components/LandingPage.vue'
import { createRouter, createWebHistory } from 'vue-router'
import TeamSummary from "@/components/TeamSummary.vue";
import PlayerComparison from "@/components/PlayerComparison.vue";
import SignIn from './components/SignIn.vue'
const routes = [
    {
        name: 'LandingPage',
        component: LandingPage,
        path: '/',
    },
    {
        name: 'TeamSummary',
        component: TeamSummary,
        path: "/team-summary/:teamId",
        props: true
    },
    {
        name: 'PlayerComparison',
        component: PlayerComparison,
        path: "/player-comparison"
    },
    {
        name: 'SignIn',
        component: SignIn,
        path: '/SignIn',
    },
    // {
    //     name: 'SignUp',
    //     component: SignUp,
    //     path: '/sign-up',
    // },
    // {
    //     name: 'LoginPage',
    //     component: LoginPage,
    //     path: '/log-in'
    // }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router