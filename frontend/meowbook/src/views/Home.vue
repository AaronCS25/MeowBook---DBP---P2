<template>
  <div>
    <h1>Home</h1>
    <input type="text" t-model="search">
    <p>{{search}}</p>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      search: ''
    }
  }
};
</script>
