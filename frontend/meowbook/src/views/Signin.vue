<template>
  <div>
    <h1>Registrarse</h1>
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
    ¿Ya eres parte de la familia MeowBook (＾• ω •＾)?
    <router-link to="/">Log in</router-link>
  </p>
</template>
