class Pokemon:
    def __init__(self, numero, nombre, tipo):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo

def ordenar_por_numero(pokemons):
    max_numero = max(pokemon.numero for pokemon in pokemons)
    conteo = [0] * (max_numero + 1)
    for pokemon in pokemons:
        conteo[pokemon.numero] += 1
    sorted_pokemons = []
    for numero, cantidad in enumerate(conteo):
        sorted_pokemons.extend([pokemon for pokemon in pokemons if pokemon.numero == numero] * cantidad)
    return sorted_pokemons

def ordenar_por_nombre(pokemons):
    if len(pokemons) <= 1:
        return pokemons
    pivote = pokemons[len(pokemons) // 2].nombre
    menores = [pokemon for pokemon in pokemons if pokemon.nombre < pivote]
    iguales = [pokemon for pokemon in pokemons if pokemon.nombre == pivote]
    mayores = [pokemon for pokemon in pokemons if pokemon.nombre > pivote]
    return ordenar_por_nombre(menores) + iguales + ordenar_por_nombre(mayores)

def mostrar_info_pokemon_numero(pokemons, numero):
    for pokemon in pokemons:
        if pokemon.numero == numero:
            print("Información del Pokémon número", numero)
            print("Nombre:", pokemon.nombre)
            print("Tipo:", pokemon.tipo)
            return
    print("No se encontró ningún Pokémon con el número", numero)

def listar_pokemons_con_letra(pokemons, letra):
    pokemons_con_letra = [pokemon for pokemon in pokemons if pokemon.nombre.startswith(letra)]
    return pokemons_con_letra

def buscar_pokemon(pokemons, nombre_pokemon):
    for pokemon in pokemons:
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            print("Se encontró el Pokémon", nombre_pokemon)
            print("Número:", pokemon.numero)
            print("Tipo:", pokemon.tipo)
            return
    print("No se encontró ningún Pokémon llamado", nombre_pokemon)

def listar_pokemons_tipo_electrico(pokemons):
    electricos = [pokemon for pokemon in pokemons if pokemon.tipo.lower() == "eléctrico"]
    cantidad_electricos = len(electricos)
    return electricos, cantidad_electricos

pokemons = [
    Pokemon(25, "Pikachu", "Eléctrico"),
    Pokemon(143, "Snorlax", "Normal"),
    Pokemon(385, "Jirachi", "Psíquico"),
    Pokemon(640, "Zekrom", "Eléctrico"),
    Pokemon(641, "Reshiram", "Fuego"),
    Pokemon(642, "Cobalion", "Acero"),
    Pokemon(702, "Dedenne", "Eléctrico"),
    Pokemon(736, "Grubbin", "Bicho"),
    Pokemon(789, "Cosmog", "Psíquico"),
    Pokemon(886, "Dracozolt", "Eléctrico")
]

print("Pokémons ordenados por número:")
for pokemon in ordenar_por_numero(pokemons):
    print(pokemon.numero, pokemon.nombre)

print("\nPokémons ordenados por nombre:")
for pokemon in ordenar_por_nombre(pokemons):
    print(pokemon.nombre)

print("\nInformación del Pokémon número 640:")
mostrar_info_pokemon_numero(pokemons, 640)

print("\nPokémons que comienzan con la letra T:")
for pokemon in listar_pokemons_con_letra(pokemons, "T"):
    print(pokemon.nombre)

print("\nInformación del Pokémon Cobalion:")
buscar_pokemon(pokemons, "Cobalion")

electricos, cantidad_electricos = listar_pokemons_tipo_electrico(pokemons)
print("\nPokémons de tipo eléctrico:")
for pokemon in electricos:
    print(pokemon.nombre)
print("Cantidad total de Pokémons de tipo eléctrico:", cantidad_electricos)