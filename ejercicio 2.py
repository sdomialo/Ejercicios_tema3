def buscar_sable_de_luz(mochila):
    objetos_sacados = 0
    while mochila:
        objeto = mochila.pop(0)
        objetos_sacados += 1
        if objeto == "sable de luz":
            print("¡Encontré un sable de luz!")
            print(f"Se sacaron {objetos_sacados} objetos para encontrarlo")
            return objetos_sacados
        elif not mochila:
            print("No quedan más objetos en la mochila")
            return -1
        else:
            print("No es un sable de luz, seguir buscando")


    return -1

mochila = ["libro", "botella de agua", "linterna", "sable de luz", "bocadillo"]

buscar_sable_de_luz(mochila)