<template>
    <v-chart class="chart" :option="option" autoresize />
  </template>
  
  <script lang="ts" setup>
  import { use } from 'echarts/core'
  import { CanvasRenderer } from 'echarts/renderers'
  import { LineChart } from 'echarts/charts'
  import { TitleComponent, TooltipComponent,  } from 'echarts/components'
  import VChart from 'vue-echarts'
  import { ref } from 'vue'
  import { getLineXinbuliangApi } from '@/apis/chart'
  
  use([CanvasRenderer, LineChart, TitleComponent, TooltipComponent, ])
  
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
    const res = await getLineXinbuliangApi();
    console.log(res);
    data.value = res.data;
    option.value.xAxis.data = data.value.map((item)=>item.typeName );
    option.value.series[0].data = data.value.map((item)=>item.num)
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
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line'
        }
    ]
  })
  </script>
  
  <style scoped></style>
  