import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import QuestionsPage from '../views/QuestionsPage.vue'
import EndPage from '../views/EndPage.vue'
import ListQuestionsAdmin from '../views/ListQuestionsAdmin.vue'
import LoginPage from '../views/LoginPage.vue'
import QuestionAdmin from '../views/QuestionAdmin.vue'
import UpdateQuestionAdmin from '../views/UpdateQuestionAdmin.vue'

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
      path: '/login',
      name: 'Login',
      component: LoginPage // TODO : Login Page 
    },
    {
      path: '/list_questions_admin',
      name: 'Liste Questions',
      component: ListQuestionsAdmin // TODO : List Question Admin Page 
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
    }
  ]
})

export default router
