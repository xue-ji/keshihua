<template>
  <div id="header">
    <div class="logo-box">长城电源质量部</div>
    <div class="right-box">
      <div class="title">可视化页面</div>
      <el-switch
        v-model="value5"
        class="ml-2"
        inline-prompt
        style="--el-switch-on-color: #13ce66; --el-switch-off-color: #ff4949"
        active-text="开启自动更新"
        inactive-text="取消自动更新"
      />
      <div class="avater-box">
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const value5 = ref(true)
</script>

<style lang="scss" scoped>
#header {
  background-color: #2b2c44;
  color: #fff;
  display: flex;
  justify-content: space-between;

  .logo-box {
    width: 200px;
    text-align: center;
    line-height: 60px;
    font-size: 22px;
    font-weight: bold;
    color: #e73267;
  }

  .right-box {
    flex: 1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18px;
    .el-avater {
      margin-right: 10px;
    }
  }
}
</style>
