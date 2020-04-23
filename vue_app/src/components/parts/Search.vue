<template>
  <div class="serach-box">
    <form id="seach-form" action="URL" method="get">
      <input v-model="form.WorkType" id="search-type" name="" type="text" placeholder=" 職種"/><input v-model="form.Location" id="search-location" name="" type="text" placeholder=" 地域"/><input v-model="form.Freeword" id="search-free" name="" type="text" placeholder=" フリーワード"/>
      <input id="search-btn" type="submit" value="検索" />
    </form>
  </div>
</template>

<script>
export default {
  data(){
    return {
      form: {
        WorkType: '',
        Location: '',
        Freeword: '',
      },
    }
  },
  computed: {
    // JSON型のデータの中から出力する値を算出する
  }

}
</script>

<style scoped>
.serach-box{
  width: 70%;
  height: 48px;
  float: right;
  padding: 15px;
}
#seach-form{
  width: 90%;
  height: 100%;
}
#search-type{
  width: 20%;
  height: 70%;
  /* border-radius: 4%; */
  border: 1px solid #FFFFFF;
}
#search-location{
  width: 20%;
  height: 70%;
  /* border-radius: 4%; */
  border: 1px solid #FFFFFF;
}
#search-free{
  width: 40%;
  height: 70%;
  /* border-radius: 4%; */
  border: 1px solid #FFFFFF;
}
#search-btn{
  width: 58px;
  height: 39px;
  border-radius: 3%;
  background-color: rgb(255, 255, 255);
  border: 1px solid #117ee4;
  border-radius: 3px;
  color: #117ee4;
  font-weight: 600; 
}

/* レスポンシブ */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/
  .serach-box{
    width: 60%;
    height: 30px;
    padding: 15px 0 0 50px;
    /* background-color: aqua; */
  }
  .seach-form{
    width: 90%;
    height: 100%;
    background-color: yellow;
  }
  #search-type{
    display: none;
  }
  #search-location{
    display: none;
  }
  #search-free{
    width: 150px;
    height: 95%;
    border-radius: 4%;
    border: 1px solid grey;
    /* margin-left: 30px; */
    font-size: 11px;
  }
  #search-btn{
    width: 42px;
    height: 33px;
    border-radius: 3%;
    background-color: rgb(255, 255, 255);
    border: 1px solid #117ee4;
    border-radius: 3px;
    color: #117ee4;
    font-size: 12px;
  }
}
</style>