<template>
  <div>
    <h1>Home</h1>
    <input type="text" v-model="search" />
    <button type="submit">search</button>
    <ul style="border: 1px solid black">
      <li class="libro">
        <h4>Título Libro</h4>
        <ul class="conjunto-libros">
          <li class="elemento-libro">Autor: -------------------</li>
          <li class="elemento-libro">Publicación: -------------</li>
          <li class="elemento-libro">Editorial: ----------------</li>
          <li class="elemento-libro">ISBN: ---------------------</li>
        </ul>
      </li>
    </ul>
    <p>{{ search }}</p>
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
