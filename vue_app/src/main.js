import Vue from 'vue'
import App from './App'
import router from './router'
// reset css
import 'normalize.css' 

Vue.config.productionTip = false

/* eslint-disable no-new */
//! Vueインスタンスを生成
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


