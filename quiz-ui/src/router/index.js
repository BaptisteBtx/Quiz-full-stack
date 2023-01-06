import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsPage from '../views/QuestionsPage.vue'
import EndPage from '../views/EndPage.vue'
import AdminPage from '../views/AdminPage.vue'
import AboutPage from '../views/AboutPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomePage
    },
    {
      path: '/start_new_quiz',
      name: 'NewQuiz',
      component: NewQuizPage
    },
    {
      path: '/score',
      name: 'EndPage',
      component: EndPage
    },
    {
      path: '/questions',
      name: 'Questions',
      component: QuestionsPage
    },
    {
      path: '/about',
      name: 'about',
      component: AboutPage
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminPage
    }
  ]
})

export default router
