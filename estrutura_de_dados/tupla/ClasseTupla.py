class ClasseTupla:
    def __init__(self):
        self.tupla = ()

    def listar(self):
        return self.tupla  

    def adicionar(self, elemento): 
        lista = list(self.tupla)
        lista.append(elemento)
        self.tupla = tuple(lista)

    def contar_ocorrencias(self, nome):
        return self.tupla.count(nome.lower())
    
    def buscar_indice(self, elemento):
        return self.tupla.index(elemento)
    
    def quantidade(self):
        return len(self.tupla)
    
    def ordem_maxima(self):
        return max(self.tupla)
    
    def ordem_minima(self):
        return min(self.tupla)