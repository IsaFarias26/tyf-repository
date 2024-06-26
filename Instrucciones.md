# Programacion-Web

Web teclas y fichas
Aca iran los comentarios

teclasYfichas es el proyecto_Django
TyF es la app

Para editar primero:

Activar el entorno virtual " MiEntorno\Scripts\activate"

Instalar Django " pip install django "

Instalar setuptools " pip install setuptools "

no olvides hacer las migraciones para guaradr los cambos en la bd en caso de hacerle
" python manage.py makemigrations "

luego...

" python manage.py migrate "
para subir los cambios a github:

primero activamos el git (previamente instalado en tu pc)
" git init "

" git status " esto te mostrara todos los cambios que haz hechoy obviamente guardado

en caso de aparecer muchas carpetas como no guardada o en el caso de la terminal de powershel en rojo agregarlos al git con " git add . " (el punto esta separado del add, esa formas es la correcta)

una vez procesados los cambios le hacemos el commit
{ git commit -m "escribe los cambios como texto" } lo que escribas dentro de las comillas aparecera en la carpeta de github en donde tengo el repositorio

por ultimo lo subes para que se actualice:
si quieres subir los cambios al repositorio principal es " git push origin main "

si quieres subir tus cambios a una nueva branch debes crear una nueva en github con el nombre que te parezca correcto y escribir " git push origin NombreDeLaBransh "
