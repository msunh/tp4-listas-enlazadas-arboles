from tdaABB import *
from tdaListaEnlazada import *




arbol1 = ArbolBuscador()
arbol1.insertarPalabra("juego", "juampy.com")
arbol1.insertarPalabra("juego", "juan.com")
arbol1.insertarPalabra("juego", "juan.com")
arbol1.insertarPalabra("Piloto", "despegar.com")
arbol1.insertarPalabra("estado", "carlitos.com")
arbol1.insertarPalabra("estado", "marcos.com")
arbol1.insertarPalabra("radio", "cachito.com")
arbol1.insertarPalabra("Futbol","espn.com")
arbol1.insertarPalabra("arbolito", "plantas.com")
arbol1.insertarPalabra("avioncito", "despegar.com")
arbol1.insertarPalabra("avioncito", "jorge.com")
arbol1.insertarPalabra("libro", "libreria.com")
arbol1.insertarPalabra("libro", "yenny.com")
arbol1.insertarPalabra("libro", "elatril.com")
arbol1.insertarPalabra("libro", "unahurlibros.com")
arbol1.insertarPalabra("ella", "cosmeticos.com")
arbol1.insertarPalabra("otorrinolaringolo", "garganta.com")


#creo mi lista de palabras para pasar por parametro a la funcion insertar pagina
listaDePalabras = Lista()
listaDePalabras.append("perro")
listaDePalabras.append("juego")
listaDePalabras.append("radio")
listaDePalabras.append("rodado")
listaDePalabras.append("arbolito")
listaDePalabras.append("mar")
listaDePalabras.append("tu")
listaDePalabras.append("Ataud")

listaDePalabras2 = Lista()
listaDePalabras2.append("juego")
listaDePalabras2.append("estado")

#insertar pagina (lista de palabras, una pagina web)
arbol1.insertarPagina(listaDePalabras, "cualquiera.com")

# arbol1.treePlot("arbolInicial")
print()

#buscar palabras (lista de palabras)
print("buscar palabras (lista de palabras): ", arbol1.buscarPalabras(listaDePalabras))

#palabrasDePagina
print("palabrasDePagina: ", arbol1.palabrasDePagina("cualquiera.com"))

print()

#eliminar palabra
#arbol1.eliminarPalabra("radio")
#arbol1.treePlot("eliminado")

#eliminar pagina (si web que eliminamos tiene una sola palabra, tambien la elimina) probar con lo del profe
arbol1.eliminarPagina("cualquiera.com")
arbol1.treePlot("eliminadoCualquiera")

print("cantidad total de palabras: ", arbol1.cantidadTotalPalabras(1))
print()

print("el arbol esta balanceado?: ", arbol1.estaBalanceado())
print()

print("paginas en nivel del arbol:", arbol1.paginasEnNivel(3))
print()

print("cantidad de palabras mas usadas:", arbol1.cantidadPalabrasMasUsadas(4))
print()

print("lista internas mayusculas en orden alfabetico: ", arbol1.internasMayusculaAlfabetico())







