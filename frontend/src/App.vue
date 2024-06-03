<template>
  <div id="app">
    <el-container>
      <el-header id="main-header">在线书店信息管理系统</el-header>
      <router-view @call-parent-method="changeview"></router-view>
    </el-container>
  </div>
</template>

<script>

export default {
  name: 'App',
  // components: {
  //   LoginComp
  // },
  data() {
    return {
      curr_view: 0
    };
  },
  methods: {
    showview() {
      if (this.curr_view === 1)
        this.$router.push({ name: 'show' }, () => { }, () => { });
      else
        this.$router.push({ name: 'login' }, () => { }, () => { });
    },
    changeview() {
      if (this.curr_view === 1){
        this.$router.push({ name: 'login' }, () => { }, () => { });
        this.curr_view = 0
      }
      else{
        this.$router.push({ name: 'show' }, () => { }, () => { });
        this.curr_view = 1
      }
      sessionStorage.setItem('curr_view', this.curr_view);
    }
  },
  mounted() {
    const savedView = sessionStorage.getItem('curr_view');
    if (savedView !== null) {
      this.curr_view = parseInt(savedView);
    }
    this.showview();
  }
}
</script>

<style>
#main-header {
  color: #333;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  font-size: xx-large;
  border-bottom: gray solid 2px;
}
</style>
