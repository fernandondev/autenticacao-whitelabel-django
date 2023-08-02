from django.test import TestCase
from .models import Usuario, Unidade

#Teste model Usuario
class UsuarioTestCase(TestCase):

    def setUp(self):
        Usuario.objects.create(
            first_name='Fernando',last_name='Santos',username='fernando.santos',
            email='fernando@fernando.com'
        )

    #Teste se a busca por usuários está correta
    def test_usuarios_model(self):
        usuario = Usuario.objects.get(first_name='Fernando')
        self.assertEquals(usuario.first_name, "Fernando")


#Teste model Unidade
class UnidadeTestCase(TestCase):

    def setUp(self):
        Unidade.objects.create(
            nome='teste', url_imagem='http://url.com.br'
        )

    #Teste se a busca por unidades está correta
    def test_unidades_model(self):
        unidade = Unidade.objects.get(url_imagem='http://url.com.br')
        self.assertEquals(unidade.url_imagem, "http://url.com.br")

