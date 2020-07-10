##lista dinamica recursiva

###########################                            N O D O  L I S T A 

class NodoLista:
  def __init__(self, dato = None):
    self.dato = dato  
    self.siguiente = None

  def tieneSiguiente(self):
        return self.siguiente != None

  #agrega un elemento a la lista
  def append(self, nodoNuevo):    
    if self.tieneSiguiente():            #si tiene siguiente, 
      self.siguiente.append(nodoNuevo)   #agrega el nodo nuevo a continuación del siguiente / llamada recursiva a la función
    else:
      self.siguiente = nodoNuevo         #si no tiene siguiente, el siguiente es el nodo nuevo      

  #devuelve la cantidad de elementos de la lista
  def len(self):                          
    cant = 1
    if self.tieneSiguiente():             #si tiene siguiente
      cant += self.siguiente.len()        #incrementa en uno el contador / llamada recursiva a la función
    return cant                           #devuelve un la cantidad(numero)


  #devuelve el dato , segun la posicion dada
  def getDato(self, getPos, actPos = 0):                    
    dato = None                                                   
    if actPos == getPos:                                                  
      dato = self.dato
    else:
      dato = self.siguiente.getDato(getPos, actPos+1)
    return dato

  #elimina un elemento según la posición indicada por parametro
  def eliminar(self, delPos, actPos = 0):
    if actPos == delPos-1:
      self.siguiente = self.siguiente.siguiente
    else:
          self.siguiente.eliminar(delPos, actPos+1)

  #clona la lista
  def clonar(self, listaClon):
    listaClon.append(self.dato)
    if self.tieneSiguiente():
      self.siguiente.clonar(listaClon)


  #devuelve *True* si el dato que viene por parámetro está en la lista
  def estaEnLista(self,dato):
    aux = False
    if self.dato == dato:                        #si el dato del nodo es igual al buscado
      aux = True                                 #la variable cambia true   
    else:                                        #si no 
      if self.tieneSiguiente():                  #si tiene siguiente 
        aux = self.siguiente.estaEnLista(dato)   #llamada recursiva la función 
    return aux


      


########################################################   L I S T A


class Lista:
  def __init__(self):
    self.primero = None

  def estaVacia(self):
    return self.primero == None

  def __repr__(self):
    out = "["
    aux = self.primero
    while aux != None:
      out += " , " + str(aux.dato)
      aux = aux.siguiente
    out += "]"
    return out

  #vaciar lista
  def vaciarLista(self):                                  #apunta el primero a none
      self.primero = None

  #agrega elementos de la lista
  def append(self, dato):                                 
    nodoNuevo = NodoLista(dato)
    if self.estaVacia():
      self.primero = nodoNuevo
    else:
      self.primero.append(nodoNuevo)

  #devuelve la cantidad de elementos de la lista
  def len(self):
    cant = 0
    if not self.estaVacia():
      cant = self.primero.len()
    return cant

  #get dato (LISTA) se obtiene el dato segun la posicion que se pasa por parámetro
  def getDato(self, pos):
    if 0 <= pos < self.len() and not self.estaVacia():
      return self.primero.getDato(pos)
    else:
      raise Exception("Posicion invalida")


  #eliminarDeLista (LISTA)

  def eliminar(self, pos):                                  
    if 0 <= pos < self.len() and not self.estaVacia():    # si la posicion a eliminar es menor o igual a cero y menor que el len de la lista, y no esta vacía 
      if pos == 0:                                        #y si la posicion es igual a cero (o sea la primera)
        self.primero = self.primero.siguiente             #ahora el primero , es el siguiente
      else:
        self.primero.eliminar(pos)                        #llamada recursiva a la función
    else:
      raise Exception("Posicion invalida")

  #clona una lista    
  def clonar(self):
    listaClon = Lista()                              #crea una lista nueva 
    if not self.estaVacia():                         #si la lista no esta vacia 

      self.primero.clonar(listaClon)                 #llama a la función clonar del nodo 
    return listaClon                                 #devuelve una lista clonada 


  #funcion aux que devuelve si una pagina web que viene por parametro esta en la lista de paginas web que contiene el nodo
  def estaEnLista(self,direccionWeb):
    aux = False
    if not self.estaVacia():                         #si no está vacia
      aux = self.primero.estaEnLista(direccionWeb)   #pregunta si esta en el primer nodo, sino hace la llamada recursiva a la funcón 
    return aux


  #funcion auxiliar que devuelve la posicion en donde se encuentra un dato dentro de la lista
  def posicionEnLista(self,dato):
    aux = self.primero
    pos = 0

    while aux.dato != dato:       #mientras el dato del nodo sea distinto del dato que viene por parámetro
      pos += 1                    #incrementa el contador a uno
      aux = aux.siguiente         #ahora aux es el siguiente

    return pos                    #retorna la posición


  #funcion Auxiliar (LISTA) para unir varias listas en una sola
  def unirListas(self,lista):     #recibe una lista por parámetro    
    aux = lista.primero           #aux arranca en primero
    while aux != None:            #mientras aux no apunte a none ( o sea tiene siguiente)
      self.append(aux.dato)       #hago append del dato
      aux = aux.siguiente         #ahora aux es el siguiente, repite el proceso hasta que aux apunte a none (haya recorrido toda la lista)



  #funcionAuxiliar, devuelve la cantidad de veces que una pagina web está repetida en una lista (un numero)
  def cantWebRepetidasEnLista(self,paginaWeb): 
    aux = self.primero            #aux arranca en primero
    cont = 0
    while aux != None:            #y mientras aux tenga siguiente
      if aux.dato == paginaWeb:   #y si el dato en el nodo es igual con la página que viene por parámetro
        cont += 1                 #incremento mi contador a uno
      aux = aux.siguiente         #ahora aux es el sigiente. repite el proceso hasta que aux apunte a none (haya recorrido toda la lista)
    
    return cont
