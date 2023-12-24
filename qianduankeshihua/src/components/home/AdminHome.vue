<template>
    <div class="wrap">
        <AdminOverview class="item"></AdminOverview>
        <PieChart class="item"></PieChart>
        <BarChart class="item"></BarChart>
        <LineChart class="item"></LineChart>
        <WeiXiu class="item"></WeiXiu>

    </div>
</template>

<script setup lang="ts">
import AdminOverview from "./adminHome/AdminOverview.vue";
import BarChart from "./adminHome/BarChart.vue";
import LineChart from "./adminHome/LineChart.vue";
import PieChart from "./adminHome/PieChart.vue";
import WeiXiu from "./adminHome/WeiXiu.vue";

</script>

<style lang="scss" scoped>

.wrap {
    display: flex;
    flex-wrap: wrap;
    box-shadow: var(--el-box-shadow-light);

    .item {
        width: 50%;
        height: calc((100vh - 100px) / 2);
        min-height: 360px;
        padding: 20px;
        border: 1px solid #f5f5f5; 
    }
}

</style>

