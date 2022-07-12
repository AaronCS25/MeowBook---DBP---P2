<template>
  <div>
    <h1>Home</h1>
    <form @submit.prevent="buscar">
      <input type="text" v-model="search" />
      <button type="submit" id="submit">buscar</button>
    </form>
    <div v-for="dato in lists" :key="dato.libro_id">
      <ul style="border: 1px solid black">
        <li class="libro">
          <h4>{{ dato.libro_titulo }}</h4>
          <ul class="conjunto-libros">
            <p>ISBN:</p>
            <li>{{ dato.libro_isbn }}</li>
            <input type="checkbox" id="like_libro" @click="clickear" />
            <label for="like_libro">Like</label>
            <h1>{{ like_boolean ? "si" : "no" }}</h1>
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
      search: "",
      like_boolean: false,
    };
  },
  methods: {
    async buscar() {
      const url = "http://127.0.0.1:5000/libros";
      const response = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
          search: this.search,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      console.log("search: ", this.search);
      console.groupCollapsed("response: ", response);
      const data = await response.json();
      console.log("data: ", data);
      this.lists = data.libros;
    },
    async clickear() {
      this.like_boolean = !this.like_boolean;
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

<style>
.content {
  position: relative;
  width: 80%;
  margin: 0 auto;
}
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
.barra {
  z-index: 1;
  width: 80%;
  height: 100%;
  font-size: 0.9em;
  padding: 2px 15px;
  border: grey solid 1px;
  border-radius: 10px;
}
.barra:focus {
  outline: none;
  border: none;
}
#submit {
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  height: 100%;
  width: 18%;
  border-radius: 48px;
  margin: 5px;
  width: 83%;
  background: rgb(0, 212, 255);
  background: linear-gradient(
    141deg,
    rgba(0, 212, 255, 1) 0%,
    rgba(108, 95, 255, 1) 100%
  );
  border: none;
  color: aliceblue;
  border-radius: 10px;
}
.libros-container {
  margin-top: 20px;
  position: relative;
}
.libro-container {
  margin: 0;
  box-sizing: border-box;
}
</style>
