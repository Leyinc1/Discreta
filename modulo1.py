from collections import defaultdict

class NodoArbolFP:
    def __init__(self, articulo, contador=1):
        self.articulo = articulo  # Artículo del nodo
        self.contador = contador  # Frecuencia del artículo en este nodo
        self.padre = None  # Nodo padre
        self.hijos = {}  # Hijos del nodo
        self.enlace = None  # Enlace a otro nodo con el mismo artículo

    def incrementar(self, contador):
        """Incrementa el contador del nodo."""
        self.contador += contador

class ArbolFP:
    def __init__(self):
        self.raiz = NodoArbolFP(None, contador=1)  # Nodo raíz vacío
        self.tabla_encabezado = defaultdict(list)  # Tabla de encabezados

    def insertar_transaccion(self, transaccion, contador=1):
        """Inserta una transacción en el árbol FP."""
        nodo_actual = self.raiz

        for articulo in transaccion:
            # Si el hijo existe, incrementa el contador
            if articulo in nodo_actual.hijos:
                nodo_actual.hijos[articulo].incrementar(contador)
            else:
                # Si no, crea un nuevo nodo
                nuevo_nodo = NodoArbolFP(articulo, contador)
                nuevo_nodo.padre = nodo_actual
                nodo_actual.hijos[articulo] = nuevo_nodo

                # Actualiza la tabla de encabezados
                self.tabla_encabezado[articulo].append(nuevo_nodo)

            # Moverse al siguiente nodo
            nodo_actual = nodo_actual.hijos[articulo]

    def mostrar(self, nodo=None, nivel=0):
        """Muestra el árbol FP."""
        if nodo is None:
            nodo = self.raiz
        print('  ' * nivel + str(nodo.articulo) + ' (' + str(nodo.contador) + ')')
        for hijo in nodo.hijos.values():
            self.mostrar(hijo, nivel + 1)

def construir_arbol_fp(transacciones, soporte_minimo):
    """Construye el árbol FP a partir de las transacciones."""
    # Primero, contar la frecuencia de cada artículo
    conteo_articulos = defaultdict(int)
    for transaccion in transacciones:
        for articulo in transaccion:
            conteo_articulos[articulo] += 1

    # Filtrar artículos que no cumplan con el soporte mínimo
    articulos_frecuentes = {articulo for articulo, contador in conteo_articulos.items() if contador >= soporte_minimo}

    if not articulos_frecuentes:
        return None, None

    # Ordenar los artículos de cada transacción por su frecuencia
    transacciones_ordenadas = []
    for transaccion in transacciones:
        transaccion_ordenada = [articulo for articulo in transaccion if articulo in articulos_frecuentes]
        transaccion_ordenada.sort(key=lambda x: conteo_articulos[x], reverse=True)
        if transaccion_ordenada:
            transacciones_ordenadas.append(transaccion_ordenada)

    # Construir el árbol FP
    arbol_fp = ArbolFP()
    for transaccion in transacciones_ordenadas:
        arbol_fp.insertar_transaccion(transaccion)

    return arbol_fp, conteo_articulos

def minar_arbol_fp(arbol_fp, soporte_minimo, prefijo, conjuntos_frecuentes):
    """Extrae patrones frecuentes del árbol FP."""
    # Ordenar ítems en la tabla de encabezados por frecuencia
    articulos_ordenados = sorted(arbol_fp.tabla_encabezado.items(), key=lambda x: sum(nodo.contador for nodo in x[1]))

    # Recorrer la tabla de encabezados en orden ascendente de frecuencia
    for articulo, nodos in articulos_ordenados:
        nuevo_prefijo = prefijo.copy()
        nuevo_prefijo.append(articulo)

        # Agregar el nuevo conjunto frecuente
        conjuntos_frecuentes.append((nuevo_prefijo, sum(nodo.contador for nodo in nodos)))

        # Construir el conjunto condicional
        base_patrones_condicionales = []
        for nodo in nodos:
            camino = []
            padre = nodo.padre
            while padre.articulo is not None:
                camino.append(padre.articulo)
                padre = padre.padre
            camino.reverse()
            if camino:
                base_patrones_condicionales.append((camino, nodo.contador))

        # Crear el árbol FP condicional
        arbol_condicional, _ = construir_arbol_fp([patron for patron, contador in base_patrones_condicionales],
                                                  soporte_minimo)

        if arbol_condicional is not None:
            minar_arbol_fp(arbol_condicional, soporte_minimo, nuevo_prefijo, conjuntos_frecuentes)

def crecimiento_fp(transacciones, soporte_minimo):
    """Algoritmo FP-Growth principal."""
    arbol_fp, conteo_articulos = construir_arbol_fp(transacciones, soporte_minimo)

    if arbol_fp is None:
        return []

    conjuntos_frecuentes = []
    minar_arbol_fp(arbol_fp, soporte_minimo, [], conjuntos_frecuentes)

    return conjuntos_frecuentes
