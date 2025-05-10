import heapq

class ClasseHeapq:
    def __init__(self):
        self.lista = []

    def listar(self):
        return self.lista 
    
    def adicionar(self, elemento):
        return heapq.heappush(self.lista, elemento.lower())

    def excluir(self):
        return heapq.heappop(self.lista)

    def quantidade(self):
        return len(self.lista)    