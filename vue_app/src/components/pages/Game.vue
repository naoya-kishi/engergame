<template>
  <div class="game-wraper">
    <div class="top-title">
      <!-- <img class="game-img" :src="assetsImage"/> -->
    </div>
  </div>
</template>

<script>
import Game from "@/assets/game.png";
export default {
  name: 'Game',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      text: 'Test data',
      showText: true,
      assetsImage: Game,
      assetsImage_NG: "../assets/game.png",
      staticImage: "/game.png"
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
.game-wraper{
  width: 90%;
  height: 100%;
  background-color: rgb(255, 255, 255);
  box-shadow: 10px 5px 5px grey;
  margin: 0 auto;
}
.top-title{
  width: 60%;
  padding: 0 100px;
  margin: 20px auto;
}
.game-img{
  /* width: 100%; */
  max-width: 100%;
  margin: 20px auto;
  text-align:center;
  /* height: 80%; */
  list-style: none;
}

/* Responsive */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/
  
}
</style>
