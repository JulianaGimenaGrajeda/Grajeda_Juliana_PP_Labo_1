from biblioteca import * 

while True:
    opciones = validar_opciones()

    match opciones:
        case 1:
            print(leer_json("./data","json","data_servicios"))
        case 2:
            print(listar_datos(lista,["id_servicio",
                "descripcion",
                "tipo",
                "precioUnitario",
                "cantidad",
            "totalServicio"]))
        case 3:
            pass
        case 4:
            lista_coincidentes = hallar_coincidentes(lista,"tipo","2")
            guardar_archivo("./Nuevo_archivo.json",str(lista_coincidentes))
        case 5:
            lista_ordenada = ordenar_valores(lista,"descripcion")
            print(listar_datos(lista_ordenada,["id_servicio",
                "descripcion",
                "tipo",
                "precioUnitario",
                "cantidad",
            "totalServicio"]))
        case 6:
            lista = ordenar_valores(lista,"descripcion")
            guardar_archivo("Lista_ordenada.json",str(lista))
        case 7:
            break