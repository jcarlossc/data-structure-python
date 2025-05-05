class ClasseTupla:
    def __init__(self):
        self.tupla = ('carlos', 'teresa', 'soares', 'carlos', 'carlos', 'teresa')

    def iterar_tupla(self):
        return self.tupla    

    def contar_ocorrencias(self, nome):
        return self.tupla.count(nome.lower())
    
    def buscar_indice(self, nome):
        return self.tupla.index(nome.lower())
    
    def quantidade(self):
        return len(self.tupla)
    
    def maximo(self):
        return max(self.tupla)
    
    def minimo(self):
        return min(self.tupla)