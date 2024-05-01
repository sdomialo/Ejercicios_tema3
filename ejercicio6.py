class FunkoPop:
    def __init__(self, numero, nombre, coleccion, precio):
        self.numero = numero
        self.nombre = nombre
        self.coleccion = coleccion
        self.precio = precio

def ordenar_por_numero(funkos):
    return sorted(funkos, key=lambda x: x.numero)

def listar_por_coleccion(funkos, coleccion):
    return [funko for funko in funkos if funko.coleccion == coleccion]

def buscar_funko_por_numero_y_coleccion(funkos, numero, coleccion):
    for funko in funkos:
        if funko.numero == numero and funko.coleccion == coleccion:
            return funko
    return None

def mostrar_info_funko_por_numero(funkos, numero):
    for funko in funkos:
        if funko.numero == numero:
            print("Información del Funko Pop número", numero)
            print("Nombre:", funko.nombre)
            print("Colección:", funko.coleccion)
            print("Precio:", funko.precio)
            return
    print("No se encontró ningún Funko Pop con el número", numero)

def listar_modelos_por_nombre(funkos, nombre):
    return [funko for funko in funkos if nombre in funko.nombre]

def buscar_funkos_por_nombre(funkos, nombres):
    for nombre in nombres:
        encontrado = False
        for funko in funkos:
            if nombre.lower() in funko.nombre.lower():
                print("Se encontró el Funko Pop", nombre)
                print("Número:", funko.numero)
                print("Colección:", funko.coleccion)
                print("Precio:", funko.precio)
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún Funko Pop llamado", nombre)

def calcular_costo_tony_stark_iron_man(funkos):
    total_costo = 0
    for funko in funkos:
        if "Tony Stark" in funko.nombre or "Iron Man" in funko.nombre:
            total_costo += funko.precio
    return total_costo

def calcular_promedio_costo_y_costo_total(funkos):
    total_costo = sum(funko.precio for funko in funkos)
    promedio_costo = total_costo / len(funkos)
    
    costo_rocks = sum(funko.precio for funko in funkos if funko.coleccion == "Rocks")
    costo_harry_potter = sum(funko.precio for funko in funkos if funko.coleccion == "Harry Potter")
    
    return promedio_costo, costo_rocks, costo_harry_potter

funkos = [
    FunkoPop(130, "Funko Star Wars 1", "Star Wars", 10),
    FunkoPop(295, "Funko Star Wars 2", "Star Wars", 15),
    FunkoPop(295, "Funko Star Wars 3", "Star Wars", 20),
    FunkoPop(295, "Funko Marvel 1", "Marvel", 12),
    FunkoPop(295, "Funko Marvel 2", "Marvel", 18),
    FunkoPop(295, "Funko Rocks 1", "Rocks", 25),
    FunkoPop(295, "Funko Rocks 2", "Rocks", 30),
    FunkoPop(295, "Funko Harry Potter 1", "Harry Potter", 20),
    FunkoPop(295, "Funko Harry Potter 2", "Harry Potter", 25),
]

print("Funko Pop ordenados por número:")
for funko in ordenar_por_numero(funkos):
    print(f"Funko Pop {funko.numero}: {funko.nombre} - Colección: {funko.coleccion} - Precio: {funko.precio}")

coleccion = "Star Wars"
print(f"\nFunko Pop de la colección '{coleccion}':")
for funko in listar_por_coleccion(funkos, coleccion):
    print(f"Funko Pop {funko.numero}: {funko.nombre} - Precio: {funko.precio}")

numero_funko = 130
coleccion = "Star Wars"
print(f"\nInformación del Funko Pop {numero_funko} de la colección '{coleccion}':")
funko = buscar_funko_por_numero_y_coleccion(funkos, numero_funko, coleccion)
if funko:
    print(f"Funko Pop {funko.numero}: {funko.nombre} - Precio: {funko.precio}")
else:
    print(f"No se encontró el Funko Pop {numero_funko} en la colección '{coleccion}'")

numero_funko = 295
print(f"\nInformación de los Funko Pop número {numero_funko}:")
for funko in funkos:
    if funko.numero == numero_funko:
        print(f"Funko Pop {funko.numero}: {funko.nombre} - Colección: {funko.coleccion} - Precio: {funko.precio}")

nombres = ["Darth Vader", "Capitana Marvel"]
for nombre in nombres:
    print(f"\nModelos de {nombre}:")
    for funko in listar_modelos_por_nombre(funkos, nombre):
        print(f"Funko Pop {funko.numero}: {funko.nombre} - Colección: {funko.coleccion} - Precio: {funko.precio}")

nombres = ["Red Skull", "Thanos", "Galactus"]
buscar_funkos_por_nombre(funkos, nombres)

print("\nCosto total de todos los modelos de Tony Stark e Iron Man disponibles:")
print("Costo total:", calcular_costo_tony_stark_iron_man(funkos))

promedio_costo, costo_rocks, costo_harry_potter = calcular_promedio_costo_y_costo_total(funkos)
print("\nPromedio de costo de todos los Funko Pop:", promedio_costo)
print("Costo total de la colección 'Rocks':", costo_rocks)
print("Costo total de la colección 'Harry Potter':", costo_harry_potter)