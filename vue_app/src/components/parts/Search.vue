<template>
  <div class="serach-box">
    <form id="seach-form" action="search" method="get">
      <!-- {{ workerType.selected }} -->
      <v-select id="search-type" name="hoge" :options="workerType.options" v-model="workerType.selected"></v-select><v-select id="search-type" name="hoge" :options="location.options" v-model="location.selected"></v-select><input v-model="form.freeword" id="search-free" name="" type="text" placeholder=" フリーワード"/>
      <input id="search-btn" type="submit" value="検索" />
    </form>
  </div>
</template>

<script>
import vSelect from 'vue-select'
export default {
  data(){
    return {
      form: {
        freeword: ''
      },
      workerType: {
        selected: '職種',
        options: [
          'ゲームエンジンプログラマー',
          'ネットワークエンジニア',
          'インフラエンジニア',
          'フロントエンドエンジニア',
          'サーバーエンジニア',
          'セキュリティエンジニア',
          'データベースエンジニア',
          'テストエンジニア',
          '組み込み・制御エンジニア',
          'プロジェクトマネージャー(PM)',
          'CTO候補',

        ]
      },
      location: {
        selected: '都道府県',
        options: [
          '千葉',
          '東京',
          '埼玉',
          '沖縄',
          '北海道'
        ]
      },
    }
  },
  methods: {
    updateSelected (newSelected) {
      this.selected = newSelected
    }
  },
  computed: {
    // JSON型のデータの中から出力する値を算出する
  }

}
</script>

<style scoped>
.serach-box{
  width: 80%;
  height: 48px;
  float: right;
  padding: 15px;
}
#seach-form{
  width: 95%;
  height: 100%;
}
#search-type{
  width: 26%;
  height: 70%;
  color: #333;
  cursor: pointer;
  background-color: #117ee456;
  display: inline-block;
}
.vs__dropdown-toggle{
  background-color: green;
  width: 2000px;
}
.vs__selected-options{
  background-color: green;
  width: 2000px;
}
#search-location{
  width: 20%;
  height: 70%;
  /* border-radius: 4%; */
  border: 1px solid #FFFFFF;
}
#search-free{
  width: 40%;
  height: 62%;
  /* border-radius: 4%; */
  background-color: #117ee456;
  border: 1px solid rgba(60,60,60,.26);
  border-radius: 4px;
  color: #333333;
}
#search-free::placeholder {
	color: #333333;
}
#search-btn{
  width: 58px;
  height: 34px;
  border-radius: 3%;
  background: linear-gradient(#ef6443, #f09819);
  border: 1px solid #ef6443;
  border-radius: 3px;
  color: #FFFFFF;
  font-weight: 600; 
}

/* レスポンシブ */
@media screen and (max-width: 767px) { /*ウィンドウ幅が最大767pxまでの場合に適用*/
  .serach-box{
    width: 80%;
    height: 90%;
    padding: 15px 0 0 1px;
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
    width: 80%;
    height: 62%;
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
    color: #ffffff;
    font-size: 12px;
  }
}
</style>