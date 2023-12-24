<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script lang="ts" setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'

import { PieChart } from 'echarts/charts'
import { LabelLayout } from 'echarts/features'
import { ToolboxComponent, LegendComponent } from 'echarts/components'
import VChart from 'vue-echarts'
import { ref } from 'vue'
import { getXinbuliangApi } from '@/apis/chart'

use([CanvasRenderer, PieChart, LabelLayout, ToolboxComponent, LegendComponent])

// 定义维修数据类型
interface DataItem {
  typeName: string
  num: number
  percentage: number
}

// 响应式容器
const data = ref<DataItem[]>([])

// window.setInterval(()=>{
//   getxinbuliang();
// }, 30000)
// 维修数据接口
const getxinbuliang = async () => {
  const res = await getXinbuliangApi()
  console.log(res)
  data.value = res.data
  //   option.value.legend.data = data.value.map((item) => item.typeName)
  option.value.series[0].data = data.value.map((item) => ({
    value: item.num,
    name: item.typeName
  }))
}
getxinbuliang()

const option = ref({
  title: {
    text: '维修数据',
    left: 'center'
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)'
  },
  // 标题分类
  legend: {
    top: 'bottom'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Nightingale Chart',
      type: 'pie',
      radius: [50, 250],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 40, name: 'rose 1' },
        { value: 38, name: 'rose 2' },
        { value: 32, name: 'rose 3' },
        { value: 30, name: 'rose 4' },
        { value: 28, name: 'rose 5' },
        { value: 26, name: 'rose 6' },
        { value: 22, name: 'rose 7' },
        { value: 18, name: 'rose 8' }
      ]
    }
  ]
})
</script>

<style scoped></style>
