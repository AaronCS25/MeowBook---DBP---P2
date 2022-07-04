<template>
  <html>
    <body>
      <form
        id="registro"
        class="registro"
        action="/registro/succesful"
        method="POST"
      >
        <h1>Registrarse</h1>
        <div class="container">
          <div class="input-container">
            <i class="fa-solid fa-user icon"></i>
            <input
              id="nombre"
              name="nombre"
              type="text"
              placeholder="Nombre"
              required
            />
          </div>
          <div class="input-container">
            <i class="fa-solid fa-user icon-hidden"></i>
            <input
              id="apellido"
              name="apellido"
              type="text"
              placeholder="Apellido"
              required
            />
          </div>
          <div class="input-container">
            <i class="fa-solid fa-envelope icon"></i>
            <input
              id="email"
              name="email"
              type="email"
              placeholder="Email@"
              required
            />
          </div>
          <p>{{ data_1 }}</p>
          <div class="input-container">
            <i class="fa-solid fa-user-astronaut icon"></i>
            <input
              id="usuario"
              name="usuario"
              type="text"
              placeholder="usuario"
              required
            />
          </div>
          <p>{{ data_2 }}</p>
          <div class="input-container">
            <i class="fa-solid fa-key icon"></i>
            <input
              id="contraseña"
              name="contraseña"
              type="password"
              placeholder="Password"
              required
            />
          </div>
          <input type="submit" value="Sign in" class="button" />
          <p>
            ¿Ya eres parte de la familia MeowBook (＾• ω •＾)?
            <router-link to="/">Log in</router-link>
          </p>
        </div>
      </form>
    </body>
  </html>
</template>
