import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsPage from '../views/QuestionsPage.vue'
import EndPage from '../views/EndPage.vue'
import QuestionAdmin from '../views/QuestionAdmin.vue'
import UpdateQuestionAdmin from '../views/UpdateQuestionAdmin.vue'
import AdminPage from '../views/AdminPage.vue'

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
      path: '/end_page',
      name: 'EndPage',
      component: EndPage
    },
    {
      path: '/questions',
      name: 'Questions',
      component: QuestionsPage // TODO : Questions Page (questions)
    },
    {
      path: '/question_admin',
      name: 'Question',
      component: QuestionAdmin // TODO : Question Admin Page 
    },
    {
      path: '/update_question_admin',
      name: 'Update Question',
      component: UpdateQuestionAdmin // TODO : Update Question Admin Page 
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminPage
    }
  ]
})

export default router
