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
import { defineEmits } from 'vue'  
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
    percent:item.percentage,
  }))
  
})
onUpdated(() => {
  option.value.legend.data =  yyy.shuju.map((item)=>item.typeName );
  option.value.series[0].data =  yyy.shuju.map((item)=>({
    value:item.num,
    name:item.typeName,
    percent:item.percentage,
  }))
  
})

// 定义派发事件
let emit = defineEmits(['refresh'])
// const fanhui = () => {
//   emit('refresh')
//   console.log('chuchcu')
// }

// console.log(yyy.shuju)
// console.log(option.value.legend)
window.myDialog = (shuju) => {
  emit('refresh', shuju)
}

const option = ref({
  title: {
    text: '维修数据',
    left: 'center'
  },
  tooltip: {
    enterable: true,
    // triggerOn: 'mousemove',
    trigger: 'item',
    triggerOn: "mousemove", 
    // 浮层隐藏的延迟
    hideDelay: 100,
    position: 'inside', 
    formatter: function (params) {
        
        return `<div class=chartLabel>
              <div class=title>${params.seriesName}</div>
              <div class=label>${params.name}:${params.value}  (${params.percent}%)</div>
              <button onclick="myDialog('${params.name}')">查看更多</button>
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
      center: ['50%', '50%'],
      avoidLabelOverlap: true,
      labelLayout: {
        hideOverlap: false
      },
      label: {
        alignTo: 'labelLine', // ! 文字对齐方式
        formatter: function (e) {
            let {
                data: { value, name, percent },
            } = e;
            return `{x|}{a|${name}}\n{b|${value}个}{c|${percent}%}`;
        },
        minMargin: 5,
        lineHeight: 15,
        rich: {
            x: { width: 10, height: 10, backgroundColor: 'inherit', borderRadius: 5 },
            a: { fontSize: 14, color: 'inherit', padding: [0, 20, 0, 8] },
            b: { fontSize: 12, align: 'left', color: '#666666', padding: [8, 0, 0, 18] },
            c: { fontSize: 12, align: 'left', color: '#666666', padding: [8, 0, 0, 8] },
        },
      },
      // 数据
      data: [
        { value: 335, name: 'Direct', percent: 123 },

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

<style scoped>

</style>
