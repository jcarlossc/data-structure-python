# Estudo sobre estruturas de dados em linguagem de programação Python.

Estudo sobre manipulação de estrutura de dados e os respectivos testes unitário em linguagem de programação Python e ambiente virtual VENV.

VENV: Um ambiente virtual em Python isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

## Sobre a manipulação das estruturas de dados Python deste projeto:
* Observação 01: todas as estruturas de dados estão configuradas para receberem NOMES, números só serão utilizados para indicar posições(index).
* Observação 02: as estruturas imutáveis (SET, FROZENSET) foram modificadas na classe Menu, com intuto de dar mais dinamismo à manipulação, ou seja, funciona com se fossem mutáveis para inserção.
* Observação 03: existe um conjunto adicionado com alguns nomes tanto em SET quanto em FROZENSET que será usado com os métotos UNIÃO(UNION), INTERSEÇÃO(INTERSECTION) e DIFERENÇA(DIFFERENCE); por isso, adicione o nome MARIA entre as suas inserções para que as saídas(prints) sejam melhor compreendidos.

* LISTA(LIST): sequência ordenada e mutável de elementos. Aceita valores duplicados.
* TUPLA(TUPLE): sequência ordenada e imutável de elementos. Aceita duplicatas.
* CONJUNTO(SET): coleção não ordenada, mutável e sem elementos duplicados.
* CONJUNTO CONGELADO(FROZENSET): versão imutável de set. Não permite modificações após a criação.
* DICIONÁRIO(DICT): coleção de pares chave-valor. Mutável e não ordenado - Python 3.6+ mantém ordem de inserção.
* DEQUE: Double-Ended Queue - fila de dois lados — permite inserção e remoção rápida tanto no início quanto no fim.
* QUEUE: Fila segura para threads, usada em programação concorrente. Usa a lógica FIFO - First-In First-Out.
* HEAPQ: fila de prioridade com base em heap binário mínimo - menor valor no topo. Usa list como estrutura base.

## Ferramentas utilizadas
* Linguagem de programação Python 3.9.13.
* Ambiente virtual VENV.
* Unitest.
* Git.
* GitHub.
* Visual studio code.
* Windows 10.

## Modo de utilizar - nesta ordem
* Clonar repositório.
* Entrar no diretório do projeto ```cd data-structure-python```. 
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar as dependências. Obs: Este projeto não contém módulos externos.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## Sobre os testes
O projeto também conta com classes de testes unitários com módulo Unittest. Seguem abaixo os comandos para serem executados na raiz do projeto.
* ```python -m unittest tests/estrutura_de_dados/lista/TestClasseLista.py```
* ```python -m unittest tests/estrutura_de_dados/tupla/TestClasseTupla.py```
* ```python -m unittest tests/estrutura_de_dados/conjunto/TestClasseConjunto.py```
* ```python -m unittest tests/estrutura_de_dados/conjuntocongelado/TestClasseFrozenset.py```
* ```python -m unittest tests/estrutura_de_dados/dicionario/TestClasseDicionario.py```
* ```python -m unittest tests/estrutura_de_dados/filadeque/TestClasseFilaDeque.py```
* ```python -m unittest tests/estrutura_de_dados/filaqueue/TestClasseFilaQueue.py```
* ```python -m unittest tests/estrutura_de_dados/filaheapq/TestClasseHeapq.py```

## Contribuição:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## Licença:
Este projeto é licenciado sob a Licença MIT.

## Comandos importantes
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para descrever as dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.


