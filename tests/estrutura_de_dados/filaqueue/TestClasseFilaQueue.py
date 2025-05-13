import unittest

from estrutura_de_dados.filaqueue.ClasseFilaQueue import ClasseFilaQueue

class TestClasseFilaQueue(unittest.TestCase):
    """Classe de testes para a classe ClasseFilaQueue."""

    def setUp(self):
        """Configuração do objeto Queue."""
        self.filaqueue = ClasseFilaQueue()

    def test_quantidade(self):
        """Teste para validar o método quantidade."""
        self.filaqueue.adicionar('carlos')
        self.filaqueue.adicionar('teresa')
        self.assertEqual(self.filaqueue.quantidade(), 2)     
        self.assertNotEqual(self.filaqueue.quantidade(), 3) 

    def test_remover(self):
        """Teste para validar o método remover."""
        self.filaqueue.adicionar('carlos')
        self.assertEqual(self.filaqueue.remover(), 'carlos')

    def test_verificar(self):
        """Teste para validar o método verificar."""
        for nome in ['A', 'B', 'C', 'D', 'E']:
            self.filaqueue.adicionar(nome)
        self.assertTrue(self.filaqueue.verificar())

    def test_ordem(self):
        """Teste para validar o método ordem."""
        nomes = ['carlos', 'maria', 'jose']
        for nome in nomes:
            self.filaqueue.adicionar(nome)
        
        self.assertEqual(self.filaqueue.remover(), 'carlos')
        self.assertEqual(self.filaqueue.remover(), 'maria')
        self.assertEqual(self.filaqueue.remover(), 'jose')    