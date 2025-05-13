# from estrutura_de_dados.menu.Menu import Menu

# Menu.menu()




from queue import Queue
teste = Queue()

v1 = 'carlos'
v2 = 'jose'

teste.put(v1)
teste.put(v2)

print(teste.get())