<template>
  <div class="chat-container">
    <div class="left-chatbox">
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
  background-color: #FFFFFF;
  /* background-color: rgb(226, 227, 229); */
}
#bms_send_message{
  width: calc(100% - 75px);
  height: 100%;
  border: 1px solid rgb(226, 227, 229);
  line-height: 30px;
  display: inline-block;

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

/* レスポンシブ */
@media screen and (max-width: 767px) {
  .right-chatbox{
    display: none;
  }
}

</style>