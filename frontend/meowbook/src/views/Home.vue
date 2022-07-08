<template>
  <div>
    <h1>Home</h1>
    <input type="text" v-model="search" />
    <form @submit.prevent="buscar">
      <button type="submit" id="submit">buscar</button>
    </form>
    <div v-for="dato in lists" :key="dato.libro_id">
      <ul style="border: 1px solid black">
        <li class="libro">
          <h4>{{ dato.libro_titulo }}</h4>
          <ul class="conjunto-libros">
            <p>ISBN:</p>
            <li>{{ dato.libro_isbn }}</li>
            <h1></h1>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
let firstName = sessionStorage.getItem("current_user");
console.log("current_user: ", firstName);
export default {
  name: "Home",
  data() {
    return {
      lists: [],
    };
  },
  methods: {
    async buscar() {
      const url = "http://127.0.0.1:5000/libros";
      const response = await fetch(url, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.groupCollapsed("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      this.lists = data.libros;
    },
  },
};
</script>

<style>
.libro {
  display: flex;
  text-decoration: none;
}

.conjunto-libro {
  padding: 2px;
  text-decoration: none;
  justify-content: left;
}

.elemento-libro {
  padding: 2px;
  text-decoration: none;
  justify-content: left;
}
</style>
