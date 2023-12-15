import axios from "axios";
import { ElLoading, ElMessage } from "element-plus";

// 使用 create 创建 axios 实例
let loadingObj = null

const Service = axios.create({
    timeout:8000,
    baseURL:"http://127.0.0.1:8000",
    changeOrigin: true,
    headers:{
        "Content-Type" : "application/json;chartset=utf-8"
    }
})

// 请求拦截-增加loading，对请求做统一处理
 Service.interceptors.request.use(config=>{
    loadingObj = ElLoading.service({
        lock: true,
        text: 'Loading',
        background: 'rgba(0, 0, 0, 0.7)',
    })
    return config
 })

// 响应拦截-对返回值做统一处理
Service.interceptors.response.use(res=>{
    loadingObj.close()
    return res.data

},error=>{
    // loadingObj.close()
    ElMessage({
        message:"服务器错误",
        type:"error",
        duration:2000
    })
})

// post 请求
export const post=config=>{
    return Service({
        ...config,
        method:'post',
        data:config.data
    })
}

// get 请求
export const get=config=>{
    return Service({
        ...config,
        method:'get',
        data:config.data
    })
}

