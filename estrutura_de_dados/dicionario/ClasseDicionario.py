class ClasseDicionario:
    def __init__(self):
        self.dicionario = {}

    def adicionar(self, elemento, idade):
        chave = len(self.dicionario)
        self.dicionario[chave] = {"Nome": elemento, "Idade": idade}
        
    def listar(self):
        return self.dicionario
    
    def pesquisar(self, id):
        return self.dicionario.get(id)
    
    def copiar(self):
        return self.dicionario.copy()
    
    def excluir(self, chave):
        return self.dicionario.pop(chave)
    
    def limpar(self):
        return self.dicionario.clear()