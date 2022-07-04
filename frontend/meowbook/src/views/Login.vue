<template>
  <html>
    <body>
      <form action="/login/succesful" class="login" method="POST">
        <h1>Iniciar Sesión</h1>
        <div class="container">
          <div class="input-container">
            <i class="fa-solid fa-envelope icon"></i>
            <input
              id="email"
              required
              name="email"
              type="email"
              placeholder="Email@"
            />
          </div>
          <div class="input-container">
            <i class="fa-solid fa-key icon"></i>
            <input
              id="contraseña"
              required
              name="contraseña"
              type="password"
              placeholder="Contraseña"
            />
          </div>

          <p>{{ data }}</p>
        </div>
        <input type="submit" value="Log In" class="button" />
        <p>
          ¿Aún no tienes una cuenta MeowBook (=^･ｪ･^=)?
          <router-link to="/signin">Sign In</router-link>
        </p>
      </form>
    </body>
  </html>
</template>
