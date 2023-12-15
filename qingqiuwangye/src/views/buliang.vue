<template>
    <button @click="buliang" >buliang</button>
  </template>

<script>
export default {
  name: "buliang",
  setup(){
    const buliang=()=>{
      alert("你好")
      BuLingApi().then(res=>{
        
        console.log(res)
      })

    }
    const data=reactive({

    })
    return {
      ...toRefs(data),
      buliang
    }
  }
}

</script>
