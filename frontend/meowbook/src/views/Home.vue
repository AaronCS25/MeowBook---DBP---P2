<template>
  <html>
    <body>
      <form class="nav" id="searchForm">
        <input
          class="barra"
          type="text"
          maxlength="200"
          name="q"
          id="searchFieldx"
          value=""
          placeholder="Buscar por título o autor"
        />
        <input class="submit" type="submit" value="Buscar" />
      </form>
      <form class="options">
        <div class="option">
          <label for="editorial">Editorial:</label>
          <input
            class="option-input"
            type="text"
            id="editorial"
            name="editorial"
          />
        </div>
        <div class="option">
          <label for="año_publicacion">Año de Publicacion:</label>
          <select class="option-input" id="year" name="year">
            <option value="Accion" disabled selected>--Desde--</option>
            <option value="Accion">2000</option>
            <option value="Ficcion">1990</option>
            <option value="Drama">1980</option>
            <option value="Ficcion">1970</option>
            <option value="Drama">1960</option>
            <option value="Comedia">1950</option>
            <option value="Accion">1940</option>
            <option value="Ficcion">1930</option>
            <option value="Drama">1920</option>
            <option value="Comedia">1910</option>
            <option value="Accion">1900</option>
          </select>
        </div>
        <div class="option">
          <label for="nro_paginas">Número de Páginas:</label><br />
          <select class="option-input" id="min" name="min">
            <option value="Accion" disabled selected>--mín--</option>
            <option value="Accion">50</option>
            <option value="Ficcion">100</option>
            <option value="Drama">200</option>
            <option value="Ficcion">300</option>
            <option value="Drama">400</option>
            <option value="Comedia">500</option>
            <option value="Accion">600</option>
            <option value="Ficcion">650</option>
            <option value="Drama">700</option>
            <option value="Comedia">750</option>
            <option value="Accion">800</option>
          </select>
          <select class="option-input" id="max" name="max">
            <option value="Accion" disabled selected>--max--</option>
            <option value="Accion">100</option>
            <option value="Ficcion">200</option>
            <option value="Drama">300</option>
            <option value="Ficcion">400</option>
            <option value="Drama">500</option>
            <option value="Comedia">600</option>
            <option value="Accion">700</option>
            <option value="Ficcion">800</option>
            <option value="Drama">900</option>
            <option value="Comedia">>1000</option>
          </select>
        </div>
        <div class="option">
          <label for="genero">Género:</label>
          <select class="option-input" id="genero" name="genero">
            <option value="Accion" disabled selected>
              --Seleccione un género--
            </option>
            <option value="Accion">Acción</option>
            <option value="Comedia">Comedia</option>
            <option value="Drama">Drama</option>
            <option value="Ficcion">Ficción</option>
          </select>
        </div>
      </form>
    </body>
  </html>
</template>
