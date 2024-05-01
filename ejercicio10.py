class Cancion:
    def __init__(self, nombre, banda_artista, año_lanzamiento):
        self.nombre = nombre
        self.banda_artista = banda_artista
        self.año_lanzamiento = año_lanzamiento

canciones = [
    Cancion("Smells Like Teen Spirit", "Nirvana", 1991),
    Cancion("Under the Bridge", "Red Hot Chili Peppers", 1991),
    Cancion("Black Hole Sun", "Soundgarden", 1994),
    Cancion("Fake Tales of San Francisco", "Arctic Monkeys", 2006),
    Cancion("Cochise", "Audioslave", 2002),
    Cancion("Satisfaction", "The Rolling Stones", 1965),
    Cancion("Come as You Are", "Nirvana", 1991),
    Cancion("Californication", "Red Hot Chili Peppers", 1999),
    Cancion("Yellow Ledbetter", "Pearl Jam", 1992),
    Cancion("Heart-Shaped Box", "Nirvana", 1993)
]

def listar_canciones_ordenadas(canciones, criterio):
    if criterio == "cancion":
        return sorted(canciones, key=lambda x: x.nombre)
    elif criterio == "banda":
        return sorted(canciones, key=lambda x: x.banda_artista)
    elif criterio == "año":
        return sorted(canciones, key=lambda x: x.año_lanzamiento)

def buscar_cancion_por_banda(canciones, banda):
    return any(cancion.banda_artista == banda for cancion in canciones)

def canciones_por_banda(canciones, banda):
    return [cancion for cancion in canciones if cancion.banda_artista == banda]

def agregar_cancion(canciones, nombre, banda_artista, año_lanzamiento):
    nueva_cancion = Cancion(nombre, banda_artista, año_lanzamiento)
    canciones.append(nueva_cancion)
    return sorted(canciones, key=lambda x: x.nombre)

def contar_canciones_por_banda(canciones, banda):
    return sum(1 for cancion in canciones if cancion.banda_artista == banda)

def mostrar_info_cancion(canciones, nombre_cancion):
    for cancion in canciones:
        if cancion.nombre == nombre_cancion:
            return cancion
    return None

print("Canciones ordenadas por nombre:")
for cancion in listar_canciones_ordenadas(canciones, "cancion"):
    print(f"{cancion.nombre} - {cancion.banda_artista} - {cancion.año_lanzamiento}")

print("\nCanciones ordenadas por banda o artista:")
for cancion in listar_canciones_ordenadas(canciones, "banda"):
    print(f"{cancion.banda_artista} - {cancion.nombre} - {cancion.año_lanzamiento}")

print("\nCanciones ordenadas por año de lanzamiento:")
for cancion in listar_canciones_ordenadas(canciones, "año"):
    print(f"{cancion.año_lanzamiento} - {cancion.nombre} - {cancion.banda_artista}")

bandas_buscar = ["Audioslave", "The Rolling Stones"]
for banda in bandas_buscar:
    if buscar_cancion_por_banda(canciones, banda):
        print(f"\nHay canciones de {banda} en la lista.")
    else:
        print(f"\nNo hay canciones de {banda} en la lista.")

print("\nCanciones de Nirvana:")
for cancion in canciones_por_banda(canciones, "Nirvana"):
    print(f"{cancion.nombre} - {cancion.año_lanzamiento}")

canciones = agregar_cancion(canciones, "Purple Haze", "Jimi Hendrix", 1967)
print("\nCanciones ordenadas por nombre después de agregar 'Purple Haze':")
for cancion in canciones:
    print(cancion.nombre)

cantidad_rhcp = contar_canciones_por_banda(canciones, "Red Hot Chili Peppers")
print(f"\nCantidad de canciones de Red Hot Chili Peppers: {cantidad_rhcp}")

canciones_buscar = ["Fake tales of San Francisco", "Black Hole Sun"]
print("\nInformación de las canciones:")
for cancion_nombre in canciones_buscar:
    cancion_info = mostrar_info_cancion(canciones, cancion_nombre)
    if cancion_info:
        print(f"Nombre: {cancion_info.nombre}, Banda o Artista: {cancion_info.banda_artista}, Año de lanzamiento: {cancion_info.año_lanzamiento}")
    else:
        print(f"No se encontró información para la canción '{cancion_nombre}'.")