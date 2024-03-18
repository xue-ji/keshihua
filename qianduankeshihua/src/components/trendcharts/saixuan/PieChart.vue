<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script lang="ts" setup>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components';
import VChart from 'vue-echarts';
import { ref, onUpdated, onMounted } from 'vue';

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])



// 定义维修数据类型
// interface DataItem {
//   typeName: string;
//   num: number;
//   percentage: number;
// }

// // 响应式容器
// const data = ref<DataItem[]>([])

// window.setInterval(()=>{
//   getxinbuliang();
// }, 30000)
// 维修数据接口
// const getxinbuliang = async () => {
//   const res = await getXinbuliangApi();
//   console.log(res);
//   data.value = res.data;
  // option.value.legend.data = data.value.map((item)=>item.typeName );
  // option.value.series[0].data = data.value.map((item)=>({
//     value:item.num,
//     name:item.typeName,
//   }))
// };
// getxinbuliang();

const yyy = defineProps({
  shuju: {
    type: Object,
  }
})
// option.value.legend.data = yyy.shuju.value.map((item)=>item.typeName );
// option.value.series[0].data = yyy.shuju.value.map((item)=>({
//   value:item.num,
//   name:item.typeName,
// }))
// onServerPrefetch(async () => {
//   option.value.legend.data = await yyy.shuju.map((item)=>item.typeName );
//   option.value.series[0].data = await yyy.shuju.map((item)=>({
//     value:item.num,
//     name:item.typeName,
//   }))
// })

onMounted(() => {
  option.value.legend.data =  yyy.shuju.map((item)=>item.typeName );
  option.value.series[0].data =  yyy.shuju.map((item)=>({
    value:item.num,
    name:item.typeName,
  }))
  console.log(yyy.shuju)
})
onUpdated(() => {
  option.value.legend.data =  yyy.shuju.map((item)=>item.typeName );
  option.value.series[0].data =  yyy.shuju.map((item)=>({
    value:item.num,
    name:item.typeName,
  }))
  console.log(yyy.shuju)
})

// console.log(yyy.shuju)
// console.log(option.value.legend)

const option = ref({
  title: {
    text: '维修数据',
    left: 'center'
  },
  tooltip: {
    enterable: true,
    triggerOn: 'mousemove',
    trigger: 'item',
    // 浮层隐藏的延迟
    hideDelay: 100,
    position: 'inside', 
    formatter: function (params) {
               return `<div class=chartLabel>
              <div class=title>${params.seriesName}</div>
              <div class=label>${params.name}:${params.value} (${params.percent}%)</div>
              <button id="btn-tooltip">查看更多</button>
            </div>`
    }

  },
  // 标题分类
  legend: {
    orient: 'vertical',
    left: 'left',
    data: ['Direct', 'Email', 'Ad Networks', 'Video Ads', 'Search Engines'],
  },
  series: [
    {
      name: '不良原因',
      type: 'pie',
      radius: '55%',
      center: ['70%', '60%'],
      // 数据
      data: [
        { value: 335, name: 'Direct' },
        { value: 310, name: 'Email' },
        { value: 234, name: 'Ad Networks' },
        { value: 135, name: 'Video Ads' },
        { value: 1548, name: 'Search Engines' }
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        },
      }
    }
  ]
})
</script>

<style scoped></style>
