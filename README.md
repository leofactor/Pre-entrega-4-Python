# Sistema de blog modular y validado

Preentrega 4: programa de consola en Python para listar publicaciones, buscar por título, filtrar por etiqueta y validar los datos de cada post.

## Requisitos

Python 3 (no necesita bibliotecas adicionales).

## Ejecución

Desde una terminal, ubicarse en la carpeta que contiene `sistema_blog_funciones.py` y ejecutar:

```bash
python sistema_blog_funciones.py
```

Si el sistema usa el comando `python3`, ejecutar `python3 sistema_blog_funciones.py`.

## Uso

Elegir una opción del menú (1 a 5). La opción 4 muestra cuáles posts son válidos y cuál es incorrecto. El tercer post carece intencionalmente de `contenido` para comprobar la validación. El programa controla entradas no numéricas, opciones inexistentes y búsquedas vacías.

## Estructuras

`perfil_autor` es un diccionario anidado dentro de cada post; `estados_post` es una tupla; `etiquetas_blog` es un set; `posts` es una lista de diccionarios.
