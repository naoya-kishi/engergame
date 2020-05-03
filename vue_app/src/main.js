import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios' //Axios バックエンド側のデータ処理
import VuePaginate from 'vue-paginate';
import Vuex from 'vuex'

Vue.use(Vuex)
// reset css
import 'normalize.css' //ResetCss

/* Font Awesome */
// https://fontawesome.com/
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCommentDots, faGamepad, faBookmark, faList, faYenSign, faMapMarkerAlt, faDungeon } from '@fortawesome/free-solid-svg-icons'

library.add(faCommentDots, faGamepad, faBookmark, faList, faYenSign, faMapMarkerAlt, faDungeon)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(VuePaginate);
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



