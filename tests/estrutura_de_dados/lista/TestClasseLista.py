import unittest

from estrutura_de_dados.lista.ClasseLista import ClasseLista

class TestClasseLista(unittest.TestCase):
    """Classe de testes para a classe ClasseLista."""

    def setUp(self):
        """Configuração do objeto ContaPopança."""
        self.lista = ClasseLista()

    def test_adicionar(self):
        """Teste para validar o método adicionar."""
        self.lista.adicionar('carlos')
        self.assertEqual(self.lista.listar(), ['carlos'])      
        self.assertNotEqual(self.lista.listar(), ['jose']) 

    def test_listar(self):
        """Teste para validar o método adicionar."""
        self.lista.adicionar('carlos')
        self.lista.adicionar('jose')
        self.assertEqual(self.lista.listar(), ['carlos', 'jose'])      
        self.assertNotEqual(self.lista.listar(), ['maria', 'jose'])    

    def test_inserir_com_posicao(self):
        """Teste para validar o método inserir_com_posição."""
        self.lista.inserir_com_posicao(0, 'teresa')
        self.lista.inserir_com_posicao(1, 'maria')
        self.assertEqual(self.lista.listar(), ['teresa', 'maria'])      
        self.assertNotEqual(self.lista.listar(), ['carlos', 'soares'])     
    
    def test_pesquisar_por_letras(self):
        """Teste para validar o método pesquisar_por_letras."""
        self.lista.adicionar('carlos')
        self.lista.adicionar('costa')
        self.lista.pesquisar_por_letras('c')
        self.assertEqual(self.lista.sublistar(), ['carlos', 'costa'])      
        self.assertNotEqual(self.lista.sublistar(), ['maria', 'soares'])

    def test_excluir(self):
        """Teste para validar o método excluir."""
        self.lista.adicionar('carlos')
        self.lista.adicionar('costa')
        self.lista.excluir('carlos')
        self.assertEqual(self.lista.listar(), ['costa'])      
        self.assertNotEqual(self.lista.listar(), ['maria'])    

    def test_quantidade_ocorrencias(self):
        """Teste para validar o método quantidade_ocorrencias."""
        self.lista.adicionar('carlos')
        self.lista.adicionar('costa')
        self.lista.adicionar('carlos')
        self.assertEqual(self.lista.quantidade_ocorrencias('carlos'), 2)      
        self.assertNotEqual(self.lista.quantidade_ocorrencias('carlos'), 3)     

    def test_limpar_lista(self):
        """Teste para validar o método limpar_lista."""
        self.lista.adicionar('carlos')
        self.lista.adicionar('costa')
        self.lista.limpar_lista()
        self.assertEqual(self.lista.listar(), [])      
        self.assertNotEqual(self.lista.listar(), ['carlos'])     