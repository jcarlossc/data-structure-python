class ClasseLista:
    def __init__(self):
        self.estrutura_lista = []
        self.estrutura_sublista = []

    def adicionar_na_lista(self, elemento):
        self.estrutura_lista.append(elemento.lower())

    def iterar_lista(self): 
        return self.estrutura_lista

    def inserir_com_posicao(self, posicao, nome):     
        self.estrutura_lista.insert(posicao, nome)   

    def pesquisar_por_letras(self, elemento):
        for itens in self.estrutura_lista:
            if itens.startswith(elemento.lower()):
                self.estrutura_sublista.append(itens)

    def sublistar(self):
        return self.estrutura_sublista  
               
    def excluir_da_lista(self, elemento):   
        self.estrutura_lista.remove(elemento.lower())

    def quantidade_ocorrencias(self, elemento):
        return self.estrutura_lista.count(elemento)
    
    def limpar_lista(self):
        return self.estrutura_lista.clear()