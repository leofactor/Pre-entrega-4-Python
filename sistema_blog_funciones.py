# Preentrega 4 - Sistema de blog modular y validado
# Conserva las estructuras del modulo 2 y agrega funciones y validaciones.

perfil_autor = {"nombre": "Leonardo", "email": "autor@ejemplo.com"}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"python", "programacion", "blog"}

posts = [
    {"id": 1, "titulo": "Mi primer post en Python", "contenido": "Mi primer contenido.",
     "autor": perfil_autor, "tags": ["python", "blog"], "estado": "publicado"},
    {"id": 2, "titulo": "Aprendiendo funciones", "contenido": "Organizar codigo en funciones.",
     "autor": perfil_autor, "tags": ["python", "programacion"], "estado": "borrador"},
    {"id": 3, "titulo": "Post incompleto", "autor": perfil_autor,
     "tags": ["blog"], "estado": "publicado"}  # Falta 'contenido' intencionalmente.
]


def mostrar_menu():
    """Muestra el menu y devuelve un numero, o 0 si la entrada no es numerica."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        return int(input("Elegí una opcion: "))
    except ValueError:
        print("Error: debes ingresar un numero.")
        return 0


def error_post(post):
    """Devuelve el motivo de error, o None cuando el post es valido."""
    if not isinstance(post, dict):
        return "el post no es un diccionario"
    for clave in ("id", "titulo", "contenido", "autor", "tags", "estado"):
        if clave not in post:
            return f'falta la clave "{clave}"'
    if not isinstance(post["id"], int) or isinstance(post["id"], bool):
        return "id debe ser un entero"
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return "titulo vacio o incorrecto"
    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return "contenido vacio o incorrecto"
    if not isinstance(post["autor"], dict):
        return "autor debe ser un diccionario"
    if "nombre" not in post["autor"]:
        return 'falta la clave "nombre" en autor'
    if not isinstance(post["autor"]["nombre"], str) or not post["autor"]["nombre"].strip():
        return "nombre del autor vacio o incorrecto"
    if not isinstance(post["tags"], list):
        return "tags debe ser una lista"
    if not all(isinstance(tag, str) for tag in post["tags"]):
        return "los tags deben ser textos"
    if not isinstance(post["estado"], str) or post["estado"] not in estados_post:
        return "estado no permitido"
    return None


def validar_post(post):
    """Retorna True si cumple todas las reglas; False en caso contrario."""
    return error_post(post) is None


def listar_posts(lista):
    """Muestra el titulo y el nombre del autor de cada post valido."""
    if not lista:
        print("No hay publicaciones.")
        return
    for numero, post in enumerate(lista, start=1):
        if validar_post(post):
            print(f'Post {numero}: {post["titulo"]} - Autor: {post["autor"]["nombre"]}')
        else:
            print(f"Post {numero}: error - {error_post(post)}")


def buscar_por_titulo(lista, termino):
    """Busca un termino en los titulos, sin distinguir mayusculas."""
    termino = termino.strip().lower()
    if not termino:
        print("Error: la busqueda por titulo no puede estar vacia.")
        return
    encontrados = 0
    for post in lista:
        if validar_post(post) and termino in post["titulo"].lower():
            print(f'Titulo: {post["titulo"]} - Autor: {post["autor"]["nombre"]}')
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron publicaciones con ese titulo.")


def filtrar_por_tag(lista, tag):
    """Muestra posts que tienen el tag, sin distinguir mayusculas."""
    tag = tag.strip().lower()
    if not tag:
        print("Error: el tag no puede estar vacio.")
        return
    encontrados = 0
    for post in lista:
        if validar_post(post) and any(etiqueta.lower() == tag for etiqueta in post["tags"]):
            print(f'Titulo: {post["titulo"]} - Autor: {post["autor"]["nombre"]}')
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron publicaciones con ese tag.")


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            buscar_por_titulo(posts, input("Ingrese el titulo a buscar: "))
        elif opcion == 3:
            filtrar_por_tag(posts, input("Ingrese el tag a filtrar: "))
        elif opcion == 4:
            for numero, post in enumerate(posts, start=1):
                if validar_post(post):
                    print(f"Post {numero}: valido")
                else:
                    print(f"Post {numero}: error - {error_post(post)}")
        elif opcion == 5:
            print("Gracias por utilizar el blog. ¡Hasta luego!")
            break
        else:
            print("Opcion inexistente. Elegi un numero del 1 al 5.")
