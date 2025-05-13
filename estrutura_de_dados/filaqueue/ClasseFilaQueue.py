from queue import Queue

class ClasseFilaQueue:
    def __init__(self):
        self.fila_queue = Queue(maxsize=5)

    def adicionar(self, nome):
        return self.fila_queue.put(nome)    
    
    def listar(self):
        return self.fila_queue

    def quantidade(self):
        return self.fila_queue.qsize()
    
    def verificar(self):
        return self.fila_queue.full()
    
    def remover(self):
        return self.fila_queue.get()
    
