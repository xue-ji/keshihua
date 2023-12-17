<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div id="dom">{{ msg }}--{{ num }}</div>
    <button @click="buliang">buliang</button>
    <div v-html="shuju"></div>
  </div>
</template>

<script>
import { reactive, toRefs } from 'vue';
import { BuLingApi } from '@/util/request';
export default {
  // name:"about",
  setup() {
    const data = reactive({
      msg:"您好",
      msg2:"helloworld",
      num:0,
      shuju:''
    })
    const buliang=()=>{
      BuLingApi().then(res=>{
        console.log(res)
        data.shuju = res
      })

    }

    return{
      ...toRefs(data),
      buliang
    }
  }
}

</script>



