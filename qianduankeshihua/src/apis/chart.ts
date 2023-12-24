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