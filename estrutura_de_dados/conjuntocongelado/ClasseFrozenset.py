class ClasseFrozenset:
    def __init__(self):
        self.conjunto = set()
        self.conjunto_frozen = frozenset()
        self.conjunto_frozen_suporte = frozenset(['carlos', 'jose', 'maria'])

    def listar(self):
        return self.conjunto_frozen  

    def adicionar(self, elemento):  
        self.conjunto.add(elemento)
        self.conjunto_frozen = frozenset(self.conjunto)
    
    def uniao(self):
        conjunto_frozen_unido = self.conjunto_frozen.union(self.conjunto_frozen_suporte)  
        return conjunto_frozen_unido
    
    def intersecao(self):
        conjunto_frozen_intersecao = self.conjunto_frozen.intersection(self.conjunto_frozen_suporte)  
        return conjunto_frozen_intersecao
    
    def diferenca(self):
        conjunto_congelado_diferenca = self.conjunto_frozen.difference(self.conjunto_frozen_suporte)  
        return conjunto_congelado_diferenca
    
    def copiar(self):
        return self.conjunto_frozen.copy()