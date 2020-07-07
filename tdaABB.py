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

  def getListaWeb(self):
    return self.listaWeb      

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
    
    

  #grado del nodoArbol

  def grado(self):
    grado = 0
    if self.tieneIzquierdo():
      grado += 1
    if self.tieneDerecho():
      grado += 1
    return grado

  #altura del arbol en nodo

  def altura(self):
    altura = 0
    if self.grado() == 2:
      altura = 1 + max(self.izquierdo.altura() , self.derecho.altura())
    elif self.tieneIzquierdo():
      altura = 1 + self.izquierdo.altura()
    elif self.tieneDerecho():
      altura = 1 + self.derecho.altura()
    return altura

       

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


  def buscaPadre(self, dato): #parte de un nodo , buscando un dato y devuelve : me retorna 3 cosas , un puntero al padre, un puntero al nodo y de que lado del padre esta ese nodo
    nodoHijo = None              #se definnen los punteros de salida , con esta funcion buscamos el dato de los hijos
    nodoPadre = None
    lado = None
    if dato < self.dato:       #si el dato que busco es menor que el dato en donde estoy 
      if self.tieneIzquierdo(): #pregunto si el tiene izquierdo (si esta de este lado)
        if self.izquierdo.dato == dato: #y si coincide con el dato que viene por parametro y lo encuentro
          nodoHijo = self.izquierdo    #seteo mis punteros, el hijo es izquierdo
          nodoPadre = self              
          lado = "izq"                 #y lado es izquierdo 
        else:                         #tengo que llamar con el hijo izquierdo/nodo izquierdo
          nodoHijo, nodoPadre, lado = self.izquierdo.buscaPadre(dato) #llamo con el izquierdo
    else:                            # sino si es mayor, hay que ver el lado derecho 
      if self.tieneDerecho():       #si tiene derecho
        if self.derecho.dato == dato: # si lo encuentro del lado derecho
          nodoHijo = self.derecho   #seteo mis punteros
          nodoPadre = self
          lado = "der"              #y lado es igual derecho
        else:
          nodoHijo, nodoPadre, lado = self.derecho.buscaPadre(dato) #si no es el que yo quiero , lo mando a buscar al lado derecho
    return nodoHijo, nodoPadre, lado

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

  def palabrasDePagina(self, direccionWeb,listaDePalabras):

      if self.listaWeb.estaEnLista(direccionWeb):
        listaDePalabras.append(self.dato)

      if self.tieneDerecho():
        self.derecho.palabrasDePagina(direccionWeb, listaDePalabras)    

      if self.tieneIzquierdo():
        self.izquierdo.palabrasDePagina(direccionWeb, listaDePalabras)  



  def eliminarPalabra(self, dato):      #funcion eliminar del nodo
    nodoEliminar, nodoPadre, lado = self.buscaPadre(dato)  ##lado = "izq" / "der" - funcion que me "busca" y me retorna 3 cosas , un puntero al padre, un puntero al nodo y de que lado del padre esta ese nodo
    if nodoEliminar != None:            #si es distinto de none, si encontró el dato en el arbol
      if nodoEliminar.grado() == 2:                      #este es el caso si tiene dos hijos
        nodoPred = nodoEliminar.predecesor()             #primero buscamos al predecesor del nodo eliminar, ahi tengo un puntero al nodo que quiero eliminar
        self.eliminarPalabra(nodoPred.dato)                     #ahora elimino al predecesor con la misma funcion (elDatoQQueesta en elpredecesor) es el parametro
        nodoPred.izquierdo = nodoEliminar.izquierdo      #los hijos del nodo predecesor son los que eran los hijos del nodo a eliminar tanto izquierdo
        nodoPred.derecho = nodoEliminar.derecho          #como derecho
        if lado == "izq":                                #ahora tengo que poner al nodo predecesor como hijo del nodo padre dependiendo del lado, si es lado izq
          nodoPadre.izquierdo = nodoPred                 #el nodo predecesor es el hijo izquierdo del nodo padre
        else:                                            #si es lado derecho 
          nodoPadre.derecho = nodoPred                   #el nodo predecesor es hijo derecho del nodo padre 
      elif nodoEliminar.tieneIzquierdo():               # en este caso el hijo solo tiene izquierdo (tiene un solo hijo)
        if lado == "izq":                               #si el lado apunta al izquierdo, entonces el que quiero eliminar esta a la izquierda del padre
          nodoPadre.izquierdo = nodoEliminar.izquierdo  # entonces el izquierdo del padre tiene que apuntar al izquierdo del nodo eliminar
        else:                                           # en este caso solo tiene hijo derecho, (estamos eliminando un nodo que solo tiene izquierdo, pero esta del lado derecho del padre)
          nodoPadre.derecho = nodoEliminar.izquierdo    #entonces el derecho del padre = al derecho del hijo
      elif nodoEliminar.tieneDerecho():                 # en este caso el hijo solo tiene derecho (tiene un solo hijo)
        if lado == "izq":                               #si esta a la izquierda del padre 
          nodoPadre.izquierdo = nodoEliminar.derecho    #el que esta a la izquierdo del padre, va ser el derecho del hijo 
        else:                                           #si esta a la derecha del padre
          nodoPadre.derecho = nodoEliminar.derecho      #el derecho del padre , va ser el derecho del hijo
      else:                                             #este el caso que el nodo que quiero eliminar no tiene nigun hijo
        if lado == "izq":                               #si el lado es el izquierdo
          nodoPadre.izquierdo = None                    #pongo a none el hijo izquierdo
        else:
          nodoPadre.derecho = None                      #pongo a none el hijo derecho

  #eliminarPaginaNodo

  
  def eliminarPagina(self, direccionWeb, palabrasSinWeb):

      if self.listaWeb.estaEnLista(direccionWeb):  
        self.listaWeb.eliminar(self.listaWeb.posicionEnLista(direccionWeb))
        if self.listaWeb.estaVacia():
          palabrasSinWeb.append(self.dato)


      if self.tieneDerecho() :
         self.derecho.eliminarPagina(direccionWeb, palabrasSinWeb)

      if self.tieneIzquierdo() :
         self.izquierdo.eliminarPagina(direccionWeb, palabrasSinWeb)
    


  def cantidadTotalPalabras(self,cantidadLetras):
    contador = 0
    if self.cantidadLetrasDePalabra() >= cantidadLetras:
      contador+= 1
    
    if self.tieneDerecho():
      contador += self.derecho.cantidadTotalPalabras(cantidadLetras)
      
    if self.tieneIzquierdo():
      contador += self.izquierdo.cantidadTotalPalabras(cantidadLetras)
      
    return contador
  
  
  def cantidadLetrasDePalabra(self):
    return len(self.dato)
  

  #funcion de esta balanceado
  def estaBalanceado(self):
    alturaDerecho = 0
    alturaIzquierdo = 0
    

    if self.tieneDerecho():
      alturaDerecho = self.derecho.altura()

    if self.tieneIzquierdo():
      alturaIzquierdo = self.izquierdo.altura()  

    
    return alturaDerecho, alturaIzquierdo



  
  #nivel a lista de nodo
  def nivelALista(self, nivel, listaNivel, nivelNodo = 0):
    if nivelNodo == nivel:
      listaNivel.append(self.dato)
    else:
      if self.tieneDerecho():
        self.derecho.nivelALista(nivel, listaNivel, nivelNodo+1)
      if self.tieneIzquierdo():
        self.izquierdo.nivelALista(nivel, listaNivel, nivelNodo+1)



  def paginasEnNivel(self,nivel,listaNivelWeb, nivelNodo = 0):
    pos = 0
    if nivelNodo == nivel:
      if self.dato != None:
        while pos < self.listaWeb.len():
          listaNivelWeb.append(self.listaWeb.getDato(pos))
          pos +=1  
    else:
      if self.tieneDerecho():
        self.derecho.paginasEnNivel(nivel, listaNivelWeb, nivelNodo+1)
      if self.tieneIzquierdo():
        self.izquierdo.paginasEnNivel(nivel, listaNivelWeb, nivelNodo+1) 
  


  def cantidadPalabrasMasUsadas(self,cantidadPaginas):
    cantidadPalabras = 0
    
    if self.listaWeb.len() >= cantidadPaginas :
      cantidadPalabras +=1
      
    if self.tieneDerecho():
      cantidadPalabras += self.derecho.cantidadPalabrasMasUsadas(cantidadPaginas)
      
    if self.tieneIzquierdo():
      cantidadPalabras += self.izquierdo.cantidadPalabrasMasUsadas(cantidadPaginas)
    
    return cantidadPalabras
    
    
  # def internasMayusculaAlfabetico(self):
  #   listaPalabrasMayus = Lista()
    
  #   if self.tieneIzquierdo():
  #     self.izquierdo.internasMayusculaAlfabetico()
         
  #   if self.tieneMayuscula():
  #     listaPalabrasMayus.append(self.dato)

  #   if self.tieneDerecho():
  #     self.derecho.internasMayusculaAlfabetico()
    
  #   return listaPalabrasMayus
  
  
  def internasMayusculaAlfabetico(self,listaPalabras):
    listaPalabras = Lista()
    
    if not self.esHoja() and self.tieneMayuscula():
      listaPalabras.append(self.dato)
      print("hola")
      
    if self.tieneDerecho():
      listaPalabras = self.derecho.internasMayusculaAlfabetico(listaPalabras)
      
    if self.tieneIzquierdo():
      listaPalabras = self.izquierdo.internasMayusculaAlfabetico(listaPalabras)
      
    return listaPalabras
      
    
  def tieneMayuscula(self):
    return not self.dato.islower()
    
    

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










################################                         A R B O L


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

   

  #Recibe un elemento y retorna *True* si el elemento esta en el árbol y *False* en caso contrario.
  def buscar(self, dato):
    estaDato = False
    if not self.estaVacio():
      estaDato = self.raiz.buscar(dato) != None
    return estaDato
 
  #requerimientos

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
        listaWeb.unirListas(self.raiz.buscarPalabra(listaDePalabras.getDato(cont))) #llama al buscar palabra de nodo
        cont +=1

    listaWebClon = listaWeb.clonar()
    listaWeb.vaciarLista()
    pos = 0

    while pos < listaWebClon.len():
          
      if listaWebClon.cantWebRepetidasEnLista(listaWebClon.getDato(pos)) == listaDePalabras.len() and not listaWeb.estaEnLista(listaWebClon.getDato(pos)):
        listaWeb.append(listaWebClon.getDato(pos))
      pos +=1
      
      # while pos < listaWebClon.len():
          
      # if listaWebClon.cantWebRepetidasEnLista(listaWebClon.getDato(pos)) == listaDePalabras.len() and not listaWeb.estaEnLista(listaWebClon.getDato(pos)):
      #   listaWeb.append(listaWebClon.getDato(pos))
      # pos +=1

    return listaWeb 


  def palabrasDePagina(self,direccionWeb): #palabra de pagina de ARBOL
    listaDePalabras = Lista()    

    if not self.estaVacio():
      self.raiz.palabrasDePagina(direccionWeb, listaDePalabras)

    return listaDePalabras  


  def eliminarPalabra(self, dato): # viene por parametro el dato a borrar
    if not self.estaVacio():              # se valida que el arbol no esta vacio
      if dato == self.raiz.dato:          #primero se resuelven los casos particulares , si el elemento que quiero eliminar  esta en la raiz (dato == self.raiz.dato)
        if self.raiz.grado() == 2:        # si tiene grado 2, o sea que tiene dos hijos (izq y der)
          nodoPred = self.raiz.predecesor()         #primero buscamos el predecesor y lo guardamos en una variable aux la cual quedara apuntando al predecesor aún despues de que lo eliminé
          self.eliminarPalabra(nodoPred.dato)              #eliminamos el predecesor llamando a la funcion de eliminar y pasando el dato por parametro
          nodoPred.izquierdo = self.raiz.izquierdo  #entonces ahora apunto el izquierdo al que era el hijo izquierdo de la raiz, (donde apuntaba antes la raiz)
          nodoPred.derecho = self.raiz.derecho      #y tambien apunto el derecho al que era el hijo derecho de la raiz, (donde apuntaba antes la raiz)
          self.raiz = nodoPred                      # y por ultimo ahora mi raiz, pasa a ser el nodo predecesor
        elif self.raiz.tieneIzquierdo():  # tiene grado uno, y aqui solo tiene izquierdo o sea un solo hijo
          self.raiz = self.raiz.izquierdo # por lo tanto hay que reemplazar directamente al nodo por su hijo (en este caso izquierdo que es el unico que tiene), el nodo raiz apunta ahora a su hijo izquierdo y ya queda eliminado el que queriamos
        elif self.raiz.tieneDerecho():    # tiene grado uno, y aqui solo tiene derecho
          self.raiz = self.raiz.derecho   # se hace lo mismo que las lineas de arriba pero en este caso es reemplazado directamente por su hijo derecho, el nodo raiz apunta ahora a su hijo derecho
        else:                             #en este caso no tiene hijos, 
          self.raiz = None                #asi que ahora el nodo raiz apunta a None
      else:                 # Ahora se resuleve el caso en que el dato a borrar no este en la raiz, por eso entonces
        self.raiz.eliminarPalabra(dato) # si no es el dato de raiz, llamamos a la funcion eliminar del tipo nodo


  #eliminarPagina de arbol


  def eliminarPagina(self, direccionWeb):
    listaSinWeb = Lista()
    cont = 0

    if not self.estaVacio():
      self.raiz.eliminarPagina(direccionWeb, listaSinWeb) 

    
    while cont < listaSinWeb.len(): #elimina una palabra sin web
      self.eliminarPalabra(listaSinWeb.getDato(cont))
      cont +=1   
 

  #funcion aux
  def cantidadTotalPalabras(self,cantidadLetras):
    aux = 0
    if not self.estaVacio():
      aux = self.raiz.cantidadTotalPalabras(cantidadLetras)
      
    return aux


  #funcion Esta Balanceado de Arbol
  def estaBalanceado(self):
    balanceado = False
    derecho = 0
    izquierdo = 0 

    if not self.estaVacio():
      derecho, izquierdo = self.raiz.estaBalanceado()  

    if ((derecho - izquierdo) <= 1) and ((derecho - izquierdo) >= -1):
      balanceado = True

    return balanceado
  
  def nivelALista(self, nivel):
    listaNivel = []

    if not self.estaVacio():
      self.raiz.nivelALista(nivel, listaNivel)

    return listaNivel


  def paginasEnNivel(self, nivel):
    listaNivel = Lista()

    if not self.estaVacio():
      self.raiz.paginasEnNivel(nivel, listaNivel)

    listaNivelClonada = listaNivel.clonar()
    listaNivel.vaciarLista()
    pos = 0
    
    while pos < listaNivelClonada.len():
      if not listaNivel.estaEnLista(listaNivelClonada.getDato(pos)):
        listaNivel.append(listaNivelClonada.getDato(pos))
      pos +=1  


    return listaNivel 


  def cantidadPalabrasMasUsadas(self,cantidadPaginas):
    
    cantidadPalabras = 0
    
    if not self.estaVacio():
      cantidadPalabras = self.raiz.cantidadPalabrasMasUsadas(cantidadPaginas)
      
    return cantidadPalabras
  
    

  def internasMayusculaAlfabetico(self):
    listaPalabras = Lista()
    
    if not self.estaVacio():
      listaPalabras = self.raiz.internasMayusculaAlfabetico(listaPalabras)
    
    return listaPalabras





        
  

  #funcion para salida-graficar arbol
  def treePlot(self, fileName='representacionAbolEjemplo'):
    if not self.estaVacio():
      treeDot = Digraph()
      treeDot.node(str(self.raiz.dato), str(self.raiz.dato))
      self.raiz.treePlot(treeDot)
      treeDot.render(fileName, view=True)


      
