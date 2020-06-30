from graphviz import Digraph

###########################   N O D O 

class NodoArbol:
  
  def __init__(self, dato = None):
    self.dato = dato
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
    
    
  #insertar dato

  def insertar(self, nuevoNodo):
    if self.dato == nuevoNodo.dato:
      print("El elemento ya esta en el arbol")
    elif nuevoNodo.dato < self.dato:
      if self.tieneIzquierdo():
        self.izquierdo.insertar(nuevoNodo)
      else:
        self.izquierdo = nuevoNodo
    else:
      if self.tieneDerecho():
        self.derecho.insertar(nuevoNodo)
      else:
        self.derecho = nuevoNodo  

  #grado

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

  def buscaMaximo(self):
    dato = None
    if self.tieneDerecho():
      dato = self.derecho.buscaMaximo()
    else:
      dato = self

    return dato


  def predecesor(self):
    predecesor = None
    if self.tieneIzquierdo():
      predecesor = self.izquierdo.buscaMaximo()
    return predecesor   


  def sucesor(self):
    sucesor = None
    if self.tieneDerecho():
          sucesor = self.derecho.buscaMinimo()
    return sucesor



  #buscar dato

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


class ABB:
  def __init__(self, entrada = None):
    self.raiz = None
    if entrada:
        for elemento in entrada:
         self.insertar(elemento)

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

  #Inserta nuevo nodo en el lugar que corresponde en el árbol con el elemento que recibe como parámetro.
  def insertar(self, dato):
    nuevoNodo = NodoArbol(dato)
    if self.estaVacio():
      self.raiz = nuevoNodo
    else:
      self.raiz.insertar(nuevoNodo)

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




##***      
