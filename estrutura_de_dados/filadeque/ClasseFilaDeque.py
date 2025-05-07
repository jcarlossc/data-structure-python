from collections import deque

class ClasseFilaDeque:
    def __init__(self):
        self.fila_deque = deque()

    def adicionar(self, nome):
        return self.fila_deque.append(nome)  

    def iterar_deque(self):  
        return self.fila_deque
    
    def adiciona_comeco(self, nome):
        return self.fila_deque.appendleft(nome)

    def remove_fim(self):
        return self.fila_deque.pop()
    
    def remover_primeiro(self):
        return self.fila_deque.popleft()
    
    def limpar(self):
        return self.fila_deque.clear()