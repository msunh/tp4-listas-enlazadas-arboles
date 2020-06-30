from tdaABB import *
from tdaListaEnlazada import *



# arbol1 = ABB([30,20,70,25,55,6,75])
# arbol1.treePlot()
# print(arbol1.buscar(80))



# arbol1 = ArbolBuscador(["juego","estado", "radio", "casa", "pato", "frio", "zorro", "balon", "nariz"])
# # #arbol1.insertar("pato")
# arbol1.treePlot()

# arbol1 = ArbolBuscador("juego", "play.com")
# arbol1 = ArbolBuscador("entrada", "ticketeck.com")

arbol1 = ArbolBuscador()
arbol1.insertar("juego", "juampy.com");

arbol1.insertar("estado", "carlitos.com");
#arbol1.insertar("estado", "marcos.com");
arbol1.insertar("radio", "cachito.com");
arbol1.treePlot()



