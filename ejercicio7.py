dioses_griegos = ["Zeus", "Hera", "Poseidón", "Deméter", "Atenea", "Apolo", "Artemisa", "Ares", "Afrodita", "Hermes", "Hefesto", "Hestia", "Hades", "Dionisio"]

def listar_dioses_ordenados(dioses):
    return sorted(dioses)

def buscar_atenea(dioses):
    return "Atenea" in dioses

def posicion_demeter(dioses):
    return dioses.index("Deméter") + 1

def listar_dioses_con_letra(dioses, letra):
    dioses_con_letra = [dios for dios in dioses if dios.startswith(letra)]
    return dioses_con_letra, len(dioses_con_letra)

def agregar_helios(dioses):
    dioses.append("Helios")
    return sorted(dioses)

print("Dioses griegos ordenados:")
print(listar_dioses_ordenados(dioses_griegos))

print("\n¿Atenea está en la lista de dioses?")
print("Sí" if buscar_atenea(dioses_griegos) else "No")

print("\nPosición de Deméter:", posicion_demeter(dioses_griegos))

dioses_con_h, cantidad_h = listar_dioses_con_letra(dioses_griegos, "H")
print("\nDioses que comienzan con la letra H:")
print(dioses_con_h)
print("Cantidad:", cantidad_h)

print("\nAgregar a Helios y volver a listar los dioses:")
dioses_griegos_con_helios = agregar_helios(dioses_griegos)
print(dioses_griegos_con_helios)