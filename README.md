# Git leaks
## Archivos
- git_leaks.py: fichero de python que incluye un código que obtiene los commits del repositorio adjunto
- requirements.txt: fichero de texto con las librerías y sus correspondientes versiones necesarias para la ejecución del script de python
- repositorio: carpeta que contiene un repositorio clonado en el que se ejercerán las búsquedas de los commits.

## Descripción del script de python
Para el desarrollo de el código del script, hacemos uso de la función "Repo" de la librería de python "git". Para empezar cargamos el repositorio y después, mediante bucles se buscan todas las coincidencias en los commits con las palabras clave, que se encuentran en una lista. Si encuentra coincidencia, añade el commit a un diccionario, que será impreso por pantalla al terminarse de ejecutarse el programa
