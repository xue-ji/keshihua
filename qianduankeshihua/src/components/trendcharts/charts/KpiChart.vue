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
import { getKpiApi } from '@/apis/chart'

use([CanvasRenderer, BarChart, TitleComponent, TooltipComponent, GridComponent])

// 定义维修数据类型
interface DataItem {
  yuefen: string
  choujian: number
  gongzi: number
  tongxun: number
  zhaofan: number
  fangong: number
  zhitong: number
}

// 响应式容器
const data = ref<DataItem[]>([])

// window.setInterval(()=>{
//   getxinbuliang();
// }, 30000)
// 维修数据接口
const getkpi = async () => {
  const res = await getKpiApi()
  console.log(res)
  data.value = res.data
  option.value.xAxis[0].data = data.value.map((item) => item.yuefen)
  option.value.series[0].data = data.value.map((item) => item.gongzi)
  option.value.series[1].data = data.value.map((item) => item.tongxun)
  option.value.series[2].data = data.value.map((item) => item.fangong)
  option.value.series[3].data = data.value.map((item) => item.zhaofan)
  option.value.series[4].data = data.value.map((item) => item.choujian)
  option.value.series[5].data = data.value.map((item) => item.zhitong)




}
getkpi()

const colors = ['#5470C6', '#91CC75', '#EE6666', '#12563c', '#173878', '#6e9675']
const option = ref({
  title: {
    text: 'KPI',
    left: 'left'
  },
  color: colors,

  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  grid: {
    right: '20%'
  },
  toolbox: {
    feature: {
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  legend: {
    data: ['工资成本', '通讯上线DPPM', '返工工时', 'PC产品5月早返率(DPPM)', '抽检良率', '直通率']
  },
  xAxis: [
    {
      type: 'category',
      axisTick: {
        alignWithLabel: true
      },
      // prettier-ignore
      data: [1, 2, 3]
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: '工资成本',
      position: 'right',
      alignTicks: true,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[0]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    {
      type: 'value',
      name: '通讯上线DPPM',
      position: 'right',
      alignTicks: true,
      offset: 60,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[1]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    {
      type: 'value',
      name: '返工工时',
      position: 'right',
      alignTicks: true,
      offset: 120,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[2]
        }
      },
      axisLabel: {
        formatter: '{value} h'
      }
    },
    {
      type: 'value',
      name: 'PC产品5月早返率(DPPM)',
      position: 'right',
      alignTicks: true,
      offset: 180,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[3]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },
    {
      type: 'value',
      name: '抽检良率',
      position: 'left',
      alignTicks: true,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[4]
        }
      },
      axisLabel: {
        formatter: '{value} %'
      }
    },
    {
      type: 'value',
      name: '直通率',
      position: 'left',
      alignTicks: true,
      offset: 60,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[5]
        }
      },
      axisLabel: {
        formatter: '{value} %'
      }
    },
  ],
  series: [
    {
      name: '工资成本',
      type: 'bar',
      label: {
        show: true,
        position: 'top',
        valueAnimation: true,
      },
      data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    },
    {
      name: '通讯上线DPPM',
      type: 'bar',
      yAxisIndex: 1,
      label: {
        show: true,
        position: 'top',
      },
      data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    },
    {
      name: '返工工时',
      type: 'bar',
      yAxisIndex: 2,
      label: {
        show: true,
        position: 'top',
      },
      data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    },
    {
      name: 'PC产品5月早返率(DPPM)',
      type: 'bar',
      yAxisIndex: 3,
      label: {
        show: true,
        position: 'top',
      },
      data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    },
    {
      name: '抽检良率',
      type: 'line',
      yAxisIndex: 4,
      label: {
        show: true,
        position: 'top',
      },
      data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    },
    {
      name: '直通率',
      type: 'line',
      yAxisIndex: 5,
      label: {
        show: true,
        position: 'top',
      },
      data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    },
  ]
})
</script>

<style scoped></style>
