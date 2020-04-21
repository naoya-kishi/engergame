<template>
  <div id="app">
    <div class="header">
      <Search></Search> <!-- 検索コンポーネント -->
    </div>

    <div class="left-container">
      <div class="user-content">
        <router-link to="/profile">
          <div class="user-profile">
            <div class="user-image">
            </div>
            <div class="user-name">
              Kauzya Sakamoto
            </div>
          </div>
        </router-link>
      </div>
      <div class="menu-conntent">
        <ul class="menu-box">
          <router-link to="/recruit">
            <li class="work-menu">
              <div class="logobox"></div>
              <div class="menu-name">案件一覧</div>
            </li>
          </router-link>
          <router-link to="/like">
          <li class="work-menu">
            <div class="logobox"></div>
            <div class="menu-name">お気に入り</div>
          </li>
          </router-link>
          <router-link to="/chat">
          <li class="work-menu">
            <div class="logobox"></div>
            <div class="menu-name">チャット</div>
          </li>
          </router-link>
          <router-link to="/game">
          <li class="work-menu">
            <div class="logobox"></div>
            <div class="menu-name">ゲーム</div>
          </li>
          </router-link>
        </ul>
      </div>
    </div>

    <div class="container">
      <router-view/> 
    </div>

  </div>
</template>

<script>
import Search from './components/parts/Search.vue'
export default {
  name: 'App',
  data: function(){
    return{
      LoginUser: false // User ログイン判定
    }
  },
  components:{
    Search,
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  height: 789px;
  font-family: "Mplus 1p";
}

/* ! Header CSS */
.header{
  width: 100%;
  height: 64px;
  background-color: #117ee4;
  /* background-color: #FFFFFF; */
}


/* ! left-Container CSS */
.left-container{
  width: 240px;
  height: 88%;
  background-color: #FFFFFF;
  box-shadow: 8px 0px 0px rgb(128, 128, 128);
  display: inline-block;
}
.user-content{
  width: 100%;
  height: 80px;
  background-color: #FFFFFF;
  box-shadow: 2px 4px 8px rgba(128, 128, 128, 0.39);
  color: #506690;
}
.menu-conntent{
  width: 100%;
  height: calc(100% - 80px);
}

/* User アカウント 欄 */
.user-profile{
  width: 92%;
  height: 50px;
  padding: 12px 10px;
  cursor: pointer;
  color: #506690;
  /* background-color: #117ee4; */
}
.user-image{
  width: 60px;
  height: 60px;
  background-color: grey;
  border-radius: 50%;
  display: inline-block;
}
.user-name{
  /* display: inline-block; */
  float: right;
  padding: 20px 0 0 0;
  width: 67%;
  height: 40px;
  /* background-color: red; */
}

/* Menu 欄 */
.menu-box{
  width: 80%;
  height: 250px;
  padding: 0 20px;
}
.work-menu{
  width: 95%;
  height: 40px;
  list-style: none;
  border-radius: 3%;
  margin: 5px 0;
  padding: 5px;
  cursor: pointer;
  color: #506690;
}
.logobox{
  width: 40px;
  height: 40px;
  background-color: grey;
  display: inline-block;
}
.menu-name{
  width: 120px;
  height: 30px;
  /* background-color: yellow; */
  /* display: inline-block;  */
  float: right;
  padding: 10px 0 0 0;
  /* color: #506690; */
}

/* contant */
.container{
  width: calc(1440px - 240px);
  height: calc(811px - 87px);
  background-color: rgb(226, 227, 229);
  /* background-color: #FFFFFF; */
  display: inline-block;
  position: absolute;
  right: 0;
  overflow: scroll;
}

/* action */
.work-menu:hover{
  /* background-color: #117ee4; */
  background-color: rgb(235, 236, 240);
  /* color: #FFFFFF; */
}
.user-profile:hover{
  opacity: 0.8;
}

/* Responsive */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/

}
</style>
