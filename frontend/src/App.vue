<template>
  <router-view></router-view>
</template>

<script>

export default {
  name: 'App',

}
</script>

<style lang="scss">

body{
  background: var(--greyLight-1);
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

  & input:-webkit-autofill{
  -webkit-text-fill-color: var(--greyDark);
}
 & input:-webkit-autofill:focus{
  -webkit-text-fill-color: var(--greyDark);
}
}
</style>
