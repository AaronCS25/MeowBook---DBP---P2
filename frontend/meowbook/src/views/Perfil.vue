<template>
  <div>
    <h1>Perfil de {{ this.usuario_nombre }}</h1>
    <ul style="border: 1px solid black">
      <li class="perfil">
        <h4>Datos:</h4>
        <ul class="conjunto-perfil">
          <li class="elemento-perfil">Nombre: {{ this.usuario_nombre }}</li>
          <li class="elemento-perfil">
            Apellidos: {{ this.usuario_apellido }}
          </li>
          <li class="elemento-perfil">
            Nacimiento: {{ this.usuario_nacimiento }}
          </li>
          <li class="elemento-perfil">Email: {{ this.usuario_email }}</li>
          <li class="elemento-perfil">Apodo: {{ this.usuario_apodo }}</li>
        </ul>
      </li>
    </ul>
    <p>{{ search }}</p>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    usuario_nombre: {
      type: String,
      required: false,
    },
    usuario_apellido: {
      type: String,
      required: false,
    },
    usuario_nacimiento: {
      type: String,
      required: false,
    },
    usuario_email: {
      type: String,
      required: false,
    },
    usuario_apodo: {
      type: String,
      required: false,
    },
    usuario_contrasena: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      search: "",
    };
  },
};
</script>

<style>
.perfil {
  display: flex;
  text-decoration: none;
}

.conjunto-perfil {
  padding: 2px;
  text-decoration: none;
  justify-content: left;
}

.elemento-perfil {
  padding: 2px;
  text-decoration: none;
  justify-content: left;
}
</style>
