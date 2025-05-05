class ClasseConjunto:
    def __init__(self):
        self.conjunto = set()
        self.conjunto_suporte = set(('jeck da costa', 'duda soares', 'zeck soares'))

    def iterar_conjunto(self):
        return self.conjunto    
    
    def adicionar(self, nome):
        self.conjunto.add(nome.lower())

    def excluir(self, nome):
        self.conjunto.remove(nome.lower())

    def excluir_aleatorio(self):
        self.conjunto.pop()    

    def uniao(self):
        conjunto_unido = self.conjunto.union(self.conjunto_suporte)  
        return conjunto_unido
    
    def intersecao(self):
        conjunto_intersecao = self.conjunto.intersection(self.conjunto_suporte)
        return conjunto_intersecao
    
    def diferenca(self):
        conjunto_diferenca = self.conjunto.difference(self.conjunto_suporte)
        return conjunto_diferenca