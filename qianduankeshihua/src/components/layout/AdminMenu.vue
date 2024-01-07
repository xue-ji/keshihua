<template>
  <div id="menu">
    <el-menu
      active-text-color="#fff"
      background-color="#2b2c44"
      class="el-menu-vertical-demo"
      :default-active="defaultActive"
      text-color="#c1c1c1"
      router 
    >
      <!-- 使用动态组件渲染菜单数据 -->
      <component
        :is="item.children?  ElSubMenu : ElMenuItem"
        v-for="item in menulist"
        :key="item.id"
        :index="item.index"
      >
        <template v-if="item.children" #title>
          <el-icon v-if="item.icon">
            <component :is="item.icon"></component>
          </el-icon>
          <span>{{ item.name }}</span>
        </template>
        <span v-if="!item.children">
          <el-icon v-if="item.icon">
            <component :is="item.icon"></component>
          </el-icon>
          <span>{{ item.name }}</span>
        </span>
        <el-menu-item v-for="subItem in item.children" :key="subItem.id" :index="subItem.index">
          {{ subItem.name }}
        </el-menu-item>
      </component>
    </el-menu>
  </div>
</template>

<script setup lang="ts">
import type { Component } from 'vue';
import { ElSubMenu, ElMenuItem } from 'element-plus';
import { House, User, Goods, TrendCharts } from '@element-plus/icons-vue/global';
import { ref } from "vue";
import router from '@/router';

// 完善菜单路由
const defaultActive = ref<string>(router.currentRoute.value.path);
// 使用动态组件渲染菜单数据
interface MenuItem {
  id: number
  name: string
  index: string
  icon?: Component
  children?: MenuItem[]
}
// 菜单假数据
const menulist: MenuItem[] = [
  {
    id: 1,
    name: '首页',
    index: '/home/admin-home',
    icon: House
  },
  {
    id: 2,
    name: '客诉管理',
    index: '/home/users',
    icon: User
  },
  {
    id: 3,
    name: '维修数据',
    index: '/home/charts',
    icon: TrendCharts, 
    children: [
      {
        id: 301,
        name: '基本数据',
        index: '/home/charts-jiben',
      },
      {
        id: 302,
        name: '筛选数据',
        index: '/home/charts-saixuan',
      },
    ],
  },
  {
    id: 101,
    name: '品质管理',
    index: '/home/goods',
    icon: Goods,
    children: [
      {
        id: 102,
        name: '。。管理',
        index: '/home/goods'
      },
      {
        id: 103,
        name: '。。管理',
        index: '/home/goods'
      },
      {
        id: 104,
        name: '。。管理',
        index: '/home/goods'
      },
      {
        id: 105,
        name: '。。管理',
        index: '/home/goods'
      },
      {
        id: 106,
        name: '。。管理',
        index: '/home/goods'
      },
    ],
  },
]
</script>

<style lang="scss" scoped></style>
