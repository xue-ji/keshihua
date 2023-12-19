import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import path from 'node:path'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // // 跨域处理
  // server: {
  //   proxy: {
  //     "api": {
  //       // 配置需要代理的路径 --> 这里的意思是代理 http://localhost:80/api/后的所有路由
  //       target: "http://xxx.xxx.xxx.xxx:xx", // 目标地址 --> 服务器路径
  //       changeOrigin: true, // 允许跨越，
  //       ws: true, // 允许 websocket代理
  //       // 重写路径 --> 作用与vue配置pathRewrite作用相同
  //       rewrite: (path) => path.replace(/^\/api/, ""),
  //     }
  //   }
  // }
})
