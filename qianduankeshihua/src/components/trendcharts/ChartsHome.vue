<template>
    <div class="wrap">
        <PieChart class="item"></PieChart>
        <BarChart class="item"></BarChart>
        <LineChart class="item"></LineChart>
        <WeiXiu class="item"></WeiXiu>
        <MeiGui class="item"></MeiGui>
        <KpiChart class="item"></KpiChart>

    </div>
</template>

<script setup lang="ts">
import BarChart from "./charts/BarChart.vue";
import LineChart from "./charts/LineChart.vue";
import PieChart from "./charts/PieChart.vue";
import WeiXiu from "./charts/WeiXiu.vue";
import MeiGui from "./charts/MeiGui.vue";
import KpiChart from "./charts/KpiChart.vue";


</script>

<style lang="scss" scoped>

.wrap {
    display: flex;
    flex-wrap: wrap;
    box-shadow: var(--el-box-shadow-light);

    .item {
        height: 90vh;
        min-height: 360px;
        padding: 20px;
        border: 1px solid #f5f5f5; 
    }
}

</style>

