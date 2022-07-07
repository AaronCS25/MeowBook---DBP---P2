<template>
  <div>
    <h1>Home</h1>
    <input type="text" v-model="search" />
    <button>search</button>
    <h1>{{ search }}</h1>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      search: "",
    };
  },
};
</script>
