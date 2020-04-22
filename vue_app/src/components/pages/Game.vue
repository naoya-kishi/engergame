<template>
  <div class="game">
    game一覧画面
  </div>
</template>

<script>
// import Battle from "@/assets/battle.png";
export default {
  name: 'Game',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      text: 'Test data',
      showText: true,
      // assetsImage: Battle,
      // assetsImage_NG: "../assets/battle.jpg",
      // staticImage: "/battle.jpg"
    }
  },
  methods: {
    toggle: function(){
      this.showText = !this.showText
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}


/* Responsive */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/
  
}
</style>
