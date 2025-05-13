import unittest

from estrutura_de_dados.conjunto.ClasseConjunto import ClasseConjunto

class TestClasseConjunto(unittest.TestCase):
    """Classe de testes para a classe ClasseConjunto."""

    def setUp(self):
        """Configuração do objeto conjunto(set)."""
        self.conjunto = ClasseConjunto()

    def test_listar(self):
        """Teste para validar o método listar."""
        self.conjunto.adicionar('carlos')
        self.assertEqual(self.conjunto.listar(), {'carlos'})      
        self.assertNotEqual(self.conjunto.listar(), {'jose'}) 
    
    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.conjunto.adicionar('maria')
        self.assertEqual(self.conjunto.listar(), {'maria'})      
        self.assertNotEqual(self.conjunto.listar(), {'jose'}) 

    def test_excluir(self):
        """Teste para validar o método excluir."""
        self.conjunto.adicionar('maria')
        self.conjunto.adicionar('teresa')
        self.conjunto.excluir('maria')
        self.assertEqual(self.conjunto.listar(), {'teresa'})      
        self.assertNotEqual(self.conjunto.listar(), {'jose'})        

    def test_excluir_aleatorio(self):
        """Teste para validar o método excluir_aleatorio."""
        self.conjunto.adicionar('carlos')
        self.conjunto.excluir_aleatorio()
        self.assertEqual(self.conjunto.listar(), set())      
        self.assertNotEqual(self.conjunto.listar(), {'jose'})         

    def test_uniao(self):
        """Teste para validar o método uniao."""
        self.conjunto.adicionar('jose carlos')
        self.assertEqual(self.conjunto.uniao(), {'jeck da costa', 'duda soares', 'jose carlos'})      
        self.assertNotEqual(self.conjunto.uniao(), {'jeck da costa', 'jose carlos', 'jose carlos'})         

    def test_intersecao(self):
        """Teste para validar o método intersecao."""
        self.conjunto.adicionar('jose carlos')
        self.assertEqual(self.conjunto.intersecao(), {'jose carlos'})      
        self.assertNotEqual(self.conjunto.intersecao(), {'jeck da costa'})           

    def test_diferenca(self):
        """Teste para validar o método diferenca."""
        self.conjunto.adicionar('jose carlos')
        self.assertEqual(self.conjunto.diferenca(), set())      
        self.assertNotEqual(self.conjunto.diferenca(), {'jeck da costa', 'jose carlos'})         