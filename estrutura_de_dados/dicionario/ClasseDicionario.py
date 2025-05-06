class ClasseDicionario:
    def __init__(self):
        self.dicionario = {}

    def adicionar(self, nome, idade):
        chave = len(self.dicionario)
        self.dicionario[chave] = {"Nome": nome, "Idade": idade}
        
    def iterar_dicionario(self):
        return self.dicionario.items()
    
    def buscar(self, id):
        return self.dicionario.get(id)
    
    def copiar(self):
        return self.dicionario.copy()
    
    def remover(self, chave):
        return self.dicionario.pop(chave)
    
    def limpar(self):
        return self.dicionario.clear()