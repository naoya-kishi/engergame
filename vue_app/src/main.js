import Vue from 'vue'
import App from './App'
import router from './router'
// reset css
import 'normalize.css' 

/* Font Awesome */
// https://fontawesome.com/
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCommentDots, faGamepad, faBookmark, faList, faYenSign, faMapMarkerAlt, faDungeon } from '@fortawesome/free-solid-svg-icons'

library.add(faCommentDots, faGamepad, faBookmark, faList, faYenSign, faMapMarkerAlt, faDungeon)

Vue.component('font-awesome-icon', FontAwesomeIcon)
/* ここまで */

Vue.config.productionTip = false

/* eslint-disable no-new */
//! Vueインスタンスを生成
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
