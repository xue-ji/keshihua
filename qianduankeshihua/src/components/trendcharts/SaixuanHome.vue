<template>
  <el-form>
    <div class="demo-date-picker">
      <div class="select">
        <span class="demonstration">线体</span>
        <el-select
          v-model="value"
          multiple
          clearable
          collapse-tags
          placeholder="线别"
          popper-class="custom-header"
          :max-collapse-tags="1"
        >
          <template #header>
            <el-checkbox v-model="checkAll" :indeterminate="indeterminate" @change="handleCheckAll">
              All
            </el-checkbox>
          </template>
          <el-option
            v-for="item in cities"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </div>

      <!-- 时间选择器 -->
      <div class="block">
        <span class="demonstration">不良时间</span>
        <el-date-picker
          v-model="value2"
          type="daterange"
          unlink-panels
          range-separator="To"
          start-placeholder="开始时间"
          end-placeholder="结束时间"
          :shortcuts="shortcuts"
        />
      </div>
      <div class="btns">
        <el-button type="primary" class="btn" @click="songsuo">搜索</el-button>
      </div>
    </div>
  </el-form>
  <div class="wrap">
    <PieChart class="item" v-if="xianshi == 1" :shuju="data1" @refresh="xiangqin"></PieChart>
    <BarChart class="item" v-if="xianshi == 1 && xq_xianshi == 1" :shuju="xq_data" @jixin="jixing"></BarChart>
    <BarChart2 class="item" v-if="xianshi == 1 && xq_xianshi == 1 && jx_xianshi == 1" :shuju="jx_data"></BarChart2>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import type { CheckboxValueType } from 'element-plus'
import { getXiantiApi, postxiantishijianApi, postxiangqinApi, postjixingApi } from '@/apis/chart'
import PieChart from './saixuan/PieChart.vue';
import BarChart from './saixuan/BarChart.vue';
import BarChart2 from './saixuan/BarChart2.vue';
import { time } from 'console'

const checkAll = ref(true)
const indeterminate = ref(false)
const value = ref<CheckboxValueType[]>([])

const value2 = ref('')

interface XiantiItem {
  typeName: string
}
interface DataItem {
  typeName: string
  num: number
  percentage: number
}

interface WeihaoItem {
  weihao: string
  num: number
}
interface JixingItem {
  jixing: string
  num: number
}
// interface XiantiShuju {
//   DAYS: number
//   PROCESS_NAME: string
//   '不良原因': string
//   '不良时间': string
//   '不良现象': string
//   '备注': null
//   '客户条码': null
//   '工作站': string
//   '工单': string
//   '工单线体': string
//   '成品料号': number
//   '成品料号描述': string
//   '新厂商描述': string
//   '新料号': string
//   '新料号DC': string
//   '新料号Lot': string
//   '新料号Reel': string
//   '新料号描述': string
//   '旧厂商描述': string
//   '旧料号': string
//   '旧料号DC': string
//   '旧料号Lot': string
//   '旧料号Reel': string
//   '旧料号描述': string
//   '条码': string
//   '线别': string
//   '维修人员': string
//   '维修人工号': string
//   '维修位号': string
//   '维修料号': null
//   '维修方式': string
//   '维修时间': string
//   '责任类别': string
//   '送修时间': string
// }

const data = ref<XiantiItem[]>([])

const getxianti = async () => {
  const res = await getXiantiApi()
  console.log(res)
  data.value = res.data
  cities.value = data.value.map((item) => ({
    value: item.typeName,
    label: item.typeName
  }))
  // 开始默认全选
  value.value = cities.value.map((_) => _.value)
}
getxianti()

const cities = ref([
  {
    value: 'Beijing',
    label: 'Beijing'
  }
])

watch(value, (val) => {
  if (val.length === 0) {
    checkAll.value = false
    indeterminate.value = false
  } else if (val.length === cities.value.length) {
    checkAll.value = true
    indeterminate.value = false
  } else {
    indeterminate.value = true
  }
})
const handleCheckAll = (val: CheckboxValueType) => {
  indeterminate.value = false
  if (val) {
    value.value = cities.value.map((_) => _.value)
  } else {
    value.value = []
  }
}

const shortcuts = [
  {
    text: '上一周',
    value: () => {
      const end = new Date()
      const start = new Date()
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
      return [start, end]
    }
  },
  {
    text: '上一个月',
    value: () => {
      const end = new Date()
      const start = new Date()
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
      return [start, end]
    }
  },
  {
    text: '上三个月',
    value: () => {
      const end = new Date()
      const start = new Date()
      start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
      return [start, end]
    }
  }
]

// 搜索部分
const xianshi = ref(0)
const data1 = ref<DataItem[]>([])
const data2 = ref([])
const songsuo = async () => {
  const res = await postxiantishijianApi({
    xianti: value.value,
    time: value2.value.toLocaleString(),
  })
  data1.value = res.data[0]
  data2.value = res.data[1]
  console.log(data2)
  xianshi.value = 1
}

// 详情部分
const xq_xianshi = ref(0)
const xq_data = ref<WeihaoItem[]>([])
const xq_tiaoma = ref([])
const xiangqin = async (mingchen) => {
  const res = await postxiangqinApi({
    name:mingchen,
    tiaoma:data2.value,
  })
  xq_data.value = res.data[0]
  xq_tiaoma.value = res.data[1]
  console.log(xq_data)
  xq_xianshi.value = 1
}


// 机型详情部分
const jx_xianshi = ref(0)
const jx_data = ref<JixingItem[]>([])
const jixing = async (wh) => {
  const res = await postjixingApi({
    weihao:wh,
    tiaoma:xq_tiaoma.value,
  })
  jx_data.value = res.data[0]
  console.log(jx_data)
  jx_xianshi.value = 1
}


</script>

<style lang="scss" scoped>
.custom-header {
  .el-checkbox {
    display: flex;
    height: unset;
  }
}

.demo-date-picker {
  display: flex;
  width: 100%;
  padding: 15px 0;
  // line-height: 26px;
  flex-wrap: wrap;
  box-shadow: var(--el-box-shadow-light);
  .select {
    // display: flex;
    // flex: 1;
    flex-direction: column;
    justify-content: center;
    // text-align: center;
  }
  .block {
    display: flex;
    border-right: solid 1px var(--el-border-color);
    // flex: 1;
    :last-child {
      border-right: none;
    }
  }
  .demonstration {
    // display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    // margin-right: 20px;
    margin-bottom: 20px;
  }
  .btns {
    display: flex;
    // flex: 2;
    flex-direction: column;
    align-items: center;
    .btn {
      width: 100%;
      border-radius: 20px;
      cursor: pointer;
    }
  }
}

.wrap {
  display: flex;
  flex-wrap: wrap;
  margin-top: 10px;
  box-shadow: var(--el-box-shadow-light);

  .item {
    height: 90vh;
    min-height: 360px;
    padding: 20px;
    border: 1px solid #f5f5f5;
  }
}
</style>
