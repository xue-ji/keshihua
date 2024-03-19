<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import { GridComponent } from 'echarts/components'
import { TitleComponent, TooltipComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { ref, onUpdated, onMounted } from 'vue'
// import { getBarXinbuliangApi } from '@/apis/chart'
import { defineEmits } from 'vue'

use([CanvasRenderer, BarChart, TitleComponent, TooltipComponent, GridComponent])

//   // 定义维修数据类型
//   interface DataItem {
//     typeName: string;
//     num: number;
//     percentage: number;
//   }

//   // 响应式容器
// const data = ref<DataItem[]>([])

// window.setInterval(()=>{
//   getxinbuliang();
// }, 30000)
// 维修数据接口
// const getxinbuliang = async () => {
//   const res = await getBarXinbuliangApi();
//   console.log(res);
//   data.value = res.data;
//   option.value.xAxis.data = data.value.map((item)=>item.typeName );
//   option.value.series[0].data = data.value.map((item)=> item.num)
// };
// getxinbuliang();

const yyy = defineProps({
  shuju: {
    type: Object
  }
})

onMounted(() => {
  option.value.xAxis.data = yyy.shuju.map((item) => item.jixing)
  option.value.series[0].data = yyy.shuju.map((item) => item.num)
})
onUpdated(() => {
  option.value.xAxis.data = yyy.shuju.map((item) => item.jixing)
  option.value.series[0].data = yyy.shuju.map((item) => item.num)
})

const option = ref({
  title: {
    text: '共性不良机型',
    left: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  xAxis: {
    axisLabel: {
      interval: 0, //代表显示所有x轴标签显示
      rotate:15, //代表逆时针旋转45度
    },
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '不良位号',
      data: [120, 200, 150, 80, 70, 110, 130],
      type: 'bar',
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.2)'
      },
      label: {
        show: true,
        // position: 'TOP',
        valueAnimation: true
      },
    }
  ]
})
</script>

<style scoped></style>
