<template>
  <div>
  <div class="detail-wrapper" v-if="post" key="product">
    <div class="top-recruit-detail">
      <span class="ribbon15"></span>
      <div class="time-zone">{{ post.created_at }}</div>
      <!-- IDの確認 -->
      <!-- <p>このページは ID: {{ $route.params.id }} の詳細を表示する</p> -->
      <div class="company-logo"></div>
      <div class="company-name">{{ post.company }}</div>
      <div class="recruit-title">{{ post.title }}</div>
    </div>
    <div class="top-main-recruit-box">
      <div class="recruit-list-box">
        <div class="top-list">
          <div class="salary-menu">月額単価</div>
          <div class="salary-area">{{ post.monthly_income_min }} ~ {{ post.monthly_income_max }}</div>
        </div>
        <div class="middle-list">
          <div class="left-box-first">
            <div class="recruit-type-menu">雇用携帯</div>
            <div class="recruit-type-area">{{ post.working_type }}</div>
          </div>
          <div class="rigth-box-second">
            <div class="recruit-days-menu">稼働日数</div>
            <div class="recruit-days-area">{{ post.working_days }} ~</div>
          </div>
        </div>
        <div class="bottom-list">
          <div class="left-box-secound">
            <div class="recruit-times-menu">契約期間</div>
            <div class="recruit-times-area">{{ post.time }}</div>
          </div>
          <div class="right-box-secound">
            <div class="recruit-worktype-menu">募集職種</div>
            <div class="recruit-worktype-area">{{ post.position }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="center-recruit-detail">
      <div class="label-tag">
        <p class="title-label">必須スキル</p>
        <p class="content-label">{{ post.must_skill }}</p>
      </div>
      <div class="label-tag">
        <p class="title-label">歓迎スキル</p>
        <p class="content-label">{{ post.want_skill }}</p>
      </div>
      <div class="label-tag">
        <p class="title-label">案件内容</p>
        <p class="content-label">{{ post.project_detail }}</p>
      </div>
      <div class="recruit-detail-box">
        <div class="label-tag">
          <p class="detail-title-label">面談回数</p>
          <p class="content-label">{{ post.mendann }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">待遇 / 福利厚生</p>
          <p class="content-label">{{ post.welfare }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">休日 / 休暇</p>
          <p class="content-label">{{ post.vacation }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">求める人材</p>
          <p class="content-label">{{ post.want_person }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">勤務地</p>
          <p class="content-label">{{ post.prefecture }} {{ post.city }}</p>
        </div>
      </div>
    </div>
    <div class="bottom-recruit-detail">
      <!-- エージェント コメント欄 -->
      <!-- <div class="sales-comment-box">
        <div class="sales-logo"></div>
        <div class="sales-comment">{{ item.agent_comment }}</div>
      </div> -->
      <div class="send-area">
        <div class="btn-are">
          <div class="send-box">
            <router-link to="/" class="link-spa">
              <form id="seach-form" action="apply" method="get">
                <button class="apply-btn">応募する</button>
              </form>
            </router-link>
          </div>
          <div class="send-box">
            <form id="seach-form" action="like" method="get">
              <button class="save-btn">保存する</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="load-box">
    <div class="loader">Loading...</div>
  </div>
  </div>
  <!-- <div v-else class="loader">Now loading...</div> -->
  <!-- <div class="load-box" v-else key="loading">
    <div class="loader">Loading...</div>
  </div> -->
</template>

<script>
import Loading from '@/components/parts/Loading'
import axios from 'axios'
import products from '@/api/products.js'
export default {
  // * Project_id を継承する
  props: {
    id: Number,
    id: {type: Number},
  },
  data() {
    return {
      // item: null,
      post: null,
      loading: true
    }
  },
  // ! 使用しない
  watch: {
    id: {
      handler() {
        products
          .asyncFind(this.id)
          .then(it => this.item = it);
      },
      immediate: true
    }
  },
  // ! ここまで -------------
  // * id 取得し, 詳細表示
  created() {
    // this.$http(`${this.$httpPosts}/${this.id}/`)
    axios.get(`${this.$httpPosts}/${this.id}/`)
        .then(response => {
          setTimeout(() => {
            this.loading = false;
            this.post = response.data
          }, 1000);
        })
        .then(data => {
          this.post = data
        })
  },
  components: {
    Loading
  },
}
</script>

<style scoped>
/* リボン */
.ribbon15-wrapper {  
  display: block;
  position: relative;
  margin: 15px auto;
  padding: 30px 0;
  width: 300px;
  background: #f1f1f1;
  box-sizing: border-box;
}

.ribbon15 {  
  display: inline-block;
  position: absolute;
  top: -6px;
  right: 10px;
  margin: 0;
  padding: 3% 0;
  z-index: 2;
  width: 40px;
  height: 20px;
  text-align: center;
  color: white;
  font-size: 22px;
  background: linear-gradient(#f09819 0%, #e95738 100%);
  border-radius: 2px 0 0 0;
}

.ribbon15:before {
  position: absolute;
  content: '';
  top: 0;
  right: -6px;
  border: none;
  border-bottom: solid 6px #cf4a2d;
  border-right: solid 6px transparent;
}
.ribbon15:after {
  content: '';
  position: absolute;
  left: 0;
  top: 100%;
  height: 0;
  width: 0;
  border-left: 20px solid #e95738;
  border-right: 20px solid #e95738;
  border-bottom: 10px solid transparent;
}
/* ここまで */

.detail-wrapper{
  width: calc(84%);
  /* height: 140%; */
  margin: 22px auto;
  background-color: rgb(255, 255, 255);
  box-shadow: 4px 2px 2px grey;
  padding: 0 0 20px 35px; 
}
/* トップ 日付、会社名、タイトル */
.top-recruit-detail{
  width: 100%;
  height: 15%;
  position: relative;
  padding-top: 40px;
}
.time-zone{
  color: #818181;
  font-size: 14px;
}
.company-logo{
  width: 40px;
  height: 40px;
  background-color: grey;
  display: inline-block;
  margin-top: 20px;
}
.company-name{
  width: 250px;
  padding: 10px;
  display: inline-block;
  color: #818181;
}
.recruit-title{
  margin: 15px 0 35px 35px ;
  width: 90%;
  height: 65%;
  font-size: 20px;
  color: #506690;
  font-weight: bold;
}

/* 中間 */
.top-main-recruit-box{
  width: 95%;
  height: 210px;
  margin: 0 auto;
}
/* top */
.recruit-list-box{
  width: 95%;
  height: 180px;
  box-shadow: 10px 5px 5px grey;
}
.top-list{
  width: 100%;
  height: 33%;
  position: relative;
  border: solid 1px rgb(199, 199, 199);
}
.salary-menu{
  width: 20%;
  /* height: 100%; */
  height: calc(100% - 30px);
  background-color: #0052C0;
  display: inline-block;
  color: #FFFFFF;
  padding: 20px 10px 10px 10px;
  font-weight: bold;
}
.salary-area{
  width: calc(100% - 30%);
  height: calc(100% - 30px);
  display: inline-block;
  top: 0;
  font-size: 22px;
  position: absolute;
  padding: 20px 10px 10px 10px;
  color: #F09819;
  font-weight: bold;
  /* box-shadow: 10px 10px 10px rgba(0,0,0,0.4);  */
}

/* middle */
.middle-list{
  width: 100%;
  height: 33%;
  position: relative;
  border: solid 1px rgb(199, 199, 199);
}
.left-box-first{
  width: 49%;
  height: 100%;
  display: inline-block;
  position: absolute;
  top: 0;
}
.recruit-type-menu{
  width: 40.8%;
  /* height: 100%; */
  height: calc(100% - 30px);
  background-color: #0052C0;
  display: inline-block;
  color: #FFFFFF;
  padding: 20px 10px 10px 10px;
  font-weight: bold;
}
.recruit-type-area{
  height: calc(100% - 30px);
  display: inline-block;
  top: 0;
  position: absolute;
  padding: 20px 10px 10px 10px;
  color: #818181;
}
.rigth-box-second{
  width: 49%;
  height: 100%;
  float: right;
}
.recruit-days-menu{
  width: 40.8%;
  height: calc(100% - 30px);
  background-color: #0052C0;
  display: inline-block;
  color: #FFFFFF;
  padding: 20px 10px 10px 10px;
  font-weight: bold;
}
.recruit-days-area{
  height: calc(100% - 30px);
  display: inline-block;
  top: 0;
  position: absolute;
  padding: 20px 10px 10px 10px;
  color: #818181;
}
.bottom-list{
  width: 100%;
  height: 33%;
  position: relative;
  border: solid 1px rgb(199, 199, 199);
}
.left-box-secound{
  width: 49%;
  height: 100%;
  display: inline-block;
  position: absolute;
  top: 0;
}
.right-box-secound{
  width: 49%;
  height: 100%;
  float: right;
}
.recruit-times-menu{
  width: 40.8%;
  /* height: 100%; */
  height: calc(100% - 30px);
  background-color: #0052C0;
  display: inline-block;
  color: #FFFFFF;
  padding: 20px 10px 10px 10px;
  font-weight: bold;
}
.recruit-times-area{
  height: calc(100% - 30px);
  display: inline-block;
  top: 0;
  position: absolute;
  padding: 20px 10px 10px 10px;
  color: #818181;
}
.recruit-worktype-menu{
  width: 40.8%;
  height: calc(100% - 30px);
  background-color: #0052C0;
  display: inline-block;
  color: #FFFFFF;
  padding: 20px 10px 10px 10px;
  font-weight: bold;
}
.recruit-worktype-area{
  height: calc(100% - 30px);
  display: inline-block;
  top: 0;
  position: absolute;
  padding: 20px 10px 10px 10px;
  color: #818181;
}
.center-recruit-detail{
  width: 90%;
  margin: 0 auto;
}
.label-tag{
  width:100%;
}
.title-label {
  margin-top: 20px;
  position: relative;
  padding: 5px 5px 5px 42px;
  background: #77c3df;
  font-size: 20px;
  color: white;
  margin-left: -33px;
  line-height: 1.3;
  /* z-index:-1; */
  z-index: 2;
  width: 10%;
  font-size: 14px;
  font-weight: bold;
}
.title-label:before {
  position: absolute;
  content: '';
  left: -2px;
  top: -2px;
  border: none;
  border-left: solid 40px white;
  border-bottom: solid 79px transparent;
  z-index: 1;
}
.content-label{
  font-size: 14px;
  color: #636363;
}

/* 詳細 */
.recruit-detail-box{
  width: 95%;
  /* height: 100px; */
  /* background-color: rgba(0, 83, 192, 0.438); */
  margin: 0 auto;
}
.detail-title-label{
  margin-top: 20px;
  font-size: 14px;
  font-weight: bold;
  color: #77c3df;
}

/* bottom */
.bottom-recruit-detail{
  width: 100%;
  height: 20%;
}
.sales-comment-box{
  width: calc(100% - 80px);
  height: 100px;
  padding: 40px;
  position: relative;
}
.balloon1-left:before {
  content: "";
  position: absolute;
  top: 50%;
  left: -30px;
  margin-top: -15px;
  border: 15px solid transparent;
  border-right: 15px solid #e0edff;
}

.balloon1-left p {
  margin: 0;
  padding: 0;
}
/* エージェント表示 */
/* .sales-logo{
  width: 100px;
  height: 100px;
  background-color: grey;
  display: inline-block;
  position: absolute;
  bottom: 0;
  border-radius: 20%;
}
.sales-comment{
  width: calc(100% - 190px);
  height: calc(100px - 40px);
  padding: 30px;
  font-size: 14px;
  background-color: #D8D8D8;
  float: right;
} */

.send-area{
  width: calc(100% - 40px);
  height: 60px;
  margin-top: 45px;
  padding: 20px 0;
}
.btn-are{
  width: 85%;
  height: 100%;
  margin: 0 auto;
}

/* 保存 応募ボタン */
#seach-form{
  display:inline-block;
}
.send-box{
  display: inline-block;
  width: 20%;
  height: 50%;
  padding: 0 13%;
}
.apply-btn{
  width: 220px;
  height: 54px;
  background: linear-gradient(#ef6443, #f09819);
  color: #FFFFFF;
  text-align: center;
  border-radius: 12px;
  font-size: 18px;
  padding: 2px 0 0 0 ;
  display: inline-block;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0px 4px 0 rgba(138, 138, 138, 0.7);
  padding : 8px;
  transition: 0.2s all ease 0s;
  border-radius: 50rem;
}
.apply-btn:hover{
  background-color: #f09819;
  box-shadow: none;
  transform: translate3d(0, 3px, 0);
}
.save-btn{
  width: 220px;
  height: 54px;
  color: #FFFFFF;
  text-align: center;
  border-radius: 12px;
  font-size: 18px;
  font-weight: bold;
  padding: 2px 0 0 0 ;
  display: inline-block;
  cursor: pointer;
  background: linear-gradient(#2AC1DF, rgb(42, 105, 223));
  box-shadow: 0px 4px 0 rgba(138, 138, 138, 0.7);
  padding : 8px;
  transition: 0.2s all ease 0s;
  border-radius: 50rem;
}
.save-btn:hover{
  box-shadow: none;
  transform: translate3d(0, 3px, 0);
}
/* ローディング CSS */
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





/* レスポンシブデザイン */
@media screen and (max-width: 767px) {
  .detail-wrapper{
    padding: 20px;
    width: 82%;
    /* margin: 0; */
  }
  .top-recruit-detail{
    padding: 0;
  }
  .company-logo{
    width: 40px;
    height: 40px;
    display: inline-block;
  }
  .company-name{
    display: inline-block;
    width: 70%;
    height: 20px;
    font-size: 14px;
  }
  .recruit-title{
    font-size: 14px;
    width: 100%;
    margin: 0;
    /* margin-bottom: 10px; */
  }
  .top-list{
    /* border: solid 1px rgb(199, 199, 199); */
    border: none;
    width: 100%;
    height: 50px;
  }
  .top-main-recruit-box{
    width: 100%;
    height: 70%;
    /* background-color: rgba(0, 83, 192, 0.445); */
  }
  .recruit-list-box{
    width: 100%;
    height: 255px;
    margin: 30px 0;
  }
  .salary-menu{
    font-size: 12px;
    /* width: 20px; */
    height: 20px;
  }
  .salary-area{
    font-size: 18px;
    /* width: 20px; */
    height: 20px;
  }
  .middle-list{
    height: 82px;
    font-size: 12px;
    border: none;
  }
  .recruit-type-area{
    /* height: 20px; */
    /* width: 10px; */
    /* background-color: green; */
    /* padding: 0; */
    /* width: 100%; */
  }
  .recruit-type-menu{
    font-size: 12px;
    height: 20px;
    width: 20%;
    margin-top: 2px;
  }
  .left-box-first{
    width: 100%;
    height: 30px;
  }
  .right-box-secound{
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    height: 44px;
  }
  .rigth-box-second{
    width: 100%;
    height: 30px;
    position: absolute;
    bottom: 0;
    border: none;
    /* display: none; */
  }
  .recruit-days-menu{
    width: 20%;
    height: 20px;
    margin-top: 2px;
  }
  .recruit-type-area{
    width: 100%;
    height: 20px;
  }
  .recruit-times-area{
    /* background-color: green; */
  }
  .bottom-list{
    font-size: 12px;
    height: 95px;
    margin-top: 20px;
    position: relative;
    border: none;
  }
  .left-box-secound{
    width: 100%;
    height: 30px;
  }
  .recruit-times-menu{
    width: 20%;
    height: 20px;
    margin-top: 4px;

  }
  .recruit-times-area{
    width: 80%;
    height: 20px;
  }
  .recruit-worktype-menu{
    width: 100%;
    /* position: absolute;
    bottom: 0;
    left: 0; */
    margin-top: 2px;
  }
  .recruit-worktype-menu{
    width: 20%;
    height: 20px;
    margin-top: 4px;
  }
  .recruit-worktype-area{
    width: 80%;
    height: 22px;
  }

  .title-label{
  margin-top: 20px;
  position: relative;
  padding: 5px 5px 5px 42px;
  background: #77c3df;
  font-size: 20px;
  color: white;
  margin-left: -33px;
  line-height: 1.3;
  z-index: 2;
  width: 30%;
  font-size: 14px;
  font-weight: bold;
  }

  .bottom-recruit-detail{
    width: 100%;
    /* height: 230px; */
  }
  .sales-comment-box{
    padding: 15px 15px 15px 0;
    width: 100%;
    height: 120px;
  }
  .sales-logo{
    width: 40px;
    height: 40px;
    position: absolute;
    top: 0;
  }
  .sales-comment{
    width:calc(90% - 30px);
    float: none;
    /* height: ; */
  }
  /* 応募ボタン 保存ボタン */
  .send-area{
    padding: 0;
    margin: 0;
    width: 100%;
    margin-top: 20px;
  }
  .send-box{
    width: 22%;
    height: 80%;
    position: relative;
  }
  .btn-are{
    width: 70%;
    margin:0 auto
  }
  #seach-form{
    width: 100px;
    display:inline-block;
  }
  .apply-btn{
    /* width: 100px; */
    width: 100%;
    display: inline-block;
    position: absolute;
    left: 0;
    height: 90%;
    font-size: 14px;
  }
  .save-btn{
    /* width: 100px; */
    width: 100%;
    display: inline-block;
    position: absolute;
    right: 0;
        height: 90%;
    font-size: 14px;
  }

  .ribbon15 {  
    display: inline-block;
    position: absolute;
    top: -6px;
    right: 10px;
    margin: 0;
    padding: 3% 0;
    z-index: 2;
    width: 40px;
    height: 20px;
    text-align: center;
    color: white;
    font-size: 22px;
    background: linear-gradient(#f09819 0%, #e95738 100%);
    border-radius: 2px 0 0 0;
  }
}
</style>