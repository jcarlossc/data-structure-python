import unittest

from estrutura_de_dados.filaheapq.ClasseHeapq import ClasseHeapq 

class TestClasseHeapq(unittest.TestCase):
    """Classe de testes para a classe ClasseHeapq."""
    def setUp(self):
        """Configuração do objeto Heapq."""
        self.heap = ClasseHeapq()

    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.heap.adicionar("carlos")
        self.heap.adicionar("maria")
        self.assertEqual(self.heap.listar(), ['carlos', 'maria'])

    def test_excluir(self):
        """Teste para validar o método excluir."""
        self.heap.adicionar("antonio")
        self.heap.adicionar("carlos")
        self.heap.adicionar("maria")
        excluido = self.heap.excluir()
        self.assertEqual(excluido, 'antonio')

    def test_quantidade(self):
        """Teste para validar o método quantidade."""
        self.heap.adicionar("carlos")
        self.heap.adicionar("teresa")
        self.assertEqual(self.heap.quantidade(), 2)

    def test_ordenacao(self):
        """Teste para validar a ordenação."""
        elementos = ["carlos", "teresa", "antonio"]
        for el in elementos:
            self.heap.adicionar(el)
        self.assertEqual(self.heap.lista[0], 'antonio')