from tdaABB import *
from tdaListaEnlazada import *



# arbol1 = ABB([30,20,70,25,55,6,75])
# arbol1.treePlot()
# print(arbol1.buscar(80))



# arbol1 = ArbolBuscador(["juego","estado", "radio", "casa", "pato", "frio", "zorro", "balon", "nariz"])
# # #arbol1.insertarPalabra("pato")
# arbol1.treePlot()

# arbol1 = ArbolBuscador("juego", "play.com")
# arbol1 = ArbolBuscador("entrada", "ticketeck.com")

arbol1 = ArbolBuscador()
arbol1.insertarPalabra("juego", "juampy.com")
arbol1.insertarPalabra("juego", "juan.com")
arbol1.insertarPalabra("juego", "juan.com")
arbol1.insertarPalabra("estado", "carlitos.com")
arbol1.insertarPalabra("estado", "marcos.com")
arbol1.insertarPalabra("radio", "cachito.com")
arbol1.insertarPalabra("arbolito", "plantas.com")
arbol1.insertarPalabra("avioncito", "despegar.com")

#arbol1.treePlot()
#arbol1.raiz.mostrarLista()

#creo mi lista de palabras para pasar por parametro a la funcion insertar pagina
listaDePalabras = Lista()
listaDePalabras.append("perro")
listaDePalabras.append("juego")
#listaDePalabras.append("radio")
listaDePalabras.append("rodado")
listaDePalabras.append("arbolito")

listaDePalabras2 = Lista()
listaDePalabras2.append("juego")
#listaDePalabras2.append("estado")

arbol1.insertarPagina(listaDePalabras, "cualquiera.com")

arbol1.treePlot()
#print(arbol1.buscarPalabras(listaDePalabras))
#print(arbol1.buscarPalabras(listaDePalabras2))
print()
#eliminar palabra
#arbol1.eliminarPalabra("radio")
#arbol1.treePlot("eliminado")

#print(arbol1.raiz.getListaWeb())

#palabrasDePagina
#print(arbol1.palabrasDePagina("cualquiera.com"))

#eliminarWeb
arbol1.eliminarPagina("cachito.com")
arbol1.treePlot("eliminado")




