import heapq

class ClasseHeapq:
    def __init__(self):
        self.lista = []

    def iterar_heapq(self):
        return self.lista 
    
    def adicionar(self, elemento):
        return heapq.heappush(self.lista, elemento.lower())

    def remover(self):
        return heapq.heappop(self.lista)

    def quantidade(self):
        return len(self.lista)    