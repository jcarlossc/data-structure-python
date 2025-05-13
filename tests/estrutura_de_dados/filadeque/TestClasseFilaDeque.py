from collections import deque
import unittest

from estrutura_de_dados.filadeque.ClasseFilaDeque import ClasseFilaDeque

class TestClasseFilaDeque(unittest.TestCase):
    """Classe de testes para a classe ClasseFilaDeque."""

    def setUp(self):
        """Configuração do objeto Deque."""
        self.deque = ClasseFilaDeque()

    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.deque.adicionar('carlos')
        self.assertEqual(self.deque.listar(), deque(['carlos']))      
        self.assertNotEqual(self.deque.listar(), deque(['jose'])) 
    
    def test_listar(self):
        """Teste para validar o método listar."""
        self.deque.adicionar('jose')
        self.assertEqual(self.deque.listar(), deque(['jose']))      
        self.assertNotEqual(self.deque.listar(), deque(['carlos'])) 

    def test_adicionar_comeco(self):
        """Teste para validar o método adicionar_começo."""
        self.deque.adicionar('carlos')
        self.deque.adiciona_comeco('jose')
        self.assertEqual(self.deque.listar(), deque(['jose', 'carlos']))      
        self.assertNotEqual(self.deque.listar(), deque(['carlos', 'jose'])) 

    def test_remove_fim(self):
        """Teste para validar o método remover_fim."""
        self.deque.adicionar('carlos')
        self.deque.adicionar('jose')
        self.deque.remove_fim()
        self.assertEqual(self.deque.listar(), deque(['carlos']))      
        self.assertNotEqual(self.deque.listar(), deque(['jose'])) 

    def test_remover_primeiro(self):
        """Teste para validar o método remover_primeiro"""
        self.deque.adicionar('carlos')
        self.deque.adicionar('jose')
        self.deque.remover_primeiro()
        self.assertEqual(self.deque.listar(), deque(['jose']))      
        self.assertNotEqual(self.deque.listar(), deque(['carlos'])) 

    def test_limpar(self):
        """Teste para validar o método limpar."""
        self.deque.adicionar('carlos')
        self.deque.adicionar('jose')
        self.deque.limpar()
        self.assertEqual(self.deque.listar(), deque([]))      
        self.assertNotEqual(self.deque.listar(), deque(['carlos'])) 

