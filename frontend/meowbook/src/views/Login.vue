<template>
  <div>
    <h1>MeowBookApp</h1>
    <form @submit.prevent="login">
      <input
        class="form-input"
        v-model="usuario_email"
        type="email"
        placeholder="Email"
      /><br />
      <input
        class="form-input"
        v-model="usuario_contrasena"
        type="password"
        placeholder="Contraseña"
      /><br />
      <p>
        ¿Aún no tienes una cuenta MeowBook (=^･ｪ･^=)?
        <router-link to="/signin">Sign In</router-link>
      </p>
      <button class="button" type="submit" id="submit">Iniciar sesión</button>
    </form>
  </div>
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
        sessionStorage.setItem("current_user", data["user_id"]);
        this.$router.push({
          name: "Perfil",
          params: {
            user_id: data["user_id"],
            usuario_nombre: data["usuario_nombre"],
            usuario_apellido: data["usuario_apellido"],
            usuario_nacimiento: data["usuario_nacimiento"],
            usuario_email: data["usuario_email"],
            usuario_apodo: data["usuario_apodo"],
            usuario_contrasena: data["usuario_contrasena"],
          },
        });
      }
      console.log("current_user: ", data["user_id"]);
    },
  },
};
</script>

<style scoped>
.form-input {
  width: 70%;
  height: 25px;
  padding: 8px 25px;
  margin: 12px;
  border-radius: 25px;
  border: none;
}

.form-input:focus {
  border: none;
  outline: none;
}
.button {
  font-weight: bold;
  font-size: 18px;
  padding: 8px;
  margin: 20px;
  border-radius: 25px;
  width: 70%;
  text-align: center;
  background: rgb(2, 0, 36);
  background: linear-gradient(
    90deg,
    rgba(2, 0, 36, 1) 0%,
    rgba(9, 9, 121, 1) 35%,
    rgba(0, 212, 255, 1) 100%
  );
  border: none;
  color: white;
}
</style>
