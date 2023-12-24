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
  import { ref } from 'vue'
  import { getBarXinbuliangApi } from '@/apis/chart'
  
  use([CanvasRenderer, BarChart, TitleComponent, TooltipComponent, GridComponent])
  
  // 定义维修数据类型
  interface DataItem {
    typeName: string;
    num: number;
    percentage: number;
  }
  
  // 响应式容器
const data = ref<DataItem[]>([])
  
  // window.setInterval(()=>{
  //   getxinbuliang();
  // }, 30000)
  // 维修数据接口
  const getxinbuliang = async () => {
    const res = await getBarXinbuliangApi();
    console.log(res);
    data.value = res.data;
    option.value.xAxis.data = data.value.map((item)=>item.typeName );
    option.value.series[0].data = data.value.map((item)=> item.num)
  };
  getxinbuliang();
  
const option = ref({
    title: {
      text: '维修数据',
      left: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
        }
    ]
  })
  </script>
  
  <style scoped></style>
  