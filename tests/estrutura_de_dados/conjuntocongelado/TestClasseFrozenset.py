import unittest

from estrutura_de_dados.conjuntocongelado.ClasseFrozenset import ClasseFrozenset

class TestClasseFrozenset(unittest.TestCase):
    """Classe de testes para a classe ClasseFrozenset."""

    def setUp(self):
        """Configuração do objeto Frozenset."""
        self.conjunto_frozen = ClasseFrozenset()

    def test_listar(self):
        """Teste para validar o método listar."""
        self.conjunto_frozen.adicionar('jose carlos')
        self.assertEqual(self.conjunto_frozen.listar(), ({'jose carlos'}))      
        self.assertNotEqual(self.conjunto_frozen.listar(), ({'carlos jose'})) 
    
    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.conjunto_frozen.adicionar('maria teresa')
        self.assertEqual(self.conjunto_frozen.listar(), ({'maria teresa'}))      
        self.assertNotEqual(self.conjunto_frozen.listar(), ({'carlos jose'}))     

    def test_uniao(self):
        """Teste para validar o método uniao."""
        self.conjunto_frozen.adicionar('maria teresa')
        self.conjunto_frozen.adicionar('jose carlos')
        self.assertEqual(self.conjunto_frozen.uniao(), ({'maria teresa', 'jose carlos', 'jeck soares'}))      
        self.assertNotEqual(self.conjunto_frozen.uniao(), ({'carlos jose'}))     

    def test_intersecao(self):
        """Teste para validar o método intersecao."""
        self.conjunto_frozen.adicionar('maria teresa')
        self.conjunto_frozen.adicionar('jose carlos')
        self.assertEqual(self.conjunto_frozen.intersecao(), ({'maria teresa', 'jose carlos'}))      
        self.assertNotEqual(self.conjunto_frozen.intersecao(), ({'carlos jose'}))         
 
    def test_diferenca(self):
        """Teste para validar o método diferenca."""
        self.conjunto_frozen.adicionar('maria teresa')
        self.conjunto_frozen.adicionar('jose carlos')
        self.assertEqual(self.conjunto_frozen.diferenca(), frozenset())      
        self.assertNotEqual(self.conjunto_frozen.diferenca(), ({'carlos jose'}))         

    def test_copiar(self):
        """Teste para validar o método copiar."""
        self.conjunto_frozen.adicionar('maria teresa')
        self.conjunto_frozen.adicionar('jose carlos')
        self.assertEqual(self.conjunto_frozen.copiar(), ({'maria teresa', 'jose carlos'}))      
        self.assertNotEqual(self.conjunto_frozen.copiar(), ({'carlos jose'}))         