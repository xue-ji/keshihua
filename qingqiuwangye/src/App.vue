<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/" >
          bulaing
        </RouterLink>
        <RouterLink to="/about">hebing</RouterLink>
        <RouterLink to="/buliang">
          <button v-on:click="buliang">bulaing</button>
        </RouterLink>
      </nav>
      
    </div>
  </header>

  <RouterView />
</template>

<script>
import { BuLingApi } from '@/util/request';
import { reactive, toRefs } from 'vue';

export default {
  name: "app",
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

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
