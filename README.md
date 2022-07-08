## Proyecto - DBP - 1

- Proyecto desarrollado para el curso de desarrollo basado en plataformas.

## Nombre del proyecto:

- MeowBook

## Integrantes:

* Camacho Valencia, Aaron Arturo - 202020021
* Ruiz de Somocurcio Landa, Cristóbal - 202010386
* Integrante 3
* Integrante 4

## Descripción del proyecto:

   * MeowBook es una plataforma web de reseñas, en las que puedes hacer seguimiento a los libros. Existe un catálogo de estos y los usuarios pueden darle "like" a los libros que les gustan, para que los encuentren de forma más sencilla.

## Objetivos principales:

   * Permitir a los lectores hacer seguimiento de los libros que leen.
   * Permitir a los lectores compartir sus opiniones sobre los libros que les gustan.

## Mision:

Ayudar a los lectores ha poder organizar con facilidad los libros que están leyendo o que quieren leer en un futuro de manera amigable e intuitiva.

## Vision:

Crear una comunidad de lectores donde, de manera amigable, estos puedan interactuar  en base a las preferencias que puedan tener y compartirlas con los demás  usuarios.

## Frameworks & Librerias:

# 1. Front-end
    *  Se utilizó Bootstrap 5, JavaScript, Vue.js y Vue Client

# 2. Backend
    * Flask
    * Flask - SQLAlchemy
    * Flask - Migrate 
    * Flask - WTF

# 3. Base de datos
    * PostgreSQL v14.2

## Script a ejecutar para iniciar el proyecto con datos:
En el 'models.py', al configurar el app, se colocó la DATABASE_URI con el path hacia la base de datos local.

## API's information. Request & Responces (endpoints):

## Hosts:
Se utilizaron un localhost diferente para el backend y frontend
   * Para el frontend, donde estaba Vue, se utilizó el puerto 8081.
   * Para el backend, donde corre Flask, se usó el 5000.

## Forma de auntenticación:

## Error Handler:

## Cómo ejecutar el sistema (Deployment scripts):
# Backend
   * export FLASK_APP=server
   * export FLASK_ENV=development
   * run flask
# Frontend
   * yarn serve


