<template>
  <div id="home">
    <el-container>
      <el-header>
          <AdminHeader></AdminHeader>
      </el-header>
      <el-container> 
        <el-aside width="200px">
            <AdminMenu></AdminMenu>
        </el-aside>
        <el-main>
          <RouterView/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import AdminHeader from "@/components/layout/AdminHeader.vue";
import AdminMenu from "@/components/layout/AdminMenu.vue";

// import { useUserInfoStore } from "@/stores/userinfo.store";
// import { getUserInfoApi } from "@/apis/userinfo"
// // 请求用户数据
// const userInfoStore = useUserInfoStore();
// const getUserinfo = async () => {
//   const res = await getUserInfoApi();
//   console.log(res)
// }
// getUserinfo();
</script>

<style lang="scss" scoped>

#home {
  min-height: 100vh;
}
.el-header {
  position: relative;
  width: 100%;
  background-color: #2b2c43;
  padding: 0;
}
.el-aside {
  position: absolute;
  display: block;
  left: 0;
  top: 60px;
  bottom: 0;
  background-color: #2b2c43;
  min-height: calc(100vh - 60px);
}
.el-main {
  position: absolute;
  top: 60px;
  left: 200px;
  right: 0;
  bottom: 0;
  // 显示下拉滚动
  overflow-y: scroll;
}

</style>
