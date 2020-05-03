<template>
  <div class="detail-wrapper" v-if="item" key="product">
    <div class="top-recruit-detail">
      <div class="time-zone">2020年4月22日</div>
      <!-- IDの確認 -->
      <!-- <p>このページは ID: {{ $route.params.id }} の詳細を表示する</p> -->
      <div class="company-logo"></div>
      <div class="company-name">{{ item.company }}</div>
      <div class="recruit-title">{{ item.title }}</div>
    </div>
    <div class="top-main-recruit-box">
      <div class="recruit-list-box">
        <div class="top-list">
          <div class="salary-menu">月額単価</div>
          <div class="salary-area">{{ item.monthly_income_min }} ~ {{ item.monthly_income_max }}</div>
        </div>
        <div class="middle-list">
          <div class="left-box-first">
            <div class="recruit-type-menu">雇用携帯</div>
            <div class="recruit-type-area">{{ item.working_type }}</div>
          </div>
          <div class="rigth-box-second">
            <div class="recruit-days-menu">稼働日数</div>
            <div class="recruit-days-area">{{ item.working_days }} ~</div>
          </div>
        </div>
        <div class="bottom-list">
          <div class="left-box-secound">
            <div class="recruit-times-menu">契約期間</div>
            <div class="recruit-times-area">{{ item.time }}</div>
          </div>
          <div class="right-box-secound">
            <div class="recruit-worktype-menu">募集職種</div>
            <div class="recruit-worktype-area">{{ item.position }}</div>
          </div>
        </div>
      </div>
    </div>
    <div class="center-recruit-detail">
      <div class="label-tag">
        <p class="title-label">必須スキル</p>
        <p class="content-label">{{ item.must_skill }}</p>
      </div>
      <div class="label-tag">
        <p class="title-label">歓迎スキル</p>
        <p class="content-label">{{ item.want_skill }}</p>
      </div>
      <div class="label-tag">
        <p class="title-label">案件内容</p>
        <p class="content-label">電子決済サービス向けプロダクトの機能追加がメインの作業となりますが、サービス全体を俯瞰してシステム構築作業にも携わっていただきます。</p>
      </div>
      <div class="recruit-detail-box">
        <div class="label-tag">
          <p class="detail-title-label">面談回数</p>
          <p class="content-label">{{ item.mendann }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">待遇 / 福利厚生</p>
          <p class="content-label">{{ item.welfare }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">休日 / 休暇</p>
          <p class="content-label">{{ item.vacation }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">求める人材</p>
          <p class="content-label">{{ item.want_person }}</p>
        </div>
        <div class="label-tag">
          <p class="detail-title-label">勤務地</p>
          <p class="content-label">{{ item.prefecture }} {{ item.city }}</p>
        </div>
      </div>
    </div>
    <div class="bottom-recruit-detail">
      <div class="sales-comment-box">
        <div class="sales-logo"></div>
        <div class="sales-comment">{{ item.agent_comment }}</div>
      </div>
      <div class="send-area">
        <div class="btn-are">
          <router-link to="/" class="link-spa">
            <form id="seach-form" action="apply" method="get">
              <button class="apply-btn">応募する</button>
            </form>
          </router-link>
          <form id="seach-form" action="like" method="get">
            <button class="save-btn">保存する</button>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div class="load-box" v-else key="loading">
    <div class="loader">Loading...</div>
  </div>
</template>

<script>
import products from '@/api/products.js'
export default {
  props: {
    id: Number
  },
  data() {
    return {
      item: null
    }
  },
  watch: {
    id: {
      handler() {
        products
          .asyncFind(this.id)
          .then(it => this.item = it);
      },
      immediate: true
    }
  }
}
</script>

<style scoped>
.detail-wrapper{
  width: calc(92% - 80px);
  /* height: 140%; */
  margin: 22px auto;
  background-color: rgb(255, 255, 255);
  box-shadow: 10px 5px 5px grey;
  padding: 40px;
}
/* トップ 日付、会社名、タイトル */
.top-recruit-detail{
  width: 100%;
  height: 15%;
  position: relative;
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
  font-size: 18px;
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
  /* width: calc(90% - 30%); */
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
.sales-logo{
  width: 100px;
  height: 100px;
  background-color: grey;
  display: inline-block;
  position: absolute;
  bottom: 0;
}
.sales-comment{
  width: calc(100% - 190px);
  height: calc(100px - 40px);
  padding: 30px;
  font-size: 14px;
  background-color: #D8D8D8;
  border-radius: 2%;
  /* display: inline-block; */
  float: right;
}
.send-area{
  width: calc(100% - 40px);
  /* height: 25%; */
  margin-top: 20px;
  padding: 20px 0;
}
.btn-are{
  width: 35%;
  height: 100%;
  margin: 0 auto;
}

/* 保存 応募ボタン */
#seach-form{
  width: 160px;
  display:inline-block;
}
.apply-btn{
  width: 160px;
  height: 40px;
  background-color: #f09819;
  color: #FFFFFF;
  text-align: center;
  border-radius: 12px;
  font-size: 14px;
  padding: 2px 0 0 0 ;
  display: inline-block;
}
.save-btn{
  width: 160px;
  height: 40px;
  background-color: #2AC1DF;
  color: #FFFFFF;
  text-align: center;
  border-radius: 12px;
  font-size: 14px;
  padding: 2px 0 0 0 ;
  display: inline-block;
}
/* ローディング CSS */
.load-box{
  width: 100px;
  height: 100px;
  /* background-color: #0052C0; */
  margin: 200px auto 0 auto;
}

.loader {
  color: #2AC1DF;
  font-size: 121px;
  text-indent: -9999em;
  overflow: hidden;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  margin: 72px auto;
  position: relative;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation: load6 1.7s infinite ease, round 1.7s infinite ease;
  animation: load6 1.7s infinite ease, round 1.7s infinite ease;
}
@-webkit-keyframes load6 {
  0% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
  5%,
  95% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
  10%,
  59% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.087em -0.825em 0 -0.42em, -0.173em -0.812em 0 -0.44em, -0.256em -0.789em 0 -0.46em, -0.297em -0.775em 0 -0.477em;
  }
  20% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.338em -0.758em 0 -0.42em, -0.555em -0.617em 0 -0.44em, -0.671em -0.488em 0 -0.46em, -0.749em -0.34em 0 -0.477em;
  }
  38% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.377em -0.74em 0 -0.42em, -0.645em -0.522em 0 -0.44em, -0.775em -0.297em 0 -0.46em, -0.82em -0.09em 0 -0.477em;
  }
  100% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
}
@keyframes load6 {
  0% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
  5%,
  95% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
  10%,
  59% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.087em -0.825em 0 -0.42em, -0.173em -0.812em 0 -0.44em, -0.256em -0.789em 0 -0.46em, -0.297em -0.775em 0 -0.477em;
  }
  20% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.338em -0.758em 0 -0.42em, -0.555em -0.617em 0 -0.44em, -0.671em -0.488em 0 -0.46em, -0.749em -0.34em 0 -0.477em;
  }
  38% {
    box-shadow: 0 -0.83em 0 -0.4em, -0.377em -0.74em 0 -0.42em, -0.645em -0.522em 0 -0.44em, -0.775em -0.297em 0 -0.46em, -0.82em -0.09em 0 -0.477em;
  }
  100% {
    box-shadow: 0 -0.83em 0 -0.4em, 0 -0.83em 0 -0.42em, 0 -0.83em 0 -0.44em, 0 -0.83em 0 -0.46em, 0 -0.83em 0 -0.477em;
  }
}
@-webkit-keyframes round {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes round {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}





/* レスポンシブデザイン */
@media screen and (max-width: 767px) {
  .detail-wrapper{
    padding: 20px;
    width: 82%;
    /* margin: 0; */
  }
  .company-logo{
    width: 30px;
    height: 30px;
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
    font-size: 12px;
    /* width: 20px; */
    height: 20px;
  }
  .middle-list{
    height: 82px;
    font-size: 12px;
    border: none;
  }
  .recruit-type-area{
    height: 20px;
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
    width: 100%;
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
  /* z-index:-1; */
  z-index: 2;
  width: 30%;
  font-size: 14px;
  font-weight: bold;
  }

  .bottom-recruit-detail{
    width: 100%;
    height: 230px;
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
  .btn-are{
    width: 70%;
    margin:0 auto
  }
  #seach-form{
    width: 100px;
    display:inline-block;
  }
  .apply-btn{
    width: 100px;
    display: inline-block;
  }
  .save-btn{
    width: 100px;
    display: inline-block;
  }
}
</style>