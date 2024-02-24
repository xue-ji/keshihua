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
          <el-button type="primary" class="btn" @click="login">搜索</el-button>
          
        </div>
    </div>
  </el-form>
  <div class="wrap">
    <PieChart class="item"></PieChart>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import type { CheckboxValueType } from 'element-plus'
import { getXiantiApi } from '@/apis/chart'
import PieChart from './saixuan/PieChart.vue'

const checkAll = ref(true)
const indeterminate = ref(false)
const value = ref<CheckboxValueType[]>([])

const value2 = ref('')

interface XiantiItem {
  typeName: string
}

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
