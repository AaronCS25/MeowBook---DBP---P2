<template>
  <div id="nav">
    <router-link to="/home">Home</router-link> |
    <router-link to="/guardados">LikeBooks</router-link> |
    <router-link to="/perfil">Perfil</router-link> |
    <router-link to="/">Cerrar Sesión</router-link>
  </div>
</template>

<script>
export default {
  name: "TheNavigation",
};
</script>

<style scoped>
#nav {
  padding: 20px;
}

#nav a {
  font-weight: bold;
  color: #295e93;
}

#nav a.router-link-exact-active {
  color: #42a7b9;
}
</style>
