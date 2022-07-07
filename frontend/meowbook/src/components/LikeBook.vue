<template>
  <li>
    <h3>Título</h3>
    <ul>
      <li>Autor: {{ autor }}</li>
      <li>Sinopsis: {{ sinopsis }}</li>
      <li>Editorial {{ editorial }}</li>
      <li>Fecha de publicación: {{ FechaDePublicacion }}</li>
      <li>ISBN: {{ isbn }}</li>
    </ul>
  </li>
</template>

<script>
export default {
  data() {
    return {
      autor: "Mario Vargas Llosa",
      sinopsis: "ajhbwabfkbgakbfjhabfjhabfjhbajhbajhbfhjafjhabfjh",
      editorial: "EditorialDeBolsillo",
      FechaDePublicacion: "25/09/2002",
      isbn: "987 - 654 - 321",
    };
  },
};
</script>
