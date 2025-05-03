import os
from estrutura_de_dados.lista.ClasseLista import ClasseLista

class Menu:
    def __init__(self):
        pass

    @classmethod    
    def menu(self):

        def menu_principal():
            print("\n-------------------------- ESTRUTURAS DE DADOS --------------------------")
            print("1 - LISTA")
            print("2 - TUPLA")
            print("3 - SET")
            print("4 - FROZENSET")
            print("5 - DICIONÁRIO")
            print("6 - DEQUE")
            print("7 - QUEUE")
            print("8 - HEAPQ")
            print("9 - SAIR")
            print("----------------------------------- FIM ---------------------------------\n")

        lista = ClasseLista()

        def limpar_tela():
            os.system('cls' if os.name == 'nt' else 'clear')

        limpar_tela()    

        while True:  
            menu_principal()
            tipo_estrutura = input("ESCOLHA O TIPO DE ESTRUTURA DE DADOS: ")

            if tipo_estrutura == "1":
                pass
            elif tipo_estrutura == "2":
                pass
            elif tipo_estrutura == "3":
                pass
            elif tipo_estrutura == "4":
                pass
            elif tipo_estrutura == "5":
                pass
            elif tipo_estrutura == "6":
                pass
            elif tipo_estrutura == "7":
                pass
            elif tipo_estrutura == "8":
                pass
            elif tipo_estrutura == "9":
                limpar_tela()
                print("SAIR, ATÉ A PRÓXIMA!")
                exit()
                
            else:
                limpar_tela()
                print("❌ Opção inválida!")