<template>
  <div class="detail-wrapper">
    <div class="top-recruit-detail">
      <div class="time-zone">2020年4月22日</div>
      <div class="recruit-title">19万人が利用するWebサイトの最適化で使い心地の良さを追求するフロントエンジニアを募集！</div>
      <div class="main-recruit-box">
      </div>
    </div>
    <div class="center-recruit-detail"></div>
    <div class="bottom-recruit-detail"></div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.detail-wrapper{
  width: calc(92% - 80px);
  height: 120%;
  margin: 22px auto;
  background-color: rgb(255, 255, 255);
  box-shadow: 10px 5px 5px grey;
  padding: 40px;
}
.top-recruit-detail{
  width: 100%;
  height: 7%;
  /* background-color: rgba(0, 128, 0, 0.459); */
  position: relative;
}
.time-zone{
  color: #818181;
  font-size: 14px;
}
.recruit-title{
  margin: 25px 0 0 35px ;
  width: 90%;
  height: 65%;
  font-size: 20px;
  color: #506690;
  /* background-color: rgba(255, 0, 0, 0.438); */
}
.main-recruit-box{
  width: 95%;
  height: 500px;
  margin: 0 auto;
  background-color: #085bf556;
}


</style>