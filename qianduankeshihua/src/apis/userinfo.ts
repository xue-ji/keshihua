import { $http } from "."

// 登录

export const getUserInfoApi = () => {
    return $http({
        method: "GET",
        url: "/user/info",
    })
}