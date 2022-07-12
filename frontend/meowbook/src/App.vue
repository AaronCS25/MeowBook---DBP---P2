<template>
  <TheNavigation />
  <router-view />
</template>

<script>
import TheNavigation from "./components/TheNavigation.vue";

export default {
  name: "App",
  components: {
    TheNavigation,
  },
};
</script>

<style>
#app {
  position: absolute;
  top: 0px;
  left: 0px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fdfdfd;
  height: 100%;
  width: 100%;
  margin: auto 0px;
  background: rgb(51, 76, 108);
}
</style>
