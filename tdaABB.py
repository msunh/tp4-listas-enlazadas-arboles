from graphviz import Digraph
from tdaListaEnlazada import *

###########################   N O D O 

class NodoArbol:
  
  def __init__(self, dato = None, direccionWeb = None):
    self.listaWeb = Lista()
    self.dato = dato
    self.listaWeb.append(direccionWeb)
    self.izquierdo = None
    self.derecho = None

  def getDato(self):
    return self.dato  

  def esHoja(self):
    return not self.tieneDerecho() and not self.tieneIzquierdo()

  def tieneIzquierdo(self):
    return self.izquierdo != None

  def tieneDerecho(self):
    return self.derecho != None 


    #cantidad de hojas
  def cantHojas(self):

    cantHojas = 0

    if self.esHoja():
      cantHojas = 1

    if self.tieneIzquierdo():
      cantHojas += self.izquierdo.cantHojas()

    if self.tieneDerecho():
      cantHojas += self.derecho.cantHojas()

    return cantHojas  
    
    
  #insertar dato del nodoArbol

  def insertar(self, nuevoNodo , direccionWeb):
    if self.dato == nuevoNodo.dato:
      # print("La palabra ya se encuentra en el arbol")
      
      if not self.listaWeb.estaEnLista(direccionWeb):
        self.listaWeb.append(direccionWeb)

    elif nuevoNodo.dato < self.dato: 

      if self.tieneIzquierdo():
        self.izquierdo.insertar(nuevoNodo,direccionWeb)
      else:
        self.izquierdo = nuevoNodo

    else:
      if self.tieneDerecho():
        self.derecho.insertar(nuevoNodo,direccionWeb)
      else:
        self.derecho = nuevoNodo  

  
  #buscar palabra del nodoArbol
  def buscarPalabra(self,palabra):
      listaDePalabrasAux = Lista()
      
      if self.dato == palabra :
        listaDePalabrasAux = self.listaWeb
      elif self.dato > palabra:
        if self.tieneIzquierdo():
          listaDePalabrasAux = self.izquierdo.buscarPalabra(palabra)
      else:
        if self.tieneDerecho():
          listaDePalabrasAux = self.derecho.buscarPalabra(palabra)
          
      return listaDePalabrasAux

  #grado del nodoArbol

  def grado(self):
    grado = 0
    if self.tieneIzquierdo():
      grado += 1
    if self.tieneDerecho():
      grado += 1
    return grado

  #altura

  def altura(self):
    altura = 0
    if self.grado() == 2:
      altura = 1 + max(self.izquierdo.altura() , self.derecho.altura())
    elif self.tieneIzquierdo():
      altura = 1 + self.izquierdo.altura()
    elif self.tieneDerecho():
      altura = 1 + self.derecho.altura()
    return altura

  #nivel a lista
  def nivelALista(self, nivel, listaNivel, nivelNodo = 0):
    if nivelNodo == nivel:
      listaNivel.append(self.dato)
    else:
      if self.tieneDerecho():
        self.derecho.nivelALista(nivel, listaNivel, nivelNodo+1)
      if self.tieneIzquierdo():
        self.izquierdo.nivelALista(nivel, listaNivel, nivelNodo+1)

  #recorrido pre-orden
  def preOrden(self):
        
    print(self.dato)

    if self.tieneIzquierdo():
      self.izquierdo.preOrden()

    if self.tieneDerecho():
      self.derecho.preOrden()

  #recorrido in-orden (devuelve ordenado de menor a mayor)
  def inOrden(self):

    if self.tieneIzquierdo():
      self.izquierdo.inOrden()

    print(self.dato)

    if self.tieneDerecho():
      self.derecho.inOrden()
    
  #recorrido post orden
  def postOrden(self):

    if self.tieneIzquierdo():
      self.izquierdo.postOrden()
      
    if self.tieneDerecho():
      self.derecho.postOrden()

    print(self.dato)


  #busca minimo
  def buscaMinimo(self):
    dato = None
    if self.tieneIzquierdo():
      dato = self.izquierdo.buscaMinimo()
    else:
      dato = self

    return dato    

  #busca maximo
  def buscaMaximo(self):
    dato = None
    if self.tieneDerecho():
      dato = self.derecho.buscaMaximo()
    else:
      dato = self

    return dato

  #predecesor del Nodo
  def predecesor(self):
    predecesor = None
    if self.tieneIzquierdo():
      predecesor = self.izquierdo.buscaMaximo()
    return predecesor   

  #sucesor del Nodo
  def sucesor(self):
    sucesor = None
    if self.tieneDerecho():
          sucesor = self.derecho.buscaMinimo()
    return sucesor



  #buscar dato en el nodo retorna el dato

  def buscar(self, dato):
       
    nodoDato = None

    if self.dato == dato:
      nodoDato = self
    else:
      if dato < self.dato:
        if self.tieneIzquierdo():
          nodoDato = self.izquierdo.buscar(dato)
      else:
        if self.tieneDerecho():
          nodoDato = self.derecho.buscar(dato)

    return nodoDato


  def mostrarLista(self):
    print(self.listaWeb)



  #funcion para salida-graficar 
  def treePlot(self, dot):
      if self.tieneIzquierdo():
          dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
          dot.edge(str(self.dato), str(self.izquierdo.dato))
          self.izquierdo.treePlot(dot)
      else:
          dot.node("None"+str(self.dato)+"l", "None")
          dot.edge(str(self.dato), "None"+str(self.dato)+"l")
      if self.tieneDerecho():
          dot.node(str(self.derecho.dato), str(self.derecho.dato))
          dot.edge(str(self.dato), str(self.derecho.dato))
          self.derecho.treePlot(dot)
      else:
          dot.node("None"+str(self.dato)+"r", "None")
          dot.edge(str(self.dato), "None"+str(self.dato)+"r")


################################ A R B O L


class ArbolBuscador:
  def __init__(self):
    self.raiz = None
    
    
  def estaVacio(self):
    return self.raiz == None

  def preOrden(self):
    if not self.estaVacio():
      self.raiz.preOrden()
    else:
      print("Arbol vacio.")

  def inOrden(self):
    if not self.estaVacio():
      self.raiz.inOrden()
    else:
      print("Arbol vacio.")
      
  def postOrden(self):
    if not self.estaVacio():
      self.raiz.postOrden()
    else:
      print("Arbol vacio.")

 
  def insertarPalabra(self, dato, direccionWeb):
    nuevoNodo = NodoArbol(dato, direccionWeb)
    if self.estaVacio():
      self.raiz = nuevoNodo
    else:
        self.raiz.insertar(nuevoNodo,direccionWeb)

  #recibe por parametro una lista de palabras con una direccion web en comun
  def insertarPagina(self, listaDePalabras, direccionWeb):
    
    if not listaDePalabras.estaVacia():
      cont = 0
      while cont < listaDePalabras.len() :    
        self.insertarPalabra(listaDePalabras.getDato(cont), direccionWeb)
        cont += 1

  #recibe una lista de palabras y devuelve todas las paginas web  en donde estan
  def buscarPalabras(self,listaDePalabras):
    listaWeb = Lista()
    cont = 0

    if not listaDePalabras.estaVacia():
      while cont < listaDePalabras.len():
        listaWeb.unirListas(self.raiz.buscarPalabra(listaDePalabras.getDato(cont)))
        cont +=1

    listaWebClon = listaWeb.clonar()
    listaWeb.vaciarLista()
    pos = 0

    while pos < listaWebClon.len():
          
      if listaWebClon.cantWebRepetidasEnLista(listaWebClon.getDato(pos)) == listaDePalabras.len() and not listaWeb.estaEnLista(listaWebClon.getDato(pos)):
        listaWeb.append(listaWebClon.getDato(pos))
      pos +=1

    return listaWeb 
  
  

  def cantHojas(self):
    cant = 0 
    if not self.estaVacio():
      cant = self.raiz.cantHojas()
    return cant

  def minimo(self):
    minimo = None 
    if not self.estaVacio():
      minimo = self.raiz.buscaMinimo().dato
    return minimo

  def maximo(self):
    maximo = None 
    if not self.estaVacio():
          maximo = self.raiz.buscaMaximo().dato
    return maximo

  def profundidad(self):
    prof = 0
    if not self.estaVacio():
      prof = self.raiz.altura()
    return prof

  def nivelALista(self, nivel):
    listaNivel = []
    if not self.estaVacio():
      self.raiz.nivelALista(nivel, listaNivel)
    return listaNivel

  #Recibe un elemento y retorna *True* si el elemento esta en el árbol y *False* en caso contrario.
  def buscar(self, dato):
    estaDato = False
    if not self.estaVacio():
      estaDato = self.raiz.buscar(dato) != None
    return estaDato



  #funcion para salida-graficar arbol
  def treePlot(self, fileName='representacionAbolEjemplo'):
    if not self.estaVacio():
      treeDot = Digraph()
      treeDot.node(str(self.raiz.dato), str(self.raiz.dato))
      self.raiz.treePlot(treeDot)
      treeDot.render(fileName, view=True)


      
