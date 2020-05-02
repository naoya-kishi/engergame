<template>
  <div>
    <article-detail
      :data="ArticleData"
    >
    </article-detail>
  </div>
</template>

<script>
import ArticleDetail from '../components/ArticleDetail';

export default {
  computed: {
    ArticleData() {
      const dataId = parseInt(this.$route.params.id, 10);
      const data = this.$store.state.articles.find(a => (
        a.id === dataId
      ));
      return data;
    },
  },
  components: {
    articleDetail,
  },
};
</script>