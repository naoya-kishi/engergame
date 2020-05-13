<template>
  <div class="recruit-wrapper">
    <paginate name="paginate-log" :list="postList" :per="10" class="paginate">
      <router-link :to="`/recruit/${ post.project_id }`" v-for="post in paginated('paginate-log')" :key="post.id" class="post">
      <div class="recruit-content">
        <div class="recruit-topbox">
          <div class="create-time">{{ post.created_at }}</div>
          <div class="create-work">{{ post.position }}</div>
          <div class="matching-status">マッチング率 {{ post.matching }}%</div>
        </div>
        <div class="recruit-centerbox">
          <div class="recruit-title-box">
            {{ post.title }}
          </div>
          <div class="recruit-company-box">
            {{ post.company }}
          </div>
        </div>
        <div class="recruit-btmbox">
          <div class="recruit-detail-box">
            <div class="money-area">
              <div class="money-logo"><font-awesome-icon icon="yen-sign" class="awesome-icon"/></div>
              <div class="money-content">
                {{ post.monthly_income_min }} ~ {{ post.monthly_income_max }}
              </div>
            </div>
            <div class="location-area">
              <div class="location-logo"><font-awesome-icon icon="map-marker-alt" class="awesome-icon"/></div>
              <div class="location-content">
                {{ post.prefecture }} {{ post.city }}
              </div>
            </div>
          </div>
          <div class="recruit-skill-box">
            <div class="skill-logo">スキル</div>
            <div class="skill-content">{{ post.must_skill }}</div>
          </div>
          <!-- エージェント 表示 -->
          <!-- <div class="recruit-sales-box">
            <div class="sales-logo"></div>
            <div class="sales-name">{{ sales_name }}</div>
          </div> -->
        </div>
      </div>
      </router-link>
    </paginate>
    <paginate-links for="paginate-log" class="pagination" :show-step-links="true" ></paginate-links>
  </div>
</template>

<script>
import axios from 'axios'
import database from '@/api/products.js'
export default {
  data(){
    return{
      postList: [],
      paginate: ['paginate-log']
    }
  },
  //! 使用しない
  computed: {
    list: () => database.fetch()
  },
  // !------- ここまで -----
  // * 文字制限
  filters: {
    // 案件タイトル 文字制限
    truncateTitle: function(value) {
      var length = 133;
      var ommision = "...";
      if (value.length <= length) {
        return value;
      }
      return value.substring(0, length) + ommision;
    },
    // スキル 文字制限
    truncateSkill: function(value) {
      var length = 100;
      var ommision = "...";
      if (value.length <= length) {
        return value;
      }
      return value.substring(0, length) + ommision;
    },
  },
  // * axios setting
  mounted() {
    axios.get('http://localhost:3000/mock/users')
      .then(response => {
          return response.data
      })
      .then(data => {
          this.postList = data
      })
  }
}
</script>

<style scoped>
a{
  text-decoration: none;
}
li{
  width: 100px;
  height: 100px;
  background-color: green;
}

.recruit-wrapper{
  width: 92%;
  height: 120%;
  margin: 22px auto;
}
/* 求人content CSS */
.recruit-content{
  width: calc(100% - 20px);
  height: 200px;
  background-color: #FFFFFF;
  box-shadow: 10px 5px 5px grey;
  padding: 20px;
  margin: 15px 0;
  cursor: pointer;
  box-shadow: 0 0 3px 0 rgba(0,0,0,.12), 0 2px 3px 0 rgba(0,0,0,.22);
	transition: .3s;
}
/* Top BOX */
.recruit-topbox{
  width: 100%;
  height: 30px;
}
.create-time{
  color: #818181;
  font-size: 12px;
  display: inline-block;
}
.create-work{
  display: inline-block;
  background: linear-gradient(#ef6443, #f09819);
  color: #FFFFFF;
  border-radius: 12px;
  padding: 5px 12px;
  font-size: 12px;
  text-align: center;
  /* border: solid 1px #f09819; */
  font-weight: bold;
}
.matching-status{
  float: right;
  width: 12%;
  background-color: #ffffff;
  color: #1f5abc;
  border-radius: 12px;
  padding: 5px 12px;
  font-size: 12px;
  text-align: center;
  border: solid 1px #1f5abc;
  font-weight: bold;
}
.applied-tag-are{
  width: 100px;
  height: 40px;
  background-color: red;
  float: right;
  z-index: 100;
}

/* Center BOX */
.recruit-centerbox{
  width: 100%;
  height: 110px;
}
.recruit-title-box{
  width: calc(100% - 10px);
  height: 60px;
  padding: 15px 5px 0px 5px;
  color: #506690;
  font-size: 16px;
}
.recruit-company-box{
  font-size: 14px;
  color: #818181;
}


/* Bottom BOX */
.recruit-btmbox{
  width: 100%;
  height: 75px;
}
/* 単価 / 勤務地 CSS */
.recruit-detail-box{
  width: 80%;
  height: 40px;
}
.money-area{
  display: inline-block;
  position: relative;
  width: 50%;
}
.location-area{
  display: inline-block;
}
.money-logo{
  width: 25px;
  height: 25px;
  border-radius: 50%;
  display: inline-block;
}
.money-content{
  font-size: 14px;
  display: inline-block;
  position: absolute;
  top: 7px;
  color: #818181;
}

.location-area{
  display: inline-block;
  position: relative;
  width: 20%;
}
.location-logo{
  width: 25px;
  height: 25px;
  border-radius: 50%;
  display: inline-block;
}
.location-content{
  font-size: 14px;
  display: inline-block;
  position: absolute;
  top: 7px;
  color: #818181;
}

/* スキル CSS */
.recruit-skill-box{
  width: 95%;
  display: inline-block;
}
.skill-logo{
  width: 120px;
  height: 20px;
  background: linear-gradient(rgb(20, 148, 233), #2AC1DF);
  color: #FFFFFF;
  text-align: center;
  border-radius: 12px;
  font-size: 14px;
  padding: 2px 0 0 0 ;
  display: inline-block;
  font-weight: bold;
}
.skill-content{
  display: inline-block;
  color: #818181;
  font-size: 14px;
}

/* 営業 CSS */
.recruit-sales-box{
  display: inline-block;
  position: relative;
  width: 210px;
}
.sales-logo{
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background-color: grey;
  display: inline-block;
}
.sales-name{
  display: inline-block;
  position: absolute;
  top: 5px;
  margin-left: 5px;
  color: #818181;
}

.pagination{
  color: #1f5abc;
  list-style: none;
  cursor: pointer;
  font-size: 14px;
}

/* Icon  */
.awesome-icon{
  color: #2AC1DF;
  height: 30px;
}

/* Action アクション*/
.recruit-content:hover{
  opacity: 0.8;
  box-shadow: 0 15px 30px -5px rgba(0,0,0,.15), 0 0 5px rgba(0,0,0,.1);
	transform: translateY(-4px);
}


/* レスポンシブ デザイン */
@media screen and (max-width: 767px) {
  .recruit-wrapper{
    width: 90%;
    margin: 0 auto;
  }
  .recruit-content{
    /* width: calc(100% - 40px); */
    width: 90%;
  }
  .paginate{
    width: 100%;
    margin: 0;
    padding: 0;
    /* background-color: green; */
  }
  .recruit-topbox{
    width: 100%;
  }
  .create-time{
    font-size: 11px;
  }
  .create-work{
    width: 20%;
  }
  .matching-status{
    width: 30%;
  }
  .recruit-centerbox{
    width: 100%;
    height: 60%;
    position: relative;
  }
  .recruit-title-box{
    height: 54%;
    font-size: 14px;
    overflow: hidden; /* 文字制限 */
    text-overflow: ellipsis; /* 文字制限 */
  }
  .recruit-company-box{
    position: absolute;
    bottom: 3px;
  }
  .recruit-btmbox{
    width: 100%;
    height: 30%;
  }
  .recruit-detail-box{
    width: 100%;
    height: 22px;
    /* background-color: #f09819; */
  }
  .money-area{
    width: 49%;
    font-size: 9px;
    display: inline-block;
  }
  .location-area{
    width: 49%;
    font-size: 9px;
    display: inline-block;
  }
  .recruit-skill-box{
    width: 100%;
    height: 30%;
  }
  .skill-logo{
    width: 20%;
    font-size: 9px;
    height: 80%;
    display: inline-block;
  }
  .skill-content{
    width: 100%;
    font-size: 11px;
    display: inline-block;
    overflow: hidden; /* 文字制限 */
    text-overflow: ellipsis; /* 文字制限 */
    height: 12px;
  }
  /* エージェント 表示 */
  /* .recruit-sales-box{
    display: none;
  } */
  .pagination{
    margin: 0;
  }

}

</style>

