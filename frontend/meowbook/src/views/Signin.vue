<template>
  <div>
    <h1>Registrarse</h1>
    <form @submit.prevent="signin">
      <input v-model="usuario.usuario_nombre" placeholder="Nombre" /> <br />
      <input v-model="usuario.usuario_apellido" placeholder="Apellido" /> <br />
      <input
        v-model="usuario.usuario_nacimiento"
        type="date"
        placeholder="Nacimiento"
      />
      <br />
      <input v-model="usuario.usuario_email" type="email" placeholder="Email" />
      <br />
      <input v-model="usuario.usuario_apodo" placeholder="Apodo" /> <br />
      <input
        v-model="usuario.usuario_contrasena"
        type="password"
        placeholder="Contraseña"
      />
      <br />
      <button type="submit">Signin</button>
    </form>
  </div>
  <p>
    ¿Ya eres parte de la familia MeowBook (＾• ω •＾)?
    <router-link to="/">Log in</router-link>
  </p>
</template>

<script>
export default {
  name: "Signin",
  data() {
    return {
      usuario: {
        usuario_nombre: "",
        usuario_apellido: "",
        usuario_nacimiento: "",
        usuario_email: "",
        usuario_apodo: "",
        usuario_contrasena: "",
      },
    };
  },
  methods: {
    async signin() {
      const URL = "http://127.0.0.1:5000/usuarios";
      const response = await fetch(URL, {
        method: "POST",
        body: JSON.stringify({
          usuario_nombre: this.usuario.usuario_nombre,
          usuario_apellido: this.usuario.usuario_apellido,
          usuario_nacimiento: this.usuario.usuario_nacimiento,
          usuario_email: this.usuario.usuario_email,
          usuario_apodo: this.usuario.usuario_apodo,
          usuario_contrasena: this.usuario.usuario_contrasena,
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
