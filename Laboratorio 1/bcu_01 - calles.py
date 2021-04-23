# Búsqueda Coste Uniforme - Uniform Cost Search
from Nodos import Nodo

def Comparar(nodo):
    return nodo.get_costo()

def busqueda_BCU(conecciones, estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(0)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijo (ciudades con conexion)
            datos_nodo = nodo_actual.get_estado()
            lista_hijos = []
            for achild in conecciones[datos_nodo]:
                hijo = Nodo(achild)
                costo = conecciones[datos_nodo][achild]
                hijo.set_costo(nodo_actual.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.equal(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    conecciones = {
                       'Max Toledo': {'Miguel de Rodas': 5, 'Bartolomé de las Casas': 10, 'Plaza Oruro': 25,
                                     'Linares': 15, 'Junín': 10, 'Arenales': 10, 'Av. Hernando Siles': 16, 'Junín': 9,
                                     'Av. Jaime Mendoza': 7, 'Av. Ostria Gutiérrez': 5,
                                     'Av. Marcelo Quiroga Santa Cruz': 15, 'Villa Margarita': 30},
                        'Villa Margarita': {'Av. Marcelo Quiroga Santa Cruz': 5, 'Av. Ostria Gutiérrez': 10,
                                          'Av. Germán Mendoza': 20, 'Aniceto Arce': 9, 'Arenales': 5, 'Loa': 10,
                                          'Colón': 15, 'Bustillos': 5, 'Orara': 10, 'Bartolomé de las Casas': 60,
                                          'Max Toledo': 20},
                        'Barrio Japón': {'Av. Toki': 6, 'Av. Martín Cárdenas': 7, 'Cornelio Duran': 8,
                                       'Idelfonso Murguía': 8, 'Av.Jaime Mendoza': 7, 'Plz. Huallpa Rimachi': 8,
                                       'Av.Jaime Mendoza': 7, 'Manuel Morales y Ugarte': 10, 'Calvo': 9, 'España': 7,
                                       'Vicente Camargo': 6, 'Av.Hernando Siles': 16, 'Loa': 10,
                                       'Regimeinto Charcas 16 de Infanteria': 10, 'Lemoine': 8, 'Av.German Mendoza': 9,
                                       'Germán Busch': 6, 'Sebastián García': 7, 'Plz.San Juanillo': 9, 'Marzana': 10,
                                       'Pando': 9, 'Eulogio Ostria Reyes': 7, 'Vicente Donoso': 10, 'Torres': 7,
                                       'Mataniel Aguirre': 6, 'Av. A. Ostria Gutiérrez': 8,
                                       'Inca Garcilazo de la Vega': 15, 'Dtto. 317': 8, 'Surinam': 8,
                                       'Av. Marcelo Quiroga Santa Cruz': 13, 'Villa Margarita': 30},
                        'Lajastambo': {'Av. Navarra': 10, 'Av. J. Azurduy de Padilla': 15, 'Houssay': 6, 'Av. del Maestro': 12,
                                     'Av. Venezuela': 7, 'Av. Hernando Siles': 6, 'Loa': 7, 'Reg. Charcas 16 de Infantería': 8,
                           'Lemoine': 9, 'Gregorio Reynolds': 10, 'Av. J. Mendoza': 5, 'Av. Germán Mendoza': 5,
                           'Claudio Peñaranda': 8, 'Ostria Reyes': 9, 'Vicente Donoso': 12, 'Guillermo Loayza': 15,
                          'Brasil': 16, 'Andreotti': 7, 'Emilio Hochmman': 10, 'Mercado Campesino': 30},
                        'Mercado Campesino': {'Emilio Hochmman': 5, 'Pza. San Juanillo': 8, 'Marzana': 9,'Av. G. Mendoza': 12, 'Av. J. Mendoza': 13, 'A. Arce': 14,
                                           'Av. Hernando Siles': 15, 'Av. Venezuela': 17, 'Av. del Maestro': 18,
                                           'Houssay': 7, 'Av. J. Azurduy de Padilla': 15, 'Av. Navarra': 17,
                                           'Lajastambo': 30},
                        'El Morro': {'Marcelo Q. Santa Cruz': 9, 'O. Gutiérrez': 12, 'Carabineros': 7,
                                                       'Dtto. 130': 10, 'Aniceto Arce': 9, 'Arenales': 10, 'Loa': 13,
                                                       'Ayacucho': 15, 'Estudiantes': 16, 'Argentina': 10,
                                                       'Bustillos': 10, 'El Tejar': 25},
                        'El Tejar': {'Bustillos': 10, 'Pérez': 12, 'Nicolás Ortiz': 14, 'Plaza 25 de Mayo': 30, 'España': 10,
                                           'A. Arce': 17, '29 de Sep.': 12, 'Nataniel Aguirre': 10, 'O. Gutiérrez': 12,
                                        'Marcelo Q. Santa Cruz': 15, 'El Morro': 15}
        }
    estado_inicial = 'El Tejar'
    solucion = 'Barrio Japón'
    nodo_solucion = busqueda_BCU(conecciones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_estado())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))
