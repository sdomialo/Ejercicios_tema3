personajes = [
    {"nombre": "Iron Man", "año_aparicion": 2008},
    {"nombre": "Hulk", "año_aparicion": 2008},
    {"nombre": "Thor", "año_aparicion": 2011},
    {"nombre": "Captain America", "año_aparicion": 2011},
    {"nombre": "Black Widow", "año_aparicion": 2010},
    {"nombre": "Hawkeye", "año_aparicion": 2011},
    {"nombre": "Black Panther", "año_aparicion": 2016},
    {"nombre": "Doctor Strange", "año_aparicion": 2016},
    {"nombre": "Spider-Man", "año_aparicion": 2016},
    {"nombre": "Ant-Man", "año_aparicion": 2015},
    {"nombre": "Captain Marvel", "año_aparicion": 2019},
    {"nombre": "Scarlet Witch", "año_aparicion": 2015},
    {"nombre": "Vision", "año_aparicion": 2015},
    {"nombre": "Falcon", "año_aparicion": 2014},
    {"nombre": "Winter Soldier", "año_aparicion": 2014},
    {"nombre": "War Machine", "año_aparicion": 2010},
    {"nombre": "Rocket Raccoon", "año_aparicion": 2014},
    {"nombre": "Groot", "año_aparicion": 2014},
    {"nombre": "Gamora", "año_aparicion": 2014},
    {"nombre": "Drax", "año_aparicion": 2014},
]

personajes_ordenados_nombre = sorted(personajes, key=lambda x: x["nombre"])
print("Listado ascendente de los personajes ordenados por su nombre:")
for personaje in personajes_ordenados_nombre:
    print(personaje["nombre"])

primer_personaje = min(personajes, key=lambda x: x["año_aparicion"])
ultimo_personaje = max(personajes, key=lambda x: x["año_aparicion"])
print("El primer personaje en aparecer en una película es:", primer_personaje["nombre"])
print("El último personaje en aparecer en una película es:", ultimo_personaje["nombre"])

personajes_ordenados_año = sorted(personajes, key=lambda x: x["año_aparicion"], reverse=True)
print("Listado de los personajes ordenados de manera descendente por año de aparición:")
for personaje in personajes_ordenados_año:
    print(personaje["nombre"])

rango_años = ultimo_personaje["año_aparicion"] - primer_personaje["año_aparicion"]
print("El rango de años entre el primer personaje en aparecer y el último es:", rango_años)

capitan_america = next((personaje for personaje in personajes if personaje["nombre"] == "Captain America"), None)
rocket_raccoon = next((personaje for personaje in personajes if personaje["nombre"] == "Rocket Raccoon"), None)

if capitan_america:
    print("Capitan America está en la lista y apareció en el año:", capitan_america["año_aparicion"])
else:
    print("Capitan America no está en la lista")

if rocket_raccoon:
    print("Rocket Raccoon está en la lista y apareció en el año:", rocket_raccoon["año_aparicion"])
else:
    print("Rocket Raccoon no está en la lista")