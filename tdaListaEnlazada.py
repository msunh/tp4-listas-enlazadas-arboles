##lista dinamica recursiva

###########################  N O D O  L I S T A 

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

  def recPre(self):
    print(self.dato)
    if self.tieneSiguiente():
      self.siguiente.recPre()


  def recPost(self):
    if self.tieneSiguiente():
          self.siguiente.recPost()
    print(self.dato)


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



  def reemplazar(self, viejo, nuevo):
    if self.dato == viejo:
      self.dato = nuevo
    if self.tieneSiguiente():
      self.siguiente.reemplazar(viejo, nuevo)



  def clonar(self, listaClon):
    listaClon.append(self.dato)
    if self.tieneSiguiente():
      self.siguiente.clonar(listaClon)



  def clonarInvertido(self, listaClon):
    if self.tieneSiguiente():
      self.siguiente.clonarInvertido(listaClon)
    listaClon.append(self.dato)


  def deleteAll(self, dato):
    cant = 0
    if self.tieneSiguiente():
      if self.siguiente.dato == dato:
        self.siguiente = self.siguiente.siguiente
        cant = 1 + self.deleteAll(dato)
      else:
        cant = self.siguiente.deleteAll(dato)  
    return cant

  
  def estaEnLista(self,dato):
    aux = False
    if self.dato == dato:
      aux = True
    else:
      if self.tieneSiguiente():
        aux = self.siguiente.estaEnLista(dato)
    return aux

  # def estaEnListaPos(self,dato):
  #   aux = False
  #   posicion = 0
  #   if self.dato == dato:
  #     aux = True      
  #   else:
  #     if self.tieneSiguiente():
  #       aux = self.siguiente.estaEnListaPos(dato)
  #       posicion += 1

  #   return posicion  
      


################## L I S T A


class Lista:
  def __init__(self):
    self.primero = None

  def estaVacia(self):
        return self.primero == None

  def __repr__(self):
    out = "primero"
    aux = self.primero
    while aux != None:
      out += " -> " + str(aux.dato)
      aux = aux.siguiente
    out += " -|"
    return out

  def vaciarLista(self):
      self.primero = None

  def append(self, dato):
    nodoNuevo = NodoLista(dato)
    if self.estaVacia():
      self.primero = nodoNuevo
    else:
      self.primero.append(nodoNuevo)


  def recPre(self):
    if not self.estaVacia():
      self.primero.recPre()



  def len(self):
    cant = 0
    if not self.estaVacia():
      cant = self.primero.len()
    return cant


  def recPost(self):
    if not self.estaVacia():
      self.primero.recPost()

  def getDato(self, pos):
    if 0 <= pos < self.len() and not self.estaVacia():
      return self.primero.getDato(pos)
    else:
      raise Exception("Posicion invalida")


  #eliminarDeLista    

  def eliminar(self, pos):
    if 0 <= pos < self.len() and not self.estaVacia():
      if pos == 0:
        self.primero = self.primero.siguiente
      else:
        self.primero.eliminar(pos)
    else:
      raise Exception("Posicion invalida")


  def reemplazar(self, viejo, nuevo):
    if not self.estaVacia():
      self.primero.reemplazar(viejo, nuevo)
    else:
      raise Exception("Lista Vacia")

  def clonar(self):
    listaClon = Lista()
    if not self.estaVacia():

      self.primero.clonar(listaClon)
    return listaClon


  def clonarInvertido(self):
    listaClon = Lista()
    if not self.estaVacia():
      self.primero.clonarInvertido(listaClon)
    return listaClon


  def deleteAll(self, dato):
    cant = 0
    if not self.estaVacia():
      if self.primero.dato == dato:
        self.primero = self.primero.siguiente
        cant = 1 + self.deleteAll(dato)
      else:
        cant = self.primero.deleteAll(dato)
    return cant

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



  def unirListas(self,lista):
    aux = lista.primero
    while aux != None: 
      self.append(aux.dato)
      aux = aux.siguiente

  def cantWebRepetidasEnLista(self,paginaWeb):
    aux = self.primero
    cont = 0
    while aux != None:
      if aux.dato == paginaWeb:
        cont += 1        
      aux = aux.siguiente
    
    return cont


# lista1 = Lista()
# lista1.append("carlos.com")
# lista1.append("carlitos.com")

# print(lista1.posicionEnLista("carlitos.com"))


  # def deleteAll(self, dato, actPos = 0):
  #   cant = 0
  #   if not self.estaVacia() and actPos < self.len():
  #     if self.getDato(actPos) == dato:
  #       self.delete(actPos)
  #       cant = 1 + self.deleteAll(dato, actPos)
  #     else:
  #       cant = self.deleteAll(dato, actPos+1)
  #   return cant