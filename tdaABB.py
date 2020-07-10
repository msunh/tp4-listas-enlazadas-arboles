from graphviz import Digraph
from tdaListaEnlazada import *

######################################################   N O D O    A R B O L  

class NodoArbol:
  
  def __init__(self, dato = None, direccionWeb = None):
    self.listaWeb = Lista()
    self.dato = dato
    self.listaWeb.append(direccionWeb)
    self.izquierdo = None
    self.derecho = None

  def getDato(self): #retorna el dato (nuestra clave) del nodo 
    return self.dato  

  def esHoja(self): # si no tiene puntero al derecho ni al izquierdo es hoja (ambos apuntan a None)
    return not self.tieneDerecho() and not self.tieneIzquierdo()

  def tieneIzquierdo(self): #True si es distinto de None
    return self.izquierdo != None

  def tieneDerecho(self): #True si es distinto de None
    return self.derecho != None 

  def getListaWeb(self): #función de prueba para obtener la lista de las páginas ingresadas del nodo raiz
    return self.listaWeb      


  #grado (NODO) -> cantidad de hijos que tiene un nodo, si no tiene ningún hijo es una hoja
  def grado(self):  
    grado = 0
    if self.tieneIzquierdo():
      grado += 1
    if self.tieneDerecho():
      grado += 1
    return grado

  #altura (NODO) -> largo de la trayectoria desde un nodo a la hoja más lejana 
  def altura(self):
    altura = 0
    if self.grado() == 2:
      altura = 1 + max(self.izquierdo.altura() , self.derecho.altura())
    elif self.tieneIzquierdo():
      altura = 1 + self.izquierdo.altura()
    elif self.tieneDerecho():
      altura = 1 + self.derecho.altura()
    return altura


  #busca mínimo (NODO) -> busca el mínimo (el primer nodo sin hijo izquierdo) y retorna el dato
  def buscaMinimo(self):
    dato = None
    if self.tieneIzquierdo(): # si tiene izquierdo, guarda el dato y llama recursivamente a la misma función
      dato = self.izquierdo.buscaMinimo()
    else:
      dato = self   #si no tiene izquierdo , es el mínimo

    return dato    

  #busca máximo (NODO) -> busca el máximo (primer nodo sin hijo derecho) y retorna el dato
  def buscaMaximo(self):
    dato = None
    if self.tieneDerecho(): # si tiene derecho, guarda el dato y llama recursivamente a la misma función
      dato = self.derecho.buscaMaximo()
    else:
      dato = self #si no tiene derecho, es el máximo

    return dato

  #predecesor (NODO) -> máximo del sub arbol izquierdo (el más grande dentro de los mas pequeños)
  def predecesor(self): 
    predecesor = None
    if self.tieneIzquierdo(): # se mueve al lado izquierdo del árbol
      predecesor = self.izquierdo.buscaMaximo() #busca el máximo y lo guarda en la variable, ese es el predecesor
    return predecesor   

  #sucesor (NODO) -> el mínimo del sub arbol izquierdo (el más pequeño dentro de los más grandes que él)
  def sucesor(self):
    sucesor = None
    if self.tieneDerecho(): #se mueve al lado derecho del arbol
          sucesor = self.derecho.buscaMinimo() #y busca el mínimo, lo guarda en la variable, ese el sucesor
    return sucesor



  #buscar dato (NODO) -> retorna el dato dentro del nodo

  def buscar(self, dato):
       
    nodoDato = None

    if self.dato == dato: #si el dato es igual al que viene por parámetro, el dato fue encontrado y se guarda en la variable
      nodoDato = self
    else:
      if dato < self.dato:                        #si no, si el dato buscado es menor que el dato en el nodo
        if self.tieneIzquierdo():                 #y si tiene hijo izquierdo
          nodoDato = self.izquierdo.buscar(dato)  #busca recursivamente  hacia izquierda, si lo encuentra lo guarda en la variable
      else:
        if self.tieneDerecho():                   #si tiene hijo derecho        
          nodoDato = self.derecho.buscar(dato)    #busca recursivamente hacia la derecha, si lo encuentra lo guarda en la variable

    return nodoDato 

  #buscar padre (NODO)
  def buscaPadre(self, dato):                     #parte de un nodo , buscando un dato y devuelve : me retorna 3 cosas , un puntero al padre, un puntero al nodo y de que lado del padre esta ese nodo
    nodoHijo = None                               #se definen los punteros de salida , con esta funcion buscamos el dato de los hijos
    nodoPadre = None
    lado = None
    if dato < self.dato:                          #si el dato que busco es menor que el dato en donde estoy 
      if self.tieneIzquierdo():                   #pregunto si el tiene izquierdo (si esta de este lado)
        if self.izquierdo.dato == dato:           #y si coincide con el dato que viene por parametro y lo encuentro
          nodoHijo = self.izquierdo               #seteo mis punteros, el hijo es izquierdo
          nodoPadre = self              
          lado = "izq"                            #y lado es izquierdo 
        else:                                     #tengo que llamar con el hijo izquierdo/nodo izquierdo
          nodoHijo, nodoPadre, lado = self.izquierdo.buscaPadre(dato) #llamo con el izquierdo
    else:                                         # si no, si es mayor, hay que ver el lado derecho 
      if self.tieneDerecho():                     #si tiene derecho
        if self.derecho.dato == dato:             # si lo encuentro del lado derecho
          nodoHijo = self.derecho                 #seteo mis punteros
          nodoPadre = self
          lado = "der"                            #y lado es igual derecho
        else:
          nodoHijo, nodoPadre, lado = self.derecho.buscaPadre(dato) #si no es el que yo quiero , lo mando a buscar al lado derecho
    return nodoHijo, nodoPadre, lado




  #insertar dato (NODO) -> inserta el nuevo dato y la direccion web que viene por parametro

  def insertar(self, nuevoNodo , direccionWeb):
    if self.dato == nuevoNodo.dato:                      # si el dato ingresado, (palabra) es igual al nodo en donde estoy,  solo ingreso la página web         
      if not self.listaWeb.estaEnLista(direccionWeb):    #y si la página web que viene por parametro no esta en la lista
        self.listaWeb.append(direccionWeb)               # la agrego a la lista de páginas de ese nodo/dato
    elif nuevoNodo.dato < self.dato:                     #si no si el dato del nuevo nodo es menor que el dato en donde estoy (el dato no está)
      if self.tieneIzquierdo():                          # y si tiene izquierdo
        self.izquierdo.insertar(nuevoNodo,direccionWeb)  #inserto en nuevo nodo y la dirección web el la lista (llamada recursiva)
      else:                                              #si no tiene izquierdo 
        self.izquierdo = nuevoNodo                       #el izquierdo es el nuevo nodo
    else:
      if self.tieneDerecho():                            #si tiene derecho     
        self.derecho.insertar(nuevoNodo,direccionWeb)    #inserto el dato en el derecho y la web en la lista (llamada recursiva)
      else:                                              #si no tiene derecho
        self.derecho = nuevoNodo                         #el derecho es el nuevo nodo

  
  #buscar palabra (NODO)
  def buscarPalabra(self,palabra):                                      #es llamada desde el arbol de a una palabra a la vez
      listaDePalabrasAux = Lista()
      
      if self.dato == palabra :                                         #si el dato del nodo es igual a la palabra por parámetro              
        listaDePalabrasAux = self.listaWeb                              #agrego la lista de páginas de ese dato en la lista auxiliar
      elif self.dato > palabra:                                         #si el dato del nodo es mayor al que viene por parámetro    
        if self.tieneIzquierdo():                                       #y si tiene izquierdo      
          listaDePalabrasAux = self.izquierdo.buscarPalabra(palabra)    # llamada recursiva a la misma función con el hijo izquierdo
      else:
        if self.tieneDerecho():                                         #si tiene derecho
          listaDePalabrasAux = self.derecho.buscarPalabra(palabra)      # llamada recursiva a la misma función con el hijo derecho
          
      return listaDePalabrasAux                                         #retorna una lista con *todas* las web de las palabras que coincidieron con la busqueda


  #buscar palabra de Pagina (NODO)
  def palabrasDePagina(self, direccionWeb,listaDePalabras):               

      if self.listaWeb.estaEnLista(direccionWeb):                       #si la dirección web que viene por parametro, está en la lista de páginas del nodo 
        listaDePalabras.append(self.dato)                               #entonces, agrego a mi lista de palabras la palabra del nodo

      if self.tieneDerecho():                                           #si tiene hijo derecho
        self.derecho.palabrasDePagina(direccionWeb, listaDePalabras)    #llamada recursiva a la función 

      if self.tieneIzquierdo():                                         #si tiene izquierdo    
        self.izquierdo.palabrasDePagina(direccionWeb, listaDePalabras)  #llamada recursiva a la función



  def eliminarPalabra(self, dato):                        #funcion eliminar del nodo
    nodoEliminar, nodoPadre, lado = self.buscaPadre(dato)  ##lado = "izq" / "der" - funcion que me "busca" y me retorna 3 cosas , un puntero al padre, un puntero al nodo y de que lado del padre esta ese nodo
    if nodoEliminar != None:                               #si es distinto de none, si encontró el dato en el arbol
      if nodoEliminar.grado() == 2:                      #este es el caso si tiene dos hijos
        nodoPred = nodoEliminar.predecesor()             #primero buscamos al predecesor del nodo eliminar, ahi tengo un puntero al nodo que quiero eliminar
        self.eliminarPalabra(nodoPred.dato)                     #ahora elimino al predecesor con la misma función (elDato Que esta en el predecesor) es el parametro
        nodoPred.izquierdo = nodoEliminar.izquierdo      #los hijos del nodo predecesor son los que eran los hijos del nodo a eliminar tanto izquierdo
        nodoPred.derecho = nodoEliminar.derecho          #como derecho
        if lado == "izq":                                #ahora tengo que poner al nodo predecesor como hijo del nodo padre dependiendo del lado, si es lado izq
          nodoPadre.izquierdo = nodoPred                 #el nodo predecesor es el hijo izquierdo del nodo padre
        else:                                            #si es lado derecho 
          nodoPadre.derecho = nodoPred                   #el nodo predecesor es hijo derecho del nodo padre 
      elif nodoEliminar.tieneIzquierdo():                # en este caso el hijo solo tiene izquierdo (tiene un solo hijo)
        if lado == "izq":                                #si el lado apunta al izquierdo, entonces el que quiero eliminar esta a la izquierda del padre
          nodoPadre.izquierdo = nodoEliminar.izquierdo   # entonces, el izquierdo del padre tiene que apuntar al izquierdo del nodo eliminar
        else:                                            # en este caso solo tiene hijo derecho, (estamos eliminando un nodo que solo tiene izquierdo, pero esta del lado derecho del padre)
          nodoPadre.derecho = nodoEliminar.izquierdo     #entonces el derecho del padre = al derecho del hijo
      elif nodoEliminar.tieneDerecho():                  # en este caso el hijo solo tiene derecho (tiene un solo hijo)
        if lado == "izq":                                #si esta a la izquierda del padre 
          nodoPadre.izquierdo = nodoEliminar.derecho     #el que esta a la izquierdo del padre, va ser el derecho del hijo 
        else:                                            #si esta a la derecha del padre
          nodoPadre.derecho = nodoEliminar.derecho       #el derecho del padre , va ser el derecho del hijo
      else:                                              #este el caso que el nodo que quiero eliminar no tiene nigun hijo
        if lado == "izq":                                #si el lado es el izquierdo
          nodoPadre.izquierdo = None                     #pongo a none el hijo izquierdo
        else:
          nodoPadre.derecho = None                       #pongo a none el hijo derecho

  
  
  #eliminarPagina (NODO)
 
  def eliminarPagina(self, direccionWeb, palabrasSinWeb):

      if self.listaWeb.estaEnLista(direccionWeb):                            #si la dirección web que viene por parametro , esta en la lista del nodo
        self.listaWeb.eliminar(self.listaWeb.posicionEnLista(direccionWeb))  #la elimino de la lista , llamando al eliminar de lista con la posicion de la página a borrar
        if self.listaWeb.estaVacia():                                        #y si luego del borrado, la lista del nodo esta vacía, 
          palabrasSinWeb.append(self.dato)                                   #agrego a mi lista aux listaSinWeb la palabra que quedo sin ninguna web en su lista 


      if self.tieneDerecho() :                                                #si tiene derecho
         self.derecho.eliminarPagina(direccionWeb, palabrasSinWeb)            #llamada recursiva a la función

      if self.tieneIzquierdo() :                                              #si tiene izquierdo  
         self.izquierdo.eliminarPagina(direccionWeb, palabrasSinWeb)          #llamada recursiva a la función

    

  #cantidad total de palabras (NODO)
  def cantidadTotalPalabras(self,cantidadLetras):
    contador = 0
    if self.cantidadLetrasDePalabra() >= cantidadLetras:                     #si la cantidad de letras de la palabra del nodo, es mayor o igual al numero que viene por parametro
      contador+= 1                                                           # incremento en uno el contador     
    
    if self.tieneDerecho():                                                   #si tiene derecho                                     
      contador += self.derecho.cantidadTotalPalabras(cantidadLetras)          #llamada recursiva a la función
      
    if self.tieneIzquierdo():                                                 #si tiene izquierdo
      contador += self.izquierdo.cantidadTotalPalabras(cantidadLetras)        #llamada recursiva a la función
      
    return contador
  
  #función aux (nodo) devuelve la cantidad de letras del dato/palabra
  def cantidadLetrasDePalabra(self):
    return len(self.dato)
  

  #función de esta balanceado (NODO)
  def estaBalanceado(self):
    alturaDerecho = 0
    alturaIzquierdo = 0
    

    if self.tieneDerecho():                         #si tiene hijo derecho
      alturaDerecho = self.derecho.altura()         #guardo la altura 

    if self.tieneIzquierdo():                       #si tiene izquierdo
      alturaIzquierdo = self.izquierdo.altura()     #guardo la altura  

    
    return alturaDerecho, alturaIzquierdo           #retorno las alturas    


  #paginas En Nivel (NODO)
  def paginasEnNivel(self,nivel,listaNivelWeb, nivelNodo = 0):
    pos = 0
    if nivelNodo == nivel:                                                      #si el nivelNodo es igual al nivel que viene por parámetro
      if self.dato != None:                                                     #y si el dato es distinto de None, o sea no esta vacio
        while pos < self.listaWeb.len():                                        #mientras la posición sea menor que el len de la lista de páginas del nodo
          listaNivelWeb.append(self.listaWeb.getDato(pos))                      #agrego la web en mi posición de la lista , a la lista que viene por parametro
          pos +=1                                                               #incremento el contador a uno
    else:                                                                       #si el nivel nodo no es igual al que viene por parámetro
      if self.tieneDerecho():                                                   #y si tiene derecho
        self.derecho.paginasEnNivel(nivel, listaNivelWeb, nivelNodo+1)          #llamada recursiva a la función, incrementando en uno el nivel  
      if self.tieneIzquierdo():                                                 #y si tiene izquierdo  
        self.izquierdo.paginasEnNivel(nivel, listaNivelWeb, nivelNodo+1)        #llamada recursiva a la función, incrementando en uno el nivel
  

  #cant de paginas mas usadas (nodo)
  def cantidadPalabrasMasUsadas(self,cantidadPaginas):
    cantidadPalabras = 0
    
    if self.listaWeb.len() >= cantidadPaginas :                                       #si el len de la lista de páginas web del nodo es mayor o igual a la cantidad de páginas que viene por parámetro
      cantidadPalabras +=1                                                            #incremento en uno el contador
      
    if self.tieneDerecho():                                                           #si tiene derecho   
      cantidadPalabras += self.derecho.cantidadPalabrasMasUsadas(cantidadPaginas)     #llamada recursiva a la función  
      
    if self.tieneIzquierdo():                                                         #si tiene izquierdo     
      cantidadPalabras += self.izquierdo.cantidadPalabrasMasUsadas(cantidadPaginas)   #llamda recursiva a la función
    
    return cantidadPalabras                                                           #retorna la cantidad de palabras
    
 
  #internas mayuscula alfabetico (NODO)  
  def internasMayusculaAlfabetico(self,listaPalabras):                                      
 
    if self.tieneIzquierdo():                                                         #si tiene izquierdo
      self.izquierdo.internasMayusculaAlfabetico(listaPalabras)                       #llamada recursiva la función
    
    if not self.esHoja() and self.primerLetraMayuscula():                                   #si no es hoja y tiene la primer letra en mayúscula
          listaPalabras.append(self.dato)                                                   #agrego la palabra que cumple la condición en mi lista
      
    if self.tieneDerecho():                                                           #si tiene derecho 
          self.derecho.internasMayusculaAlfabetico(listaPalabras)                     #llamada recursiva a la función

      
  #funcion aux que retorna *True* si la primer letra del dato es mayúscula 
  def primerLetraMayuscula(self):
    return self.dato[0].isupper()
      
  #ORIGINAL / SOLO NODOS

  #funcion para salida-graficar (nodo)  
  # def treePlot(self, dot):
  #     if self.tieneIzquierdo():
  #         dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
  #         dot.edge(str(self.dato), str(self.izquierdo.dato))
  #         self.izquierdo.treePlot(dot)
  #     else:
  #         dot.node("None"+str(self.dato)+"l", "None")
  #         dot.edge(str(self.dato), "None"+str(self.dato)+"l")
  #     if self.tieneDerecho():
  #         dot.node(str(self.derecho.dato), str(self.derecho.dato))
  #         dot.edge(str(self.dato), str(self.derecho.dato))
  #         self.derecho.treePlot(dot)
  #     else:
  #         dot.node("None"+str(self.dato)+"r", "None")
  #         dot.edge(str(self.dato), "None"+str(self.dato)+"r")
  
  #IMPLEMENTADA POR EL PROFESOR / NODOS + LISTA
  def treePlot(self, dot):
    if self.tieneIzquierdo():
      dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato)+'\n'+str(self.izquierdo.listaWeb))
      dot.edge(str(self.dato), str(self.izquierdo.dato))
      self.izquierdo.treePlot(dot)
    else:
      dot.node("None"+str(self.dato)+"l", "None")
      dot.edge(str(self.dato), "None"+str(self.dato)+"l")
    if self.tieneDerecho():
      dot.node(str(self.derecho.dato), str(self.derecho.dato)+'\n'+str(self.derecho.listaWeb))
      dot.edge(str(self.dato), str(self.derecho.dato))
      self.derecho.treePlot(dot)
    else:
      dot.node("None"+str(self.dato)+"r", "None")
      dot.edge(str(self.dato), "None"+str(self.dato)+"r")



########################################################   A R B O L


class ArbolBuscador:
  def __init__(self):
    self.raiz = None
 
    
  def estaVacio(self):
    return self.raiz == None

  #minimo (arbol)
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
 
  ########################################## Requerimientos del TP

  #insertar palabra (ARBOL)
  def insertarPalabra(self, dato, direccionWeb):                #inserta una palabra en el arbol y una página web
    nuevoNodo = NodoArbol(dato, direccionWeb)                   #creo un nuevo nodo
    
    if self.estaVacio():                                        #si el árbol esta vacío
      self.raiz = nuevoNodo                                     #la raíz es el nuevo nodo  
    else:
        self.raiz.insertar(nuevoNodo,direccionWeb)              #si no, llamo a insertar de nodo


  #insertar página (arbol) 
  def insertarPagina(self, listaDePalabras, direccionWeb):                      #recibe por parámetro una lista de palabras con una dirección web en común
    
    if not listaDePalabras.estaVacia():                                         #si la lista palabras que viene por parámetro no esta vacía
      cont = 0
      while cont < listaDePalabras.len() :                                      #y mientras el contador sea menor que el len de la lista que viene por parámetro
        self.insertarPalabra(listaDePalabras.getDato(cont), direccionWeb)       #va llamando a insertarPalabra de Nodo con cada una de las palabras para que las inserte, y la dirección web (el nodo se encarga de que una página no repita la misma web en su lista)
        cont += 1                                                               #incremento el contador a uno      


  #recibe una lista de palabras y devuelve todas las paginas web  en donde estan
  def buscarPalabras(self,listaDePalabras):
    listaWeb = Lista()
    cont = 0

    if not listaDePalabras.estaVacia():                                               #si la lista de palabras que viene por parámetro no esta vacía
      while cont < listaDePalabras.len():                                             #usamos el while, con un contador, mientras que el valor del mismo sea menor que el len de la lista que vino por parametro
        listaWeb.unirListas(self.raiz.buscarPalabra(listaDePalabras.getDato(cont)))   #llama al buscar palabra de nodo, pasando por parámetro de a una palabra a la vez (usando el getdato(cont) ) , nos devuelve la lista de páginas de ese dato y usando el unirListas quedan todas unidas dentro de listaWeb
        cont +=1                                                                      # se incrementa el contador en uno para ser usado en (cont) = posición

    listaWebClon = listaWeb.clonar()                                                  #ahora clonamos toda la lista completa en una nueva
    listaWeb.vaciarLista()                                                            #vaciamos nuestra lista original que contiene todas las listas de web unidas para luego solo cargarla con una sola sin repetir       
    pos = 0                                                                           #inicializamos un nuevo contador para utilizar en el while de abajo

    while pos < listaWebClon.len():                                                   #y mientras la posición sea menor que el len de la lista clonada
          
      if listaWebClon.cantWebRepetidasEnLista(listaWebClon.getDato(pos)) == listaDePalabras.len() and not listaWeb.estaEnLista(listaWebClon.getDato(pos)): #comparo la cantidad de veces que aparece repetida la paginaWeb en la lista clonada con el Len de la lista que recibo por parámetro y si no esta en la lista web clonada la agrega (la primera vez va estar vacia)
        listaWeb.append(listaWebClon.getDato(pos))                                    #agrego el dato a mi lista web antes vacía.
      pos +=1                                                                         #incremento el contador
      
      return listaWeb                                                                 #devuelve la lista con la página web en donde estan todas las palabras que vienieron en la lista por parametro


  #palabras de página (ARBOL)                  
  def palabrasDePagina(self,direccionWeb):                                            #recibe una dirección web y retorna una lista de todas las palabras de esa página
    listaDePalabras = Lista()                                                         #lista de palabras a retornar

    if not self.estaVacio():                                                          #si el arbol no esta vacio
      self.raiz.palabrasDePagina(direccionWeb, listaDePalabras)                       #llama al palabrasDePagina de nodo con la dirección web a buscar, la lista que devuelve contiene las palabras
    else:
      print("el árbol está vacío")
    return listaDePalabras                                                            #retorna la lista de palabras 



  #eliminar palabra (ARBOL)
  def eliminarPalabra(self, dato):                  # viene por parámetro el dato a borrar
    if not self.estaVacio():                        # se valida que el arbol no esta vacio
      if dato == self.raiz.dato:                    #primero se resuelven los casos particulares , si el elemento que quiero eliminar  esta en la raiz (dato == self.raiz.dato)
        if self.raiz.grado() == 2:                  # si tiene grado 2, o sea que tiene dos hijos (izq y der)
          nodoPred = self.raiz.predecesor()         #primero buscamos el predecesor y lo guardamos en una variable aux la cual quedará apuntando al predecesor aún despues de que lo eliminé
          self.eliminarPalabra(nodoPred.dato)       #eliminamos el predecesor llamando a la función de eliminar y pasando el dato por parámetro
          nodoPred.izquierdo = self.raiz.izquierdo  #entonces ahora apunto el izquierdo al que era el hijo izquierdo de la raiz, (donde apuntaba antes la raiz)
          nodoPred.derecho = self.raiz.derecho      #y tambien apunto el derecho al que era el hijo derecho de la raiz, (donde apuntaba antes la raiz)
          self.raiz = nodoPred                      # y por último ahora mi raiz, pasa a ser el nodo predecesor
        elif self.raiz.tieneIzquierdo():            # tiene grado uno, y aqui solo tiene izquierdo o sea un solo hijo
          self.raiz = self.raiz.izquierdo           # por lo tanto hay que reemplazar directamente al nodo por su hijo (en este caso izquierdo que es el único que tiene), el nodo raiz apunta ahora a su hijo izquierdo y ya queda eliminado el que queriamos
        elif self.raiz.tieneDerecho():              # tiene grado uno, y aquí solo tiene derecho
          self.raiz = self.raiz.derecho             # se hace lo mismo que las lineas de arriba pero en este caso es reemplazado directamente por su hijo derecho, el nodo raiz apunta ahora a su hijo derecho
        else:                                       #en este caso no tiene hijos, 
          self.raiz = None                          #así que ahora el nodo raiz apunta a None
      else:                                         # Ahora se resuleve el caso en que el dato a borrar no esté en la raiz, por eso, entonces
        self.raiz.eliminarPalabra(dato)             # si no es el dato de raiz, llamamos a la función eliminar del tipo nodo


  #eliminarPagina (ARBOL)  
  def eliminarPagina(self, direccionWeb):            #elimina del arbol la pagina web que recibe por parametro, debe eliminarla de todo el arbol
    listaSinWeb = Lista()
    cont = 0

    if not self.estaVacio():                                  #si el arbol no esta vacío
      self.raiz.eliminarPagina(direccionWeb, listaSinWeb)     #llamo eliminar pagina (de nodo), me retorna también una lista con las palabras que quedaron sin ningúna página 
    else:
      print("el árbol está vacío")
    
    while cont < listaSinWeb.len():                           #elimina una palabra sin web, mientras que el contador sea menor que el len de la lista de palabras sin web
      self.eliminarPalabra(listaSinWeb.getDato(cont))         #llamo al eliminar palabra del arbol , pasando por parametro el dato/palabra a borrar y de esa manera quitarla del arbol
      cont +=1   
 

  #cantidad todal palabras (ARBOL)
  def cantidadTotalPalabras(self,cantidadLetras):   #recibe una cantidad de letras y devuelve la cantidad de palabras del arbol que contienen esa cantidad de letras o más
    aux = 0
    if not self.estaVacio():                                  #si el árbol no esta vacío
      aux = self.raiz.cantidadTotalPalabras(cantidadLetras)   #llamamos a la función cantidadTotalDePalabras de nodo
    else:
      print ("el árbol está vacío")  
    return aux


  #esta Balanceado (ARBOL)
  def estaBalanceado(self): 
    balanceado = False                                                       #inicializo mis variables
    derecho = 0                                                               
    izquierdo = 0 

    if not self.estaVacio():                                                 #si el árbol no esta vacío   
      derecho, izquierdo = self.raiz.estaBalanceado()                        #llamo a estaBalanceado de nodo
    else:
      print("el árbol está vacío")

    if ((derecho - izquierdo) <= 1) and ((derecho - izquierdo) >= -1):       #con lo retornado desde nodo comparo para obtener si mi diferencia es de uno 
      balanceado = True                                                      # si la condición se cumple, cambia a verdadero a mi variable 

    return balanceado                                                        #retorno true o false 
  

  #paginas en nivel (ARBOL)
  def paginasEnNivel(self, nivel):
    listaNivel = Lista()

    if not self.estaVacio():                                                  #si el árbol no esta vacío
      self.raiz.paginasEnNivel(nivel, listaNivel)                             #llamo a la función páginas en nivel de nodo
    else:
      print("El árbol está vacío")

    listaNivelClonada = listaNivel.clonar()                                   #clono la lista con los resultados desde el nodo
    listaNivel.vaciarLista()                                                  #y vaciamos la lista original
    pos = 0
    
    while pos < listaNivelClonada.len():                                      # mientras la posición sea menor que el len de la lista clonada 
      if not listaNivel.estaEnLista(listaNivelClonada.getDato(pos)):          #y si la web en la posición no está en la lista original (la primera vez esta vacía)  
        listaNivel.append(listaNivelClonada.getDato(pos))                     #la agrego a la lista
      pos +=1  

    return listaNivel                                                         #retorno la lista con todas las web del nivel 


  #cantidad Palabras Mas Usadas (ARBOL)
  def cantidadPalabrasMasUsadas(self,cantidadPaginas):
    
    cantidadPalabras = 0
    
    if not self.estaVacio():                                                    # si el árbol no esta vacío
      cantidadPalabras = self.raiz.cantidadPalabrasMasUsadas(cantidadPaginas)   #llamo a cantidad palabras mas usadas de nodo
    else:
      print ("el árbol está vacío") 

    return cantidadPalabras                                                     #retorno la cantidad de palabras
  
    
  #internas Mayusculas en orden Alfabetico (ARBOL)
  def internasMayusculaAlfabetico(self):                                        #retorna una lista con las palabras que tienen su primer letra en mayúscula , que no sean una hoja y en orden alfabético
    listaPalabras = Lista()
    
    if not self.estaVacio():                                                    #si el árbol no está vacio
      self.raiz.internasMayusculaAlfabetico(listaPalabras)                      # llamo a la funcion internas mayúscula alfabético de nodo
    else:
      print ("el árbol está vacío")    
          
          
    return listaPalabras                                                        #retorno la lista de palabras en orden alfabético



  #ORIGINAL SOLO NODOS
  #funcion para salida-graficar (ARBOL)  
  # def treePlot(self, fileName='representacionAbolEjemplo'):
  #   if not self.estaVacio():
  #     treeDot = Digraph()
  #     treeDot.node(str(self.raiz.dato), str(self.raiz.dato))
  #     self.raiz.treePlot(treeDot)
  #     treeDot.render(fileName, view=True)

  #IMPLEMENTADA POR EL PROFESOR / NODOS + LISTA
  def treePlot(self, fileName='tree'):
    if not self.estaVacio():
      treeDot = Digraph()
      treeDot.node(str(self.raiz.dato), str(self.raiz.dato)+'\n'+str(self.raiz.listaWeb))
      self.raiz.treePlot(treeDot)
      treeDot.render(fileName, view=True)

