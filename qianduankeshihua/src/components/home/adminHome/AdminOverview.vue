<template>
    <div id="overview">
        <div class="userinfo">
            <el-avatar 
                src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            />
            <span class="username">xxx </span>
        </div>
        <div class="overview-list">
            <div class="overview-item" v-for="item in overviewData.allData" :key="item.id">
                <div class="title">{{ item.name }}</div>
                <div class="number">{{ item.number }}</div>
            </div>
        </div>
        <div class="overview-list">
            <div class="overview-item" v-for="item in overviewData.orderData" :key="item.id">
                <div class="title">{{ item.name }}</div>
                <div class="number">{{ item.number }}</div>
            </div>
        </div>

    </div>
 </template>

<script setup lang="ts">
import { ref } from "vue";

interface SingleData {
    id: number;
    name: string;
    number: string;
}
interface OverviewData {
    allData: SingleData[];
    orderData: SingleData[];
}

const overviewData = ref<OverviewData>({
    allData: [
        {
            id: 1,
            name: "数据标题",
            number: "836,387",
        },
        {
            id: 2,
            name: "数据标题",
            number: "836,387",
        },
        {
            id: 3,
            name: "数据标题",
            number: "836,387",
        },
        {
            id: 4,
            name: "数据标题",
            number: "836,387",
        },
    ],
    orderData: [
        {
            id: 1,
            name: "维修数据",
            number: "333",
        },
        {
            id: 1,
            name: "维修数据",
            number: "333",
        },
        {
            id: 1,
            name: "维修数据",
            number: "333",
        },
        {
            id: 1,
            name: "维修数据",
            number: "333",
        },
    ],
});







</script>


<style lang="scss" scoped>

#overview {
    .userinfo {
        display: flex;
        align-items: center;
        .username {
            margin-left: 10px;
        }
    }
    .overview-list {
        margin-top: 40px;
        display: flex;
        justify-content: space-between;
        .overview-item {
            width: 22%;
            display: flex;
            // 纵向排列
            flex-direction: column;
            align-items: center;
            justify-content: center;
            box-shadow: var(--el-box-shadow-light);
            border-radius: 10px;
            padding: 20px;
            .title {
                font-weight: 600;
                margin-bottom: 10px;
            }
            .number {
                font-size: 18px;
            }
        }
    }
}

</style>

