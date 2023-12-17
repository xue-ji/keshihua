<template>
    <button @click="buliang" >buliang</button>
    sdafdsfafasdasdfaasdasdafdsasdf
  </template>

<script>
import { reactive, toRefs } from 'vue';
import * as echarts from 'echarts';

export default {
  name: "buliang",
  setup(){
    const data = reactive({
      num:0,
    })
    const buliang=()=>{
      BuLingApi().then(res=>{
        console.log(res)
      })

    }
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

option = {
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '5%',
    left: 'center'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 1048, name: 'Search Engine' },
        { value: 735, name: 'Direct' },
        { value: 580, name: 'Email' },
        { value: 484, name: 'Union Ads' },
        { value: 300, name: 'Video Ads' }
      ]
    }
  ]
};
    return {
      ...toRefs(data),
      buliang
    }
  }
}

</script>
