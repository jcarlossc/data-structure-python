import os
from estrutura_de_dados.conjunto.ClasseConjunto import ClasseConjunto
from estrutura_de_dados.dicionario.ClasseDicionario import ClasseDicionario
from estrutura_de_dados.filadeque.ClasseFilaDeque import ClasseFilaDeque
from estrutura_de_dados.filaheapq.ClasseHeapq import ClasseHeapq
from estrutura_de_dados.filaqueue.ClasseFilaQueue import ClasseFilaQueue
from estrutura_de_dados.lista.ClasseLista import ClasseLista
from estrutura_de_dados.tupla.ClasseTupla import ClasseTupla
from estrutura_de_dados.conjuntocongelado.ClasseFrozenset import ClasseFrozenset

class Menu:
    def __init__(self):
        pass

    @classmethod    
    def menu(self):

        # Método principal.
        def menu_principal():
            print("\n------------------------🚀 ESTRUTURAS DE DADOS 🚀-----------------------")
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
            print("\n------------------------------🚀 LISTA 🚀-------------------------------")
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
            print("\n-------------------------------🚀 TUPLA 🚀------------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - PESQUISAR OCORRÊNCIAS")
            print("4 - PESQUISAR POR ÍNDICE")
            print("5 - QUANTIDADE DE ELEMENTOS")
            print("6 - ORDEM MÁXIMO")
            print("7 - ORDEM MÍNIMO")
            print("8 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")    

        # Método menu do conjunto(set).
        def menu_conjunto():
            print("\n--------------------------------🚀 SET 🚀-------------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - EXCLUIR")
            print("4 - EXCLUIR ALEATÓRIO")
            print("5 - UNIÃO")
            print("6 - INTERSEÇÃO")
            print("7 - DIFERENÇA")
            print("8 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")  

        # Método menu do conjunto(frozenset).
        def menu_conjunto_frozen():
            print("\n----------------------------🚀 FROZENSET 🚀-----------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - UNIÃO")
            print("4 - INTERSEÇÃO")
            print("5 - DIFERENÇA")
            print("6 - COPIAR")
            print("7 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")    

        # Método menu do dicionário.
        def menu_dicionario():
            print("\n----------------------------🚀 DICIONÁRIO 🚀----------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - BUSCA ELEMENTO")
            print("4 - COPIAR")
            print("5 - EXCLUIR")
            print("6 - LIMPAR")
            print("7 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")   

        # Método menu do deque.
        def menu_fila_deque():
            print("\n-----------------------------🚀 FILA_DEQUE 🚀---------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - ADICIONA NO COMEÇO")
            print("4 - REMOVER DO FIM")
            print("5 - REMOVER DO COMEÇO")
            print("6 - LIMPAR")
            print("7 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")      

        # Método menu do queue.
        def menu_fila_queue():
            print("\n------------------------------🚀 FILA_QUEUE 🚀--------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - QUANTIDADE")
            print("4 - VERIFICAR SE FILA CHEIA")
            print("5 - REMOVER")
            print("6 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")     

        # Método menu do heapq.
        def menu_fila_heapq():
            print("\n-----------------------------🚀 FILA_HEAPQ 🚀---------------------------")
            print("1 - LISTAR")
            print("2 - ADICIONAR")
            print("3 - QUANTIDADE")
            print("4 - EXCLUIR")
            print("5 - SAIR")
            print("---------------------------------- FIM ----------------------------------\n")     
         
        # Instâncias das classes das estruturas de dados.
        lista = ClasseLista()
        tupla = ClasseTupla()
        conjunto = ClasseConjunto()
        conjunto_frozen = ClasseFrozenset()
        dicionario = ClasseDicionario()
        fila_deque = ClasseFilaDeque()
        fila_queue = ClasseFilaQueue()
        fila_heapq = ClasseHeapq()

        # Método para limpar tela.
        def limpar_tela():
            os.system('cls' if os.name == 'nt' else 'clear')

        # Chama método para limpar tela.
        limpar_tela()    

        # While principal do menu.
        while True:  
            menu_principal()
            tipo_estrutura = input(f"🔍 ESCOLHA O TIPO DE ESTRUTURA DE DADOS: ")

            # Condicional principal - Lista.
            if tipo_estrutura == "1":
                limpar_tela()

                # While da lista.
                while True:
                    menu_lista()
                    opcoes_lista = input(f"🔍 ESCOLHA UMA OPERAÇÃO: ")
                    
                    # Condicional da lista - Itera elementos.
                    if opcoes_lista == "1":
                        limpar_tela()
                        if not lista.listar():
                            limpar_tela()
                            print(f"⚠️  Lista vazia!")

                        elif opcoes_lista == None:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                        else:   
                            for itens in lista.listar():
                                print(f"👤 {itens.title()}") 

                    # Condicional da lista - Adicionar elementos.
                    elif opcoes_lista == "2":
                        limpar_tela()
                        menu_lista()
                        elemento_adicionar_lista = input(f"🔍 ADICIONAR UM NOME: ")

                        if elemento_adicionar_lista.replace(" ", "").isalpha():
                            lista.adicionar(elemento_adicionar_lista.lower())
                            limpar_tela()
                            print(f"✅ {elemento_adicionar_lista.title()} Adicionado com sucesso!")
                            
                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    # Condicional da lista - Adicionar elementos com posição(index)
                    elif opcoes_lista == "3":
                        limpar_tela()
                        menu_lista()
                        posicao_lista = input(f"🔍 ADICIONAR A POSIÇÃO: ")  
                        elemento_inserir_lista = input(f"🔍 ADICIONAR O NOME: ")  

                        if posicao_lista.isdigit() and elemento_inserir_lista.replace(" ", "").isalpha():    
                            numero_lista = int(posicao_lista)
                            lista.inserir_com_posicao(numero_lista, elemento_inserir_lista.lower()) 
                            limpar_tela()
                            print(f"✅ {elemento_inserir_lista.title()} inserido com sucesso na posição {posicao_lista}.")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")   
                                
                    # Condicional da lista - Pesquisar elementos.
                    elif opcoes_lista == "4":
                        limpar_tela()  
                        menu_lista()  
                        elemento_pesquisar_lista = input(f"🔍 PESQUISAR POR LETRAS: ")

                        if not lista.listar():
                            limpar_tela()
                            print(f"⚠️  Lista vazia!")

                        elif elemento_pesquisar_lista.replace(" ", "").isalpha(): 
                            limpar_tela()
                            lista.pesquisar_por_letras(elemento_pesquisar_lista)

                            for itens in lista.estrutura_sublista:  
                                print(f"👤 {itens.title()}")  

                            if not lista.sublistar():
                                limpar_tela()
                                print(f"⚠️  Não encontrado!")    

                            lista.estrutura_sublista.clear()   
  
                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    # Condicional da lista - Excluir elementos.
                    elif opcoes_lista == "5":
                        limpar_tela()  
                        menu_lista()  
                        elemento_excluir_lista = input(f"🔍 EXCLUIR NOME: ")

                        if not lista.listar():
                            limpar_tela()
                            print(f"⚠️  Lista vazia")
                 
                        elif elemento_excluir_lista.replace(" ", "").isalpha():
                            if elemento_excluir_lista.lower() not in lista.listar():
                                limpar_tela()
                                print(f"⚠️  {elemento_excluir_lista.title()} não está na lista.") 

                            else: 
                                lista.excluir(elemento_excluir_lista)
                                limpar_tela()
                                print(f"✅ {elemento_excluir_lista.title()} excluído com sucesso!")

                        else:
                            limpar_tela()
                            print("❌ Entrada inválida!")     

                    # Condicional da lista - Verificar quantidade de elementos.
                    elif opcoes_lista == "6":
                        limpar_tela()
                        menu_lista()
                        contar_elemento_lista = input(f"🔍 DIGITE O NOME: ")

                        if contar_elemento_lista.replace(" ", "").isalpha():
                            quantidade_elementos_lista = lista.quantidade_ocorrencias(contar_elemento_lista)
                            if not contar_elemento_lista in lista.listar():
                                limpar_tela()
                                print(f"⚠️  A lista não possui elementos do tipo {contar_elemento_lista.title()}.")  
                            else:
                                limpar_tela()
                                print(f"✅ A lista possui {quantidade_elementos_lista} elementos do tipo {contar_elemento_lista.title()}.")  
     
                        else:   
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                    # Condicional da lista - Limpar lista.
                    elif opcoes_lista == "7":
                        if not lista.listar():
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

            # Condicional menu principal - Tupla.
            elif tipo_estrutura == "2":
                limpar_tela()

                # While da tupla
                while True:
                    menu_tupla()
                    opcoes_tupla = input(f"🔍 ESCOLHA UMA OPERAÇÃO: ")

                    # Condicional da tupla - Itera elementos.
                    if opcoes_tupla == "1":
                        limpar_tela()

                        if not tupla.listar():
                            limpar_tela()
                            print(f"⚠️  Tupla vazia!")

                        else:   
                            for itens in tupla.listar():
                                print(f"👤 {itens.title()}") 

                    # Condicional da tupla - Adiciona elementos.
                    elif opcoes_tupla == "2":
                        limpar_tela()
                        menu_tupla()
                        elemento_adicionar_tupla = input(f"🔍 ADICIONAR UM NOME: ")

                        if elemento_adicionar_tupla.replace(" ", "").isalpha():
                            tupla.adicionar(elemento_adicionar_tupla.lower())
                            limpar_tela()
                            print(f"✅ {elemento_adicionar_tupla.title()} Adicionado com sucesso!")
                            
                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                    # Condicional da tupla - Pesquisar ocorrências dos elementos.
                    elif opcoes_tupla == "3": 
                        limpar_tela()
                        menu_tupla()
                        ocorrencias_tupla = input(f"🔍 DIGITE UM NOME: ")

                        if ocorrencias_tupla.replace(" ", "").isalpha():
                            if not ocorrencias_tupla in tupla.listar():
                                limpar_tela()
                                print(f"⚠️  Não há ocorrência do elemento {ocorrencias_tupla.title()}.")
                            else:  
                                quantidade_elementos_tupla = tupla.contar_ocorrencias(ocorrencias_tupla)
                                limpar_tela()
                                print(f"✅ A tupla possui {quantidade_elementos_tupla} ocorrências do elemento {ocorrencias_tupla.title()}.")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                    # Condicional da tupla - Pesquisar índice dos elementos.
                    elif opcoes_tupla == "4": 
                        limpar_tela()
                        menu_tupla()
                        pesquisa_nome_tupla = input(f"🔍 DIGITE UM NOME: ")

                        if pesquisa_nome_tupla.replace(" ", "").isalpha():
                            if not pesquisa_nome_tupla in tupla.listar():
                                limpar_tela()
                                print(f"⚠️  Não há ocorrência do elemento {pesquisa_nome_tupla.title()}.")
                            else:    
                                limpar_tela()
                                print(f"✅ A primeira ocorrência do elemento {pesquisa_nome_tupla.title()} está no índice {tupla.buscar_indice(pesquisa_nome_tupla)}.")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!") 

                    # Condicional da tupla - Pesquisar quantidade de elementos.
                    elif opcoes_tupla == "5": 
                        limpar_tela()
                        print(f"✅ Existem {tupla.quantidade()} elementos na tupla.")

                    # Condicional da tupla - Pesquisa por elementos em ordem alfabética máxima.
                    elif opcoes_tupla == "6": 
                        ordem_maxima = tupla.ordem_maxima()
                        limpar_tela()
                        print(f"✅ {ordem_maxima.title()} é a primeira ocorrência do último elemento em ordem alfabética.") 

                    # Condicional da tupla - Pesquisa por elementos em ordem alfabética mínima.
                    elif opcoes_tupla == "7": 
                        ordem_minima = tupla.ordem_minima()
                        limpar_tela()
                        print(f"✅ {ordem_minima.title()} é a primeira ocorrência do primeiro elemento em ordem alfabética.")

                    # Condicional da tupla - Sai do while.
                    elif opcoes_tupla == "8": 
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()         

            # Condicional menu principal - Set.
            elif tipo_estrutura == "3":
                limpar_tela()

                # While do conjunto(set)
                while True:
                    menu_conjunto()
                    opcoes_conjunto = input(f"🔍 ESCOLHA UMA OPERAÇÃO: ")

                    # Condicional do conjunto(set) - Iterar elementos.
                    if opcoes_conjunto == "1":
                        limpar_tela()
                        menu_lista()
                        
                        if not conjunto.listar():
                            limpar_tela()
                            print(f"⚠️  Set vazio!")
                        else:   
                            limpar_tela()
                            for itens in conjunto.listar():
                                print(f"👤 {itens.title()}") 

                    # Condicional do conjunto(set) - Adicionar elementos.
                    elif opcoes_conjunto == "2":   
                        limpar_tela()
                        menu_conjunto()
                        elemento_adicionar_conjunto = input(f"🔍 ADICIONAR UM NOME: ")

                        if elemento_adicionar_conjunto.replace(" ", "").isalpha():
                            if elemento_adicionar_conjunto in conjunto.listar():  
                                limpar_tela() 
                                print(f"⚠️  {elemento_adicionar_conjunto.title()} já existe!") 
                            else:    
                                conjunto.adicionar(elemento_adicionar_conjunto)
                                limpar_tela()
                                print(f"✅ {elemento_adicionar_conjunto.title()} Adicionado com sucesso!")  

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    # Condicional do conjunto(set) - Exclui elementos.
                    elif opcoes_conjunto == "3":  
                        limpar_tela()
                        menu_conjunto()
                        elemento_excluir_conjunto = input(f"🔍 EXCLUIR NOME: ")
                        
                        if not conjunto.listar():
                            limpar_tela()
                            print(f"⚠️  Set vazio!")

                        elif elemento_excluir_conjunto.replace(" ", "").isalpha():
                            if elemento_excluir_conjunto not in conjunto.listar():
                                limpar_tela()
                                print(f"⚠️  O elemento {elemento_excluir_conjunto.title()} não está no conjunto!")  

                            else:    
                                conjunto.excluir(elemento_excluir_conjunto)
                                limpar_tela()
                                print(f"✅ {elemento_excluir_conjunto.title()} excluído com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")

                    # Condicional do conjunto(set) - Exclui elementos aleatórios.
                    elif opcoes_conjunto == "4":   
                        if not conjunto.listar():
                            limpar_tela()
                            print(f"⚠️  Set vazio!")
                        else:   
                            resultado = conjunto.excluir_aleatorio()
                            limpar_tela()
                            print(f"✅ {resultado.title()} excluído com sucesso!")

                    # Condicional do conjunto(set) - União de elementos.
                    elif opcoes_conjunto == "5":   
                        if not conjunto.listar():
                            limpar_tela()
                            print(f"⚠️  Set vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto criado: {conjunto.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto.conjunto_suporte}")
                            print(f"✅ União dos conjuntos: {conjunto.uniao()}")

                    # Condicional do conjunto(set) - Interseção de elementos.
                    elif opcoes_conjunto == "6":   
                        if not conjunto.listar():
                            print(f"⚠️  Set vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto criado: {conjunto.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto.conjunto_suporte}")
                            print(f"✅ interseção dos conjuntos: {conjunto.intersecao()}")

                    # Condicional do conjunto(set) - Diferença de elementos.
                    elif opcoes_conjunto == "7":   
                        if not conjunto.listar():
                            print(f"⚠️  Set vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto criado: {conjunto.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto.conjunto_suporte}")
                            print(f"✅ Diferença dos conjuntos:", conjunto.diferenca())

                    elif opcoes_conjunto == "8":   
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()       

            # Condicional menu principal - FrozenSet.
            elif tipo_estrutura == "4":
                limpar_tela()

                # While do conjunto (frozenset)
                while True:
                    menu_conjunto_frozen()
                    opcoes_conjunto_frozen = input(f"🔍 ESCOLHA A OPERAÇÃO: ")

                    # Condicional do conjunto(frozenset) - Itera elementos.
                    if opcoes_conjunto_frozen == "1":
                        limpar_tela()
                        menu_conjunto_frozen()

                        if not conjunto_frozen.listar():
                            limpar_tela()
                            print(f"⚠️  Frozenset vazio!")

                        else:   
                            limpar_tela()
                            for itens in conjunto_frozen.listar():
                                 print(f"👤 {itens.title()}") 

                    # Condicional do conjunto(frozenset) - Adicionar elementos.
                    elif opcoes_conjunto_frozen == "2":
                        limpar_tela()
                        menu_conjunto_frozen()
                        elemento_adicionar_frozenset = input(f"🔍 ADICIONAR UM NOME: ")

                        if elemento_adicionar_frozenset.replace(" ", "").isalpha():
                            if elemento_adicionar_frozenset in conjunto_frozen.listar():  
                                limpar_tela() 
                                print(f"⚠️  {elemento_adicionar_frozenset.title()} já existe!") 
                            else: 
                                conjunto_frozen.adicionar(elemento_adicionar_frozenset.lower())
                                limpar_tela()
                                print(f"✅ {elemento_adicionar_frozenset.title()} Adicionado com sucesso!")

                            
                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")               

                    # Condicional do conjunto(frozenset) - Unir elementos.
                    elif opcoes_conjunto_frozen == "3": 
                        if not conjunto_frozen.listar():
                            limpar_tela()
                            print(f"⚠️  Frozenset vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto: {conjunto_frozen.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto_frozen.conjunto_frozen_suporte}")
                            print(f"✅ União dos conjuntos: {conjunto_frozen.uniao()}")

                    # Condicional do conjunto(frozenset) - Interseção dos elementos.
                    elif opcoes_conjunto_frozen == "4": 
                        if not conjunto_frozen.listar():
                            limpar_tela()
                            print(f"⚠️  Frozenset vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto: {conjunto_frozen.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto_frozen.conjunto_frozen_suporte}")
                            print(f"✅ Interseção dos conjuntos: {conjunto_frozen.intersecao()}")

                    # Condicional do conjunto(frozenset) - Diferença dos elementos.
                    elif opcoes_conjunto_frozen == "5": 
                        if not conjunto_frozen.listar():
                            limpar_tela()
                            print(f"⚠️  Frozenset vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto: {conjunto_frozen.listar()}")
                            print(f"✅ Subconjunto para teste: {conjunto_frozen.conjunto_frozen_suporte}")
                            print(f"✅ Diferença dos conjuntos: {conjunto_frozen.diferenca()}")

                    # Condicional do conjunto(frozenset) - Copiar elementos.
                    elif opcoes_conjunto_frozen == "6": 
                        if not conjunto_frozen.listar():
                            print(f"⚠️  Frozenset vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Conjunto: {conjunto_frozen.listar()}")  
                            print(f"✅ Conjunto copiado: {conjunto_frozen.copiar()}")

                    elif opcoes_conjunto_frozen == "7": 
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()       
        
            # Condicional menu principal - Dicionário.
            elif tipo_estrutura == "5":
                limpar_tela()

                # While do dicionário.
                while True:
                    menu_dicionario()
                    opcoes_dicionario = input(f"🔍 ESCOLHA A OPERAÇÃO: ")

                    # Condicional do dicionário - Itera elementos.
                    if opcoes_dicionario == "1":
                        limpar_tela()
                        if not dicionario.listar():
                            print(f"⚠️  Dicionário vazio!")

                        elif opcoes_dicionario == None:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")     

                        else:   
                            limpar_tela()
                            for chave, valor in dicionario.listar().items():
                                print(f"👤 {chave}: {valor}")

                    # Condicional do dicionário - Adicionar elementos.
                    elif opcoes_dicionario == "2":
                        limpar_tela()
                        menu_lista()
                        nome_dicionario = input(f"🔍 ADICIONAR NOME: ")
                        idade_dicionario = input(f"🔍 ADICIONAR IDADE: ")

                        if nome_dicionario.replace(" ", "").isalpha() and idade_dicionario.isdigit():
                            numero_dicionario = int(idade_dicionario)
                            dicionario.adicionar(nome_dicionario, numero_dicionario)
                            limpar_tela()
                            print(f"✅ {nome_dicionario.title()} de {idade_dicionario} anos de idade foi adicionado com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")    

                    # Condicional do dicionário - Pesquisar elementos por index.
                    elif opcoes_dicionario == "3":
                        limpar_tela()
                        menu_dicionario()
                        numero_id = input(f"🔍 DIGITE O IDENTIFICADOR: ")    
                        
                        if numero_id.isdigit():
                            id_numero = int(numero_id)
                            if dicionario.pesquisar(id_numero) == None:
                                limpar_tela()
                                print(f"⚠️  Identificador não encontrado!")  

                            else:    
                                resultado = dicionario.pesquisar(id_numero)
                                limpar_tela() 
                                print(f"👤 {resultado}")
                        
                        else:
                            limpar_tela()
                            print(f"❌ Entrada inválida!")  

                    # Condicional do dicionário - Copiar elementos.
                    elif opcoes_dicionario == "4":
                        if not dicionario.listar():
                            limpar_tela()
                            print(f"⚠️  Dicionário vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ Dicionário: {dicionario.listar()}")  
                            print(f"✅ Dicionário copiado: {dicionario.copiar()}")   

                    # Condicional do dicionário - Excluir elementos.
                    elif opcoes_dicionario == "5":
                        limpar_tela()
                        menu_dicionario()
                        numero_dicionario_excluir = input(f"🔍 DIGITE O IDENTIFICADOR: ")   
                        
                        if numero_dicionario_excluir.isdigit():
                            dicionario_excluir = int(numero_dicionario_excluir) 

                            if dicionario.pesquisar(dicionario_excluir) == None:
                                limpar_tela()
                                print(f"⚠️  Identificador não encontrado!")  

                            else:  
                                limpar_tela()
                                print(f"✅ Excluído com sucesso! {dicionario.excluir(dicionario_excluir)}")
                            
                        else:
                            limpar_tela()
                            print(f"❌  Entrada inválida!")  

                    # Condicional do dicionário - Limpar dicionário.
                    elif opcoes_dicionario == "6":
                        if not dicionario.listar():
                            limpar_tela()
                            print(f"⚠️  Dicionário vazio!")    

                        else:
                            limpar_tela()
                            dicionario.limpar()
                            print(f"✅ Dicionário apagado com sucesso!")

                    elif opcoes_dicionario == "7":
                        break          
  
                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()         
            
            # Condicional menu principal - Deque.
            elif tipo_estrutura == "6":
                limpar_tela()

                # While do deque.
                while True:
                    menu_fila_deque()
                    opcoes_fila_deque = input(f"🔍 ESCOLHA A OPERAÇÃO: ")

                    # Condicional do deque - Iterar elementos.
                    if opcoes_fila_deque == "1":
                        if not fila_deque.listar():
                            limpar_tela()
                            print(f"⚠️  Deque vazio!")

                        else:   
                            limpar_tela()
                            for item in fila_deque.listar():
                                print(f"👤 {item.title()}")

                    # Condicional do deque - Adicionar elementos.
                    elif opcoes_fila_deque == "2":
                        limpar_tela()
                        menu_fila_deque()
                        nome_fila_deque = input(f"🔍 DIGITE UM NOME: ")

                        if nome_fila_deque.replace(" ", "").isalpha():
                            limpar_tela()
                            fila_deque.adicionar(nome_fila_deque.lower())
                            print(f"✅ {nome_fila_deque.title()} adicionado com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌  Entrada inválida!")  

                    # Condicional do deque - Adicionar elemento no começo.
                    elif opcoes_fila_deque == "3":
                        limpar_tela()
                        menu_fila_deque()
                        nome_fila_deque_comeco = input(f"🔍 DIGITE UM NOME: ")

                        if nome_fila_deque_comeco.replace(" ", "").isalpha():
                            if not fila_deque.listar():
                                limpar_tela()
                                print(f"⚠️  Deque vazio")

                            else:    
                                limpar_tela()
                                fila_deque.adiciona_comeco(nome_fila_deque_comeco)
                                print(f"✅ {nome_fila_deque_comeco.title()} adicionado no início com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌  Entrada inválida!") 
                        
                    # Condicional do deque - Excluir elemento do fim.    
                    elif opcoes_fila_deque == "4":
                        if not fila_deque.listar():
                            limpar_tela()
                            print(f"⚠️  Deque vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ {fila_deque.remove_fim().title()} removido do fim com sucesso!")  

                    # Condicional do deque - Excluir elemento do começo.  
                    elif opcoes_fila_deque == "5":
                        if not fila_deque.listar():
                            limpar_tela()
                            print(f"⚠️  Deque vazio!")

                        else:
                            limpar_tela()
                            print(f"✅ {fila_deque.remover_primeiro().title()} removido do início com sucesso!")  

                    # Condicional do deque - Limpar deque.  
                    elif opcoes_fila_deque == "6":
                        if not fila_deque.listar():
                            limpar_tela()
                            print(f"⚠️  Deque vazio!")

                        else:
                            limpar_tela()
                            fila_deque.limpar()
                            print(f"✅ Deque limpo com sucesso!")  

                    elif opcoes_fila_deque == "7":
                        break

                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela() 

            # Condicional menu principal - Queue.
            elif tipo_estrutura == "7":
                limpar_tela()

                # While do Queue.
                while True:
                    menu_fila_queue()
                    opcoes_fila_queue = input(f"🔍 ESCOLHA A OPERAÇÃO: ")

                    # Condicional do Queue - Iterar elementos.
                    if opcoes_fila_queue == "1":
                        if fila_queue.fila_queue.empty():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            temp_items = []
    
                            # Esvaziar a fila salvando os itens.
                            while not fila_queue.fila_queue.empty():
                                item = fila_queue.fila_queue.get()
                                temp_items.append(item)
                            
                            # Iterar sobre os itens.
                            for item in temp_items:
                                print(f"👤 {item.title()}")

                            # Colocar de volta na fila original.
                            for item in temp_items:
                                fila_queue.fila_queue.put(item)

                    # Condicional do Queue - Adicionar elementos.
                    elif opcoes_fila_queue == "2":
                        limpar_tela() 
                        menu_fila_queue()
                        elemento_fila_queue = input(f"🔍 DIGITE UM NOME: ")

                        if elemento_fila_queue.replace(" ", "").isalpha():

                            if fila_queue.verificar() == True:
                                limpar_tela()
                                print(f"⚠️  Queue Cheia!")

                            else:
                                limpar_tela()
                                fila_queue.adicionar(elemento_fila_queue.lower())
                                print(f"✅ {elemento_fila_queue.title()} adicionado com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌  Entrada inválida!")  

                    # Condicional do Queue - Quantidade de elementos.
                    elif opcoes_fila_queue == "3": 
                        if fila_queue.fila_queue.empty():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            print(f"✅ Quantidade de itens na Queue: {fila_queue.quantidade()}")  

                    # Condicional do Queue - Verifica se a queue está cheia(caso tamanho definido).                
                    elif opcoes_fila_queue == "4": 
                        if fila_queue.fila_queue.empty():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!") 

                        else:   
                            limpar_tela()
                            if fila_queue.verificar() == True:
                                print(f"⚠️  A fila está cheia.")
                            else:
                                print(f"✅ A fila não está cheia.")  

                    # Condicional do Queue - Exclui elementos.  
                    elif opcoes_fila_queue == "5": 
                        if fila_queue.fila_queue.empty():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            print(f"✅ {fila_queue.remover().title()} removido.") 

                    elif opcoes_fila_queue == "6": 
                        break    
                      
                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()      

            # Condicional menu principal - Heapq.
            elif tipo_estrutura == "8":
                limpar_tela()

                # While do Heapq.
                while True:
                    menu_fila_heapq()
                    opcoes_fila_heapq = input(f"🔍 ESCOLHA A OPERAÇÃO: ")

                    # Condicional do Heapq - Itera elementos.  
                    if opcoes_fila_heapq == "1":
                        if not fila_heapq.listar():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            print(f"{fila_heapq.listar()}")

                    # Condicional do Heapq - Adiciona elementos.  
                    elif opcoes_fila_heapq == "2":
                        limpar_tela()
                        menu_fila_heapq()
                        elemento_fila_heapq = input(f"🔍 DIGITE UM NOME: ")

                        if elemento_fila_heapq.replace(" ", "").isalpha():
                            limpar_tela()
                            fila_heapq.adicionar(elemento_fila_heapq.lower())
                            print(f"✅ {elemento_fila_heapq.title()} adicionado com sucesso!")

                        else:
                            limpar_tela()
                            print(f"❌  Entrada inválida!") 

                    # Condicional do Heapq - Quantidade de elementos.  
                    elif opcoes_fila_heapq == "3":
                        if not fila_heapq.listar():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            print(f"✅ A fila Queue possui {fila_heapq.quantidade()} elementos.")

                    # Condicional do Heapq - Exclui elementos.  
                    elif opcoes_fila_heapq == "4":
                        if not fila_heapq.listar():
                            limpar_tela()
                            print(f"⚠️  Queue vazio!")

                        else:   
                            limpar_tela()
                            fila_heapq.excluir()
                            print(f"✅ O primeiro elemento foi excluído com sucesso.")

                    elif opcoes_fila_heapq == "5":
                        break    
                      
                    else:
                        limpar_tela()
                        print(f"❌ Opção inválida.")

                limpar_tela()   

            elif tipo_estrutura == "9":
                limpar_tela()
                print("SAIR, ATÉ A PRÓXIMA!")
                exit()
                
            else:
                limpar_tela()
                print("❌ Opção inválida!")