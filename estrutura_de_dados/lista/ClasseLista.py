class ClasseLista:
    def __init__(self):
        self.estrutura_lista = []
        self.estrutura_sublista = []

    def adicionar(self, elemento):
        self.estrutura_lista.append(elemento)

    def listar(self): 
        return self.estrutura_lista

    def inserir_com_posicao(self, posicao, elemento):     
        return self.estrutura_lista.insert(posicao, elemento)   

    def pesquisar_por_letras(self, elemento):
        for itens in self.estrutura_lista:
            if itens.startswith(elemento.lower()):
                self.estrutura_sublista.append(itens.lower())

    def sublistar(self):
        return self.estrutura_sublista  
               
    def excluir(self, elemento):   
        self.estrutura_lista.remove(elemento.lower())

    def quantidade_ocorrencias(self, elemento):
        return self.estrutura_lista.count(elemento.lower())
    
    def limpar_lista(self):
        return self.estrutura_lista.clear()