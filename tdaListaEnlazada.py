##lista dinamica recursiva

###########################                            N O D O  L I S T A 

class NodoLista:
  def __init__(self, dato = None):
    self.dato = dato
    
    self.siguiente = None

  def tieneSiguiente(self):
        return self.siguiente != None

  def append(self, nodoNuevo):
    if self.tieneSiguiente():
      self.siguiente.append(nodoNuevo)
    else:
      self.siguiente = nodoNuevo


  def len(self):
    cant = 1
    if self.tieneSiguiente():
      cant += self.siguiente.len()
    return cant



  def getDato(self, getPos, actPos = 0):
    dato = None
    if actPos == getPos:
      dato = self.dato
    else:
      dato = self.siguiente.getDato(getPos, actPos+1)
    return dato


  def eliminar(self, delPos, actPos = 0):
    if actPos == delPos-1:
      self.siguiente = self.siguiente.siguiente
    else:
          self.siguiente.eliminar(delPos, actPos+1)


  def clonar(self, listaClon):
    listaClon.append(self.dato)
    if self.tieneSiguiente():
      self.siguiente.clonar(listaClon)


  
  def estaEnLista(self,dato):
    aux = False
    if self.dato == dato:
      aux = True
    else:
      if self.tieneSiguiente():
        aux = self.siguiente.estaEnLista(dato)
    return aux


      


################## L I S T A


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

  def vaciarLista(self):
      self.primero = None

  def append(self, dato):
    nodoNuevo = NodoLista(dato)
    if self.estaVacia():
      self.primero = nodoNuevo
    else:
      self.primero.append(nodoNuevo)

  def len(self):
    cant = 0
    if not self.estaVacia():
      cant = self.primero.len()
    return cant


  def getDato(self, pos):
    if 0 <= pos < self.len() and not self.estaVacia():
      return self.primero.getDato(pos)
    else:
      raise Exception("Posicion invalida")


  #eliminarDeLista (LISTA)

  def eliminar(self, pos):
    if 0 <= pos < self.len() and not self.estaVacia():
      if pos == 0:
        self.primero = self.primero.siguiente
      else:
        self.primero.eliminar(pos)
    else:
      raise Exception("Posicion invalida")


  def clonar(self):
    listaClon = Lista()
    if not self.estaVacia():

      self.primero.clonar(listaClon)
    return listaClon


  def estaEnLista(self,direccionWeb):
    aux = False
    if not self.estaVacia():
      aux = self.primero.estaEnLista(direccionWeb)
    return aux



  def posicionEnLista(self,dato):
    aux = self.primero
    pos = 0

    while aux.dato != dato:   
      pos += 1
      aux = aux.siguiente 

    return pos  


  #funcion Auxiliar
  def unirListas(self,lista):
    aux = lista.primero
    while aux != None: 
      self.append(aux.dato)
      aux = aux.siguiente

  #funcionAuxiliar
  def cantWebRepetidasEnLista(self,paginaWeb):
    aux = self.primero
    cont = 0
    while aux != None:
      if aux.dato == paginaWeb:
        cont += 1        
      aux = aux.siguiente
    
    return cont
