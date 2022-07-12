<template>
  <div>
    <h1>Registrarse</h1>
    <form class="form1" @submit.prevent="signin">
      <input
        class="form-input"
        v-model="usuario.usuario_nombre"
        placeholder="Nombre"
      />
      <br />
      <input
        class="form-input"
        v-model="usuario.usuario_apellido"
        placeholder="Apellido"
      />
      <br />
      <input
        class="form-input"
        v-model="usuario.usuario_nacimiento"
        type="date"
        placeholder="Nacimiento"
      />
      <br />
      <input
        class="form-input"
        v-model="usuario.usuario_email"
        type="email"
        placeholder="Email"
      />
      <br />
      <input
        class="form-input"
        v-model="usuario.usuario_apodo"
        placeholder="Apodo"
      />
      <br />
      <input
        class="form-input"
        v-model="usuario.usuario_contrasena"
        type="password"
        placeholder="Contraseña"
      />
      <p>
        ¿Ya eres parte de la familia MeowBook (＾• ω •＾)?
        <router-link to="/">Log in</router-link>
      </p>
      <button class="button" type="submit">Registrarse</button>
    </form>
  </div>
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

<style scoped>
#form1 {
  width: 70%;
}
.form-input {
  width: 70%;
  height: 25px;
  padding: 8px 25px;
  margin: 10px;
  border-radius: 25px;
  border: none;
}
.form-input:focus {
  border: none;
  outline: none;
}
.button {
  padding: 8px;
  margin: 20px;
  border-radius: 25px;
  width: 70%;
  font-size: 18px;
  font-weight: bold;
  text-align: center;
  background: rgb(0, 212, 255);
  background: linear-gradient(
    141deg,
    rgba(0, 212, 255, 1) 0%,
    rgba(108, 95, 255, 1) 100%
  );
  border: none;
  color: white;
}
</style>
