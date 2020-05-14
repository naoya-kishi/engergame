<template>
  <div class="chat-container">
    <div v-show="loading"  class="load-box">
      <div class="loader">Loading...</div>
    </div>
    <div class="left-chatbox" v-show="!loading">
      <router-link to="/chat/1/">
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      </router-link>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
      <div class="user-chatbox">
        <div class="userimage">
        </div>
        <div class="user-detail">
          <div class="username">SAMPLE NAME</div>
          <div class="usercompany">株式会社SAMPLE</div>   
        </div>
      </div>
    </div>
    <div class="right-chatbox">
      <div class="main-box">
        <div class="chat-mainbox">
        </div>
      </div>
      <div class="bottom-box">
        <div id="bms_send">
          <textarea id="bms_send_message">
          </textarea>
          <div id="bms_send_btn">送信</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
    }
  },
  mounted() {
    setTimeout(() => {
      this.loading = false;
    }, 1000);
  },
}
</script>

<style scoped>
a{
  text-decoration: none;
}

.chat-container{
  width: 100%;
  height: 100%;
  /* background-color: rgb(115, 255, 0); */
}

/* 左 チャットボックス */
.left-chatbox{
  position: relative;
  width: 280px;
  height: 100%;
  overflow: scroll;
  background-color: #FFFFFF;
  box-shadow: 2px 4px 8px rgba(128, 128, 128, 0.39);
  display: inline-block;
}
.user-chatbox{
  width: 85%;
  height: 50px;
  padding: 10px;
  margin: 0 auto;
  cursor: pointer;
}
.userimage{
  width: 50px;
  height: 50px;
  background-color: grey;
  border-radius: 20%;
  display: inline-block;
}
.user-detail{
  float: right;
  font-size: 14px;
  width: 180px;
  height: 50px;
  padding: 20px 0 0 0;
  margin-right: 0px;
}
.usercompany{
  font-size: 9px;
  color: #506690;
}
.username{
  text-decoration: none;
  color: #252525;
}

/* 右側 チャットボックス */
.right-chatbox{
  position: absolute;
  right: 0;
  width: calc(100% - 284px);
  height: 100%;
  display: inline-block;
}
/* チャット 送受信 */
.main-box{
  width: calc(100% - 40px );
  height: calc(88% - 40px);
  padding: 20px;
}
.chat-mainbox{
  width: 100%;
  height: 100%;
  /* background-color: green; */
  overflow: scroll;
}
.chat-message-box{
  width: 100%;
  height: 120px;
  /* background-color: #FFFFFF; */
}
.chat-message-profile-box{
  width: 100%;
  /* height: 45%; */
  /* background-color: red; */
}
.chat-profile-image{
  width: 40px;
  height: 40px;
  border-radius: 20%;
  background-color: grey;
  display: inline-block;
}
.chat-profile-name{
  display: inline-block;
  font-size: 14px;
  color: #506690;
}
.message-content{
  padding: 5px;
  font-size: 14px;
}


/* 送信ボックス */
.bottom-box{
  width: calc(100% - 30px);
  height: calc(100% - 88% - 30px);
  padding: 15px;
  /* border-top: 1px solid red; */
  filter: drop-shadow(0 0 3px black);
  z-index: 100;
}
#bms_send_message{
  width: calc(100% - 75px);
  height: 100%;
  border: 1px solid rgb(226, 227, 229);
  line-height: 30px;
  display: inline-block;
  border-radius: 12px;
}
#bms_send_btn{
  width: 62px;
  height: 48px;
  font-size: 16px;
  line-height: 3em;
  float: right;/*bms_sendに対して右寄せ*/
  color: #fff;
  font-weight: bold;
  /* background: #ef6443; */
  background: linear-gradient(#ef6443, #f09819);
  text-align: center;/*文字をボタン中央に表示*/
  border: 1px solid #ef6443;
  border-radius: 4px;/*角丸*/
  box-sizing: border-box;
  margin-top: 15px;
}

/* Action アクション */
.user-chatbox:hover{
  opacity: 0.7;
}

.load-box{
  width: 100px;
  height: 100px;
  /* background-color: #0052C0; */
  margin: 200px auto 0 auto;
}

.loader {
  margin: 100px auto;
  font-size: 25px;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  position: relative;
  text-indent: -9999em;
  -webkit-animation: load5 1.1s infinite ease;
  animation: load5 1.1s infinite ease;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
}
@-webkit-keyframes load5 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #2AC1DF, 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.5), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.7), 1.8em -1.8em 0 0em #2AC1DF, 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.5), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7), 2.5em 0em 0 0em #2AC1DF, 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5), 2.5em 0em 0 0em rgba(255, 255, 255, 0.7), 1.75em 1.75em 0 0em #2AC1DF, 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.5), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.7), 0em 2.5em 0 0em #2AC1DF, -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.5), 0em 2.5em 0 0em rgba(255, 255, 255, 0.7), -1.8em 1.8em 0 0em #2AC1DF, -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.5), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.7), -2.6em 0em 0 0em #2AC1DF, -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.5), -2.6em 0em 0 0em rgba(255, 255, 255, 0.7), -1.8em -1.8em 0 0em #2AC1DF;
  }
}
@keyframes load5 {
  0%,
  100% {
    box-shadow: 0em -2.6em 0em 0em #2AC1DF, 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.5), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7);
  }
  12.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.7), 1.8em -1.8em 0 0em #2AC1DF, 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5);
  }
  25% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.5), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.7), 2.5em 0em 0 0em #2AC1DF, 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  37.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.5), 2.5em 0em 0 0em rgba(255, 255, 255, 0.7), 1.75em 1.75em 0 0em #2AC1DF, 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  50% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.5), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.7), 0em 2.5em 0 0em #2AC1DF, -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.2), -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  62.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.5), 0em 2.5em 0 0em rgba(255, 255, 255, 0.7), -1.8em 1.8em 0 0em #2AC1DF, -2.6em 0em 0 0em rgba(255, 255, 255, 0.2), -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  75% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.5), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.7), -2.6em 0em 0 0em #2AC1DF, -1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2);
  }
  87.5% {
    box-shadow: 0em -2.6em 0em 0em rgba(255, 255, 255, 0.2), 1.8em -1.8em 0 0em rgba(255, 255, 255, 0.2), 2.5em 0em 0 0em rgba(255, 255, 255, 0.2), 1.75em 1.75em 0 0em rgba(255, 255, 255, 0.2), 0em 2.5em 0 0em rgba(255, 255, 255, 0.2), -1.8em 1.8em 0 0em rgba(255, 255, 255, 0.5), -2.6em 0em 0 0em rgba(255, 255, 255, 0.7), -1.8em -1.8em 0 0em #2AC1DF;
  }
}

/* レスポンシブ */
@media screen and (max-width: 767px) {
  .right-chatbox{
    display: none;
  }
}

</style>