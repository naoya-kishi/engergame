import Vue from 'vue'
import Router from 'vue-router'

//! コンポーネント
import Game from '@/components/pages/Game.vue'
import Recruit from '@/components/pages/Recruit.vue'
import Like from '@/components/pages/Like.vue'
import Chat from '@/components/pages/Chat.vue'
import Profile from '@/components/pages/Profile.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/game',
      name: 'Game',
      component: Game
    },
    { 
      path: '/recruit',
      component: Recruit
    },
    {
      path: '/like',
      component: Like
    },
    {
      path: '/chat',
      component: Chat
    },
    {
      path: '/profile',
      component: Profile
    }
  ]
})
