<template>
  <div>
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login">
      <input v-model="usuario_email" type="email" placeholder="Email" /><br />
      <input
        v-model="usuario_contrasena"
        type="password"
        placeholder="Contraseña"
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
      usuario_email: "",
      usuario_contrasena: "",
    };
  },
  methods: {
    async login() {
      const url = "http://127.0.0.1:5000/";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          usuario_email: this.usuario_email,
          usuario_contrasena: this.usuario_contrasena,
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
