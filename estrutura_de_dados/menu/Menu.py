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

        def menu_lista():
            print("\n--------------------------------- LISTA ---------------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - INSERIR COM POSIÇÃO")
            print("4 - PESQUISAR POR LETRAS")
            print("5 - EXCLUIR")
            print("6 - QUANTIDADE")
            print("7 - LIMPAR LISTA")
            print("8 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")    

        lista = ClasseLista()

        def limpar_tela():
            os.system('cls' if os.name == 'nt' else 'clear')

        limpar_tela()    

        # While principal do menu.
        while True:  
            menu_principal()
            tipo_estrutura = input("ESCOLHA O TIPO DE ESTRUTURA DE DADOS: ")

            if tipo_estrutura == "1":
                limpar_tela()

                # While da lista.
                while True:
                    menu_lista()
                    opcoes_lista = input("ESCOLHA UMA OPERAÇÃO: ")
                    
                    # Condicional da lista - Iterar elementos.
                    if opcoes_lista == "1":
                        limpar_tela()
                        if not lista.iterar_lista():
                            limpar_tela()
                            print("⚠️  Lista vazia")

                        elif opcoes_lista == None:
                            limpar_tela()
                            print("⚠️  Entrada inválida!")

                        else:   
                            for itens in lista.iterar_lista():
                                print("👤", itens.title()) 

                    # Condicional da lista - Adicionar elementos.
                    elif opcoes_lista == "2":
                        limpar_tela()
                        menu_lista()
                        elemento_adicionar_lista = input("DIGITE UM NOME: ")

                        if elemento_adicionar_lista.replace(" ", "").isalpha():
                            lista.adicionar_na_lista(elemento_adicionar_lista)
                            limpar_tela()
                            print("✅ Adicionado com sucesso!")
                            
                        elif elemento_adicionar_lista == None:    
                            limpar_tela()
                            print("❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")  

                    # Condicional da lista - Adicionar elementos com posição(index)
                    elif opcoes_lista == "3":
                        limpar_tela()
                        menu_lista()
                        posicao_lista = input("DIGITE A POSIÇÃO: ")  
                        elemento_inserir_lista = input("DIGITE O NOME: ")  

                        if posicao_lista.isdigit() and elemento_inserir_lista.replace(" ", "").isalpha():    
                            numero_lista = int(posicao_lista)
                            lista.inserir_com_posicao(numero_lista, elemento_inserir_lista) 
                            limpar_tela()
                            print("✅ Inserido com sucesso!")

                        elif posicao_lista == None or elemento_inserir_lista == None:
                            limpar_tela()
                            print("❌ Entrada inválida!")       

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")   
                                
                    # Condicional da lista - Pesquisar elementos.
                    elif opcoes_lista == "4":
                        limpar_tela()  
                        menu_lista()  
                        elemento_pesquisar_lista = input("PESQUISAR NOME: ")

                        if elemento_pesquisar_lista.replace(" ", "").isalpha():
                            limpar_tela()
                            lista.pesquisar_por_letras(elemento_pesquisar_lista)
                            for itens in lista.estrutura_sublista:
                                print("👤", itens)
                            lista.estrutura_sublista.clear()     
                          
                        elif elemento_pesquisar_lista == None:  
                            limpar_tela()
                            print("❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")  

                    # Condicional da lista - Excluir elementos.
                    elif opcoes_lista == "5":
                        limpar_tela()  
                        menu_lista()  
                        elemento_excluir_lista = input("EXCLUIR NOME: ")

                        if elemento_excluir_lista.replace(" ", "").isalpha():
                            lista.excluir_da_lista(elemento_excluir_lista)
                            limpar_tela()
                            print("✅ Excluído com sucesso!")
                          
                        elif elemento_excluir_lista == None:   
                            limpar_tela() 
                            print("❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")   

                    # Condicional da lista - Verificar quantidade de elementos.
                    elif opcoes_lista == "6":
                        limpar_tela()
                        menu_lista()
                        contar_elemento_lista = input("DIGITE O NOME: ")

                        if not lista.iterar_lista():
                            limpar_tela()
                            print("⚠️  Lista vazia")

                        elif contar_elemento_lista.replace(" ", "").isalpha():
                            quantidade_elementos = lista.quantidade_ocorrencias(contar_elemento_lista)
                            limpar_tela()
                            print("✅ A lista possui", quantidade_elementos, "elementos do tipo", contar_elemento_lista, ".")  

                        elif contar_elemento_lista == None:
                            limpar_tela()
                            print("❌ Entrada inválida!")      

                        else:   
                            limpar_tela()
                            print("❌ Entrada inválida!")


                    elif opcoes_lista == "7":
                        pass             
                    elif opcoes_lista == "8":
                        break

                    else:
                        limpar_tela()
                        print("❌ Opção inválida.")

                limpar_tela()              


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