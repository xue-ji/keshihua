import {post, get} from "./service"

export const BuLingApi = data=> {
    return get({
        url:"/buliang/",
        data
    })
}


