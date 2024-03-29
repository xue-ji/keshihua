import { $http } from "."

// 获取维修数据

export const getXinbuliangApi = () => {
    return $http({
        method: "GET",
        url: "/xinbuliang/",
    })
}

export const getBarXinbuliangApi = () => {
    return $http({
        method: "GET",
        url: "/xinbuliang/",
    })
}

export const getLineXinbuliangApi = () => {
    return $http({
        method: "GET",
        url: "/xinbuliang/",
    })
}

// 筛选数据页面获取线体
export const getXiantiApi = () => {
    return $http({
        method: "GET",
        url: "/xianti/",
    })
}

export const postxiantishijianApi = (data: {
    xianti: any[];
    time: string;

}) => {
    return $http({
        method: "POST",
        url: "/xiantishuju/",
        data
    })
}
// 详情部分
export const postxiangqinApi = (data: {
    name: string;
    tiaoma: any[];

}) => {
    return $http({
        method: "POST",
        url: "/xiangqin/",
        data
    })
}

// 机型详情部分
export const postjixingApi = (data: {
    weihao: string;
    tiaoma: any[];

}) => {
    return $http({
        method: "POST",
        url: "/jixing/",
        data
    })
}




// KPI接口
export const getKpiApi = () => {
    return $http({
        method: "GET",
        url: "/kpi/",
    })
}