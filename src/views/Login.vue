<template>
  <div>
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login">
      <input v-model="nombre" placeholder="nombre" /><br />
      <input
        v-model="contrasena"
        type="password"
        placeholder="contraseña"
      /><br />
      <button type="submit">Login</button>
    </form>
  </div>
  <p>
    ¿Aún no tienes una cuenta MeowBook (=^･ｪ･^=)?
    <router-link to="/signin">Sign In</router-link>
  </p>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      nombre: "",
      contrasena: "",
    };
  },
  methods: {
    async login() {
      const url = "http://127.0.0.1:5000/";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          nombre: this.nombre,
          contrasena: this.contrasena,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.groupCollapsed("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      if (data["success"]) {
        this.$router.push({
          name: "Home",
        });
      }
    },
  },
};
</script>

<style scoped></style>
