<template>
  <div>
    <h1>LikeBooks</h1>
    <input type="text" v-model="search" />
    <button>search</button>
    <ul class="libros">
      <li class="libro">
        <h4>Título</h4>
        <ul class="especificaciones">
          <li class="elemento">Autor:</li>
          <li class="elemento">Publicación:</li>
          <li class="elemento">ISBN:</li>
        </ul>
        <input type="checkbox" id="checkbox" value="Like" />
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "LikeBooks",
};
</script>

<style>
.libros {
  border: 1px solid black;
  text-align: justify;
  display: flex;
}

.libro {
  border: 1px solid red;
  list-style: none;
}
.especificaciones {
  list-style: none;
  display: flex;
  flex-direction: column;
}
.elemento {
  padding: 5px;
  border: 1px solid black;
}
</style>
