<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import {
  ToolboxComponent,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  DataZoomComponent,
  GridComponent
} from 'echarts/components'
import VChart from 'vue-echarts'
import { ref } from 'vue'
import { getXinbuliangApi } from '@/apis/chart'

use([
  ToolboxComponent,
  CanvasRenderer,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  DataZoomComponent,
  GridComponent
])

// 定义维修数据类型
interface DataItem {
  typeName: string
  num: number
  percentage: number
}

//   响应式容器
const data = ref<DataItem[]>([])

//   window.setInterval(()=>{
//     getxinbuliang();
//   }, 30000)
//   维修数据接口
const getxinbuliang = async () => {
  const res = await getXinbuliangApi()
  console.log(res)
  data.value = res.data
    // option.value.legend.data = data.value.map((item) => item.typeName)
  option.value.xAxis.data = data.value.map((item) => item.typeName)

  option.value.series[0].data = data.value.map((item) => item.num)
}
getxinbuliang()

const option = ref({
  title: {
    text: '机型数据分析(slider-水平)'
    // left: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  //   tooltip: {
  //     trigger: 'axis',
  //     axisPointer: {
  //       type: 'shadow',
  //       label: {
  //         show: true
  //       }
  //     }
  //   },
  //   toolbox: {
  //     show: true,
  //     feature: {
  //       mark: { show: true },
  //       dataView: { show: true, readOnly: false },
  //       magicType: { show: true, type: ['line', 'bar'] },
  //       restore: { show: true },
  //       saveAsImage: { show: true }
  //     }
  //   },
  //   calculable: true,
    // legend: {
    //   orient: 'vertical',
    //   left: 'center',
    //   data: ['Growth', 'Budget 2011', 'Budget 2012'],
    //   // itemGap: 5
    // },
  grid: {
    top: '12%',
    left: '1%',
    right: '10%',
    containLabel: true
  },
  xAxis: {
    type: 'category',
    data: ['Growth', 'Budget 2011', 'Budget 2012']
  },
    
  yAxis: [
    {
      type: 'value',
        // name: 'Budget (million USD)',
        // axisLabel: {
        //   formatter: function (a: number) {
        //     a = +a
        //     return isFinite(a) ? echarts.format.addCommas(+a / 1000) : ''
        //   }
        // }
    }
  ],
  dataZoom: [
    {
      show: true,
      start: 94,
      end: 100
    },
    {
      type: 'inside',
      start: 94,
      end: 100
    },
    {
      show: true,
      yAxisIndex: 0,
      filterMode: 'empty',
      width: 30,
      height: '80%',
      showDataShadow: true,
      left: '93%'
    }
  ],
  series: [
    {
      name: 'Budget 2011',
      type: 'bar',
      data: [150, 230, 224, 218, 135, 147, 260],
      showBackground: true,
      backgroundStyle: {
        color: 'rgba(180, 180, 180, 0.2)'
      },
      label: {
        show: true,
        // position: 'TOP',
        valueAnimation: true,
        },
    },
  ]
})
</script>

<style scoped></style>
