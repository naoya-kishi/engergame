<template>
  <div id="app">
    <div class="header">
      <Search></Search> <!-- 検索コンポーネント -->
      <div class="user-box">
        <div class="user-icon">
          <div class="top-user-profile"></div>
        </div>
      </div>
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
          <router-link to="/recruit" class="link-spa">
            <li class="work-menu">
              <div class="logobox"><div class="logobox"><font-awesome-icon icon="list" class="awesome-icon"/></div></div>
              <div class="menu-name">案件一覧</div>
            </li>
          </router-link>
          <router-link to="/like" class="link-spa"> 
          <li class="work-menu">
            <div class="logobox"><font-awesome-icon icon="bookmark" class="awesome-icon"/></div>
            <div class="menu-name">お気に入り</div>
          </li>
          </router-link>
          <router-link to="/chat" class="link-spa">
          <li class="work-menu">
            <div class="logobox"><font-awesome-icon icon="comment-dots" class="awesome-icon"/></div>
            <div class="menu-name">チャット</div>
          </li>
          </router-link>
          <router-link to="/game" class="link-spa">
          <li class="work-menu">
            <div class="logobox"><font-awesome-icon icon="gamepad" class="awesome-icon"/></div>
            <div class="menu-name">ゲーム</div>
          </li>
          </router-link>
          <!-- <router-link to="/game" class="link-spa"> -->
          <li class="work-menu" style="cursor: no-drop;">
            <div class="logobox"><font-awesome-icon icon="dungeon" class="awesome-icon"/></div>
            <div class="menu-name">ギルド</div>
          </li>
          <!-- </router-link> -->
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
  /* background-color: #1f5abc; */
  background: linear-gradient(#1f5ae8, #2ac1df);
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
  font-size: 14px;
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
  box-shadow: 0 0 3px 0 rgba(255, 255, 255, 0.12), 0 2px 3px 0 rgba(255, 255, 255, 0.22);
	transition: .3s;
}
.logobox{
  width: 40px;
  height: 40px;
  margin-top: 5px;
  /* background-color: grey; */
  display: inline-block;
}
.menu-name{
  width: 120px;
  height: 30px;
  /* background-color: yellow; */
  /* display: inline-block;  */
  float: right;
  padding: 12px 0 0 0;
  /* color: #506690; */
  font-size: 14px;
}

/* contant */
.container{
  width: calc(1440px - 240px);
  /* height: calc(811px - 87px); */
  height: 95%;
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
  box-shadow: 0 15px 30px -5px rgba(0,0,0,.15), 0 0 5px rgba(0,0,0,.1);
	transform: translateY(-4px);
  /* color: #FFFFFF; */
}
.user-profile:hover{
  opacity: 0.7;
}

/* icon アイコン */
.awesome-icon{
  color: #1f5abc;
  width: 30px;
  height: 30px;
}

/* Responsive */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/
  #app{
    width: 100vw;
    height: 100vh;
    /* background-color: #1f5abc; */
    position: relative;
  }
  .link-spa{
    width: 65px;
    height: 50px;
    /* margin-right: 5px; */
    /* background-color: red; */
  }
  .header{
    width: 100%;
    height: 62px;
  }
  .user-box{
    width: 100px;
    height: 100%;
  }
  .user-icon{
    width: 50px;
    height: 70%;
    padding: 10px;
  }
  .top-user-profile{
    border-radius: 50%;
    width: 45px;
    height: 45px;
    background-color: #506690;
  }

  /* bottom_bar */
  .left-container{
    width: 100%;
    height: 68px;
    position: absolute;
    bottom: 0;
    z-index: 100;
  }
  .user-content{
    width: 100%;
    height: 80px;
    background-color: #FFFFFF;
    box-shadow: 2px 4px 8px rgba(128, 128, 128, 0.39);
    color: #506690;
    display: none;
  }
  .user-profile{
    width: 92%;
    height: 50px;
    padding: 12px 10px;
    cursor: pointer;
    color: #506690;
    display: none;
  }
  .user-image{
    width: 60px;
    height: 60px;
    background-color: grey;
    border-radius: 50%;
    display: inline-block;
    display: none;
  }
  .user-name{
    float: right;
    padding: 20px 0 0 0;
    width: 67%;
    height: 40px;
    display: none;
  }

  .menu-content{
    width: 100%;
    height: 100px;
  }
  .menu-box{
    display: flex;
    height: 30px;
    /* background-color: rgba(0, 128, 0, 0.377); */
  }
  .work-menu{
    display: inline-block;
    width: 74px;
    height: 45px;
    /* margin: 0px 10px 0 20px; */
    /* margin: 0px 5px 0px 5px; */
    margin-left: 2px;
    padding: 0;
    top:0;
    background-color: #FFFFFF;
    /* position: absolute; */
  }
  .logobox{
    width: 40px;
    height: 40px;
    display: inline-block;
    margin: 0 10px 0 10px;
  }
  .menu-name{
    width: 80px;
    height: 20px;
    font-size: 12px;
    text-align: center;
    display: none;
  }


  /* container */
  .container{
  width: 100%;
  height: 80%;

  background-color: rgb(226, 227, 229);
  /* background-color: #FFFFFF; */
  display: inline-block;
  position: absolute;
  right: 0;
  overflow: scroll;
  }
  .work-menu:hover{
  /* background-color: #117ee4; */
  /* color: #FFFFFF; */
  }
  .user-profile:hover{
  }
}
</style>
