class ClasseFrozenset:
    def __init__(self):
        self.conjunto_frozen = frozenset(['carlos costa', 'maria teresa', 'jose carlos'])
        self.conjunto_frozen_suporte = frozenset(['maria teresa', 'jeck soares', 'jose carlos'])

    def listar(self):
        return self.conjunto_frozen    
    
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