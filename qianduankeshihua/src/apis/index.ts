import router from "@/router";
import axios, { AxiosError, type AxiosRequestConfig } from "axios";
import { ElMessage, ElLoading } from "element-plus";
export const httpInstance = axios.create();

export type BkResponse = {
    data: any;
    code: number;
    message: string;
    succeed: true;
};

// 设置请求根路径
httpInstance.defaults.baseURL=import.meta.env.VITE_BASEURL

// 配置响应拦截器
export const $http = async(config: AxiosRequestConfig) => {
    const loadingInstance = ElLoading.service()

    try {
        const axiosResponse = await httpInstance<BkResponse>(config);
        // 处理后端返回值有NAN 的问题
        let bkResponse;
        if (typeof(axiosResponse?.data) === "string") {
            bkResponse = JSON.parse(axiosResponse?.data.replace(/\bNaN\b/g,"null"))
        } else{
            bkResponse = axiosResponse.data
        }
        
        // 拦截器
        if (!bkResponse?.succeed) {
            let errTilte: string='Error';
            if (bkResponse.code === 401) {
                errTilte = "Unanthorized";
                ElMessage.error('未授权')
                router.push("/login")
                //...
            } else if (bkResponse.code === 403) {
                errTilte = "Forbidden";
            } else if (bkResponse.code === 9999) {
                errTilte = "9999Error";
            } else if (bkResponse.code === 500) {
                errTilte = "ServerError"
            } else {
                errTilte = "Unknown"
            }
            const err = new Error(bkResponse?.message || 'Unknown');
            err.name = errTilte
            throw err;
        }
        return bkResponse;
    } catch (err) {
        if (err instanceof AxiosError) {
            ElMessage.error('网络错误')
        }
        throw err;
    } finally {
        loadingInstance.close();
    }
};
