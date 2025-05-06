import os
from estrutura_de_dados.conjunto.ClasseConjunto import ClasseConjunto
from estrutura_de_dados.lista.ClasseLista import ClasseLista
from estrutura_de_dados.tupla.ClasseTupla import ClasseTupla

class Menu:
    def __init__(self):
        pass

    @classmethod    
    def menu(self):

        # Método principal.
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

        # Método menu da lista.
        def menu_lista():
            print("\n--------------------------------- LISTA ---------------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - INSERIR COM POSIÇÃO")
            print("4 - PESQUISAR POR LETRAS")
            print("5 - EXCLUIR")
            print("6 - QUANTIDADE DE OCORRÊNCIAS")
            print("7 - LIMPAR LISTA")
            print("8 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")    

        # Método menu da tupla.
        def menu_tupla():
            print("\n--------------------------------- TUPLA ---------------------------------")
            print("1 - LISTAR")
            print("2 - PESQUISAR OCORRÊNCIAS")
            print("3 - PESQUISAR POR ÍNDICE")
            print("4 - QUANTIDADE DE ELEMENTOS")
            print("5 - ORDEM MÁXIMO")
            print("6 - ORDEM MÍNIMO")
            print("7 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")    

        # Método menu do conjunto(set).
        def menu_conjunto():
            print("\n-------------------------------- CONJUNTO -------------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - EXCLUIR")
            print("4 - EXCLUIR ALEATÓRIO")
            print("5 - UNIÃO")
            print("6 - INTERSEÇÃO")
            print("7 - DIFERENÇA")
            print("8 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")  

        # Instâncias das classes das estruturas de dados.
        lista = ClasseLista()
        tupla = ClasseTupla()
        conjunto = ClasseConjunto()

        # Método para limpar tela.
        def limpar_tela():
            os.system('cls' if os.name == 'nt' else 'clear')

        # Chama método para limpar tela.
        limpar_tela()    

        # While principal do menu.
        while True:  
            menu_principal()
            tipo_estrutura = input("ESCOLHA O TIPO DE ESTRUTURA DE DADOS: ")

            # Condicional principal - Lista.
            if tipo_estrutura == "1":
                limpar_tela()

                # While da lista.
                while True:
                    menu_lista()
                    opcoes_lista = input("ESCOLHA UMA OPERAÇÃO: ")
                    
                    # Condicional da lista - Itera elementos.
                    if opcoes_lista == "1":
                        limpar_tela()
                        if not lista.iterar_lista():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")

                        elif opcoes_lista == None:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                        else:   
                            for itens in lista.iterar_lista():
                                print(f"👤 {itens.title()}") 

                    # Condicional da lista - Adicionar elementos.
                    elif opcoes_lista == "2":
                        limpar_tela()
                        menu_lista()
                        elemento_adicionar_lista = input("ADICIONE UM ELEMENTO: ")

                        if elemento_adicionar_lista.replace(" ", "").isalpha():
                            lista.adicionar_na_lista(elemento_adicionar_lista)
                            limpar_tela()
                            print(f"✅ Adicionado com sucesso!")
                            
                        elif elemento_adicionar_lista == None:    
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

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
                            print(f"✅ Inserido com sucesso!")

                        elif posicao_lista == None or elemento_inserir_lista == None:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")       

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")   
                                
                    # Condicional da lista - Pesquisar elementos.
                    elif opcoes_lista == "4":
                        limpar_tela()  
                        menu_lista()  
                        elemento_pesquisar_lista = input("PESQUISAR NOME: ")

                        if not lista.iterar_lista():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")

                        elif elemento_pesquisar_lista.replace(" ", "").isalpha(): 
                            limpar_tela()
                            lista.pesquisar_por_letras(elemento_pesquisar_lista)
                            for itens in lista.estrutura_sublista:  
                                print(f"👤 {itens.title()}")  
                            if not lista.sublistar():
                                limpar_tela()
                                print(f"⚠️  Não encontrado!")        
                            lista.estrutura_sublista.clear()   
  
                        elif elemento_pesquisar_lista == None:  
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    # Condicional da lista - Excluir elementos.
                    elif opcoes_lista == "5":
                        limpar_tela()  
                        menu_lista()  
                        elemento_excluir_lista = input("EXCLUIR NOME: ")

                        if not lista.iterar_lista():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")
                 
                        elif elemento_excluir_lista == None:   
                            limpar_tela() 
                            print(f"❌ Entrada inválida!")   

                        elif elemento_excluir_lista.replace(" ", "").isalpha():

                            if elemento_excluir_lista.lower() not in lista.iterar_lista():
                                limpar_tela()
                                print(f"⚠️  {elemento_excluir_lista.title()} não está na lista.") 

                            else: 
                                lista.excluir_da_lista(elemento_excluir_lista)
                                limpar_tela()
                                print(f"✅ Excluído com sucesso!")

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")     

                    # Condicional da lista - Verificar quantidade de elementos.
                    elif opcoes_lista == "6":
                        limpar_tela()
                        menu_lista()
                        contar_elemento_lista = input("DIGITE O NOME: ")

                        if contar_elemento_lista.replace(" ", "").isalpha():
                            quantidade_elementos_lista = lista.quantidade_ocorrencias(contar_elemento_lista)
                            if not contar_elemento_lista in lista.iterar_lista():
                                limpar_tela()
                                print(f"⚠️  A lista possui {quantidade_elementos_lista} elementos do tipo {contar_elemento_lista.title()}.")  
                            else:
                                limpar_tela()
                                print(f"✅ A lista possui {quantidade_elementos_lista} elementos do tipo {contar_elemento_lista.title()}.")  

                        elif contar_elemento_lista == None:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")      

                        else:   
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                    # Condicional da lista - Limpar lista.
                    elif opcoes_lista == "7":
                        if not lista.iterar_lista():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")  

                        else:   
                            lista.limpar_lista()
                            limpar_tela()
                            print(f"✅ Lista Limpa!")

                    # Condicional da lista - Sai do while.
                    elif opcoes_lista == "8":
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()              

            # Condicional principal - Tupla.
            elif tipo_estrutura == "2":
                limpar_tela()

                # While da tupla
                while True:
                    menu_tupla()
                    opcoes_tupla = input("ESCOLHA UMA OPERAÇÃO: ")

                    # Condicional da tupla - Itera elementos.
                    if opcoes_tupla == "1":
                        limpar_tela()

                        if not tupla.iterar_tupla():
                            limpar_tela()
                            print("⚠️  Lista vazia")

                        elif opcoes_tupla == None:
                            limpar_tela()
                            print("❌ Entrada inválida!")

                        else:   
                            for itens in tupla.iterar_tupla():
                                print(f"👤 {itens.title()}") 

                    # Condicional da tupla - Pesquisar ocorrências dos elementos.
                    elif opcoes_tupla == "2": 
                        ocorrencias_tupla = input("DIGITE UM NOME: ")

                        if ocorrencias_tupla.replace(" ", "").isalpha():
                            if not ocorrencias_tupla in tupla.iterar_tupla():
                                limpar_tela()
                                print(f"⚠️  Não há ocorrência do elemento {ocorrencias_tupla.title()}.")
                            else:    
                                limpar_tela()
                                quantidade_elementos_tupla = tupla.contar_ocorrencias(ocorrencias_tupla)
                                limpar_tela()
                                print(f"✅ A tupla possui {quantidade_elementos_tupla} ocorrências do elemento {ocorrencias_tupla.title()}.")

                        elif ocorrencias_tupla == None:    
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                    # Condicional da tupla - Pesquisar índice dos elementos.
                    elif opcoes_tupla == "3": 
                        pesquisa_nome_tupla = input("DIGITE UM NOME: ")

                        if pesquisa_nome_tupla.replace(" ", "").isalpha():
                            if not pesquisa_nome_tupla in tupla.iterar_tupla():
                                limpar_tela()
                                print(f"⚠️  Não há ocorrência do elemento {pesquisa_nome_tupla.title()}.")
                            else:    
                                limpar_tela()
                                print(f"✅ A primeira ocorrência do elemento {pesquisa_nome_tupla.title()} está no índice {tupla.buscar_indice(pesquisa_nome_tupla)}.")

                        elif pesquisa_nome_tupla == None:  
                            limpar_tela()  
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                    # Condicional da tupla - Pesquisar quantidade de elementos.
                    elif opcoes_tupla == "4": 
                        limpar_tela()
                        print(f"✅ Existem {tupla.quantidade()} elementos na tupla.")

                    # Condicional da tupla - Pesquisa por elementos em ordem alfabética máxima.
                    elif opcoes_tupla == "5": 
                        ordem_maxima = tupla.ordem_maxima()
                        limpar_tela()
                        print(f"✅ {ordem_maxima.title()} é a primeira ocorrência do último elemento em ordem alfabética.") 

                    # Condicional da tupla - Pesquisa por elementos em ordem alfabética mínima.
                    elif opcoes_tupla == "6": 
                        ordem_minima = tupla.ordem_minima()
                        limpar_tela()
                        print(f"✅ {ordem_minima.title()} é a primeira ocorrência do primeiro elemento em ordem alfabética.")

                    # Condicional da tupla - Sai do while.
                    elif opcoes_tupla == "7": 
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()         

            elif tipo_estrutura == "3":
                limpar_tela()

                # While do conjunto(set)
                while True:
                    menu_conjunto()
                    opcoes_conjunto = input("ESCOLHA UMA OPERAÇÃO: ")

                    # Condicional do conjunto(set) - Iterar elementos.
                    if opcoes_conjunto == "1":
                        limpar_tela()
                        menu_lista()
                        
                        if not conjunto.iterar_conjunto():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")
                        else:   
                            limpar_tela()
                            for itens in conjunto.iterar_conjunto():
                                print(f"👤 {itens.title()}") 

                    # Condicional do conjunto(set) - Adicionar elementos.
                    elif opcoes_conjunto == "2":   
                        limpar_tela()
                        menu_lista()
                        elemento_adicionar_conjunto = input("ADICIONAR UM NOME: ")

                        if elemento_adicionar_conjunto.replace(" ", "").isalpha():
                            if elemento_adicionar_conjunto in conjunto.iterar_conjunto():  
                                limpar_tela() 
                                print(f"⚠️  O nome já existe!") 
                            else:    
                                conjunto.adicionar(elemento_adicionar_conjunto)
                                limpar_tela()
                                print(f"✅ Adicionado com sucesso!")  
                                        
                        elif elemento_adicionar_conjunto == None:  
                            limpar_tela()  
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    elif opcoes_conjunto == "3":   
                        elemento_excluir_conjunto = input("EXCLUIR NOME: ")
                        
                        if not conjunto.iterar_conjunto():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")

                        elif elemento_excluir_conjunto.replace(" ", "").isalpha():
                            if elemento_excluir_conjunto not in conjunto.iterar_conjunto():
                                limpar_tela()
                                print(f"⚠️  O elemento não está no conjunto!")  

                            else:    
                                conjunto.excluir(elemento_excluir_conjunto)
                                limpar_tela()
                                print(f"✅ Excluído com sucesso!")
                            
                        elif elemento_excluir_conjunto == None:  
                            limpar_tela()  
                            print(f"❌ Entrada inválida!") 

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                    elif opcoes_conjunto == "4":   
                        if not conjunto.iterar_conjunto():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")
                        else:   
                            conjunto.excluir_aleatorio()
                            limpar_tela()
                            print(f"✅ Excluído com sucesso!")

                    elif opcoes_conjunto == "5":   
                        if not conjunto.iterar_conjunto():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")

                        else:
                            limpar_tela()
                            print("✅ Conjunto criado:", conjunto.iterar_conjunto())
                            print("✅ Subconjunto para teste:", conjunto.conjunto_suporte)
                            print("✅ União dos conjuntos:", conjunto.uniao())

                    elif opcoes_conjunto == "6":   
                        pass         
                    elif opcoes_conjunto == "7":   
                        pass         
                    elif opcoes_conjunto == "8":   
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()       

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